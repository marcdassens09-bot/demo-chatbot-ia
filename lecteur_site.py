# Lecture d'un site public pour la demo "Votre client".
# Securite : http/https seulement, ports 80/443, adresses internes refusees
# (a chaque redirection), pages limitees en taille et en temps.

import ipaddress
import socket
from html.parser import HTMLParser
from urllib.parse import urljoin, urlparse

import requests

TIMEOUT = 8
MAX_OCTETS = 1_500_000
MAX_REDIRECTIONS = 3
MAX_PAGES = 5
MAX_TEXTE_PAGE = 6000
MAX_TEXTE_TOTAL = 20000
MOTS_UTILES = (
    "contact", "horaire", "service", "prestation", "tarif", "prix", "propos",
    "qui-sommes", "qui sommes", "entreprise", "activite", "activité", "realisation",
    "réalisation", "menu", "carte", "produit", "zone", "intervention", "accueil",
)
ENTETES = {"User-Agent": "Mozilla/5.0 (compatible; MP-Solutions-IA-demo/1.0)"}


class SiteIllisible(Exception):
    """Message lisible par le comptable."""


def adresse_publique(hote):
    try:
        infos = socket.getaddrinfo(hote, None)
    except socket.gaierror:
        raise SiteIllisible("Ce site est introuvable. Vérifiez l'adresse.")
    for info in infos:
        ip = ipaddress.ip_address(info[4][0])
        if not ip.is_global:
            raise SiteIllisible("Cette adresse n'est pas autorisée.")
    return True


def verifier_url(url):
    p = urlparse(url)
    if p.scheme not in ("http", "https") or not p.hostname:
        raise SiteIllisible("L'adresse doit commencer par http:// ou https://")
    if p.port not in (None, 80, 443):
        raise SiteIllisible("Cette adresse n'est pas autorisée.")
    if p.username or p.password:
        raise SiteIllisible("Cette adresse n'est pas autorisée.")
    adresse_publique(p.hostname)
    return url


def normaliser(url):
    url = (url or "").strip()
    if not url:
        raise SiteIllisible("Indiquez l'adresse du site.")
    if len(url) > 300:
        raise SiteIllisible("Adresse trop longue.")
    if "://" not in url:
        url = "https://" + url
    return verifier_url(url)


def telecharger(url):
    """Retourne (url_finale, html). Redirections suivies a la main et reverifiees."""
    for _ in range(MAX_REDIRECTIONS + 1):
        verifier_url(url)
        try:
            r = requests.get(url, headers=ENTETES, timeout=TIMEOUT,
                             allow_redirects=False, stream=True)
        except requests.RequestException:
            raise SiteIllisible("Le site ne répond pas.")
        if r.is_redirect or r.status_code in (301, 302, 303, 307, 308):
            suivante = r.headers.get("Location")
            r.close()
            if not suivante:
                raise SiteIllisible("Le site ne répond pas correctement.")
            url = urljoin(url, suivante)
            continue
        if r.status_code >= 400:
            r.close()
            raise SiteIllisible(f"Le site répond par une erreur ({r.status_code}).")
        if "html" not in r.headers.get("Content-Type", "html").lower():
            r.close()
            raise SiteIllisible("Cette adresse n'est pas une page web.")
        morceaux, total = [], 0
        for bloc in r.iter_content(65536):
            total += len(bloc)
            if total > MAX_OCTETS:
                break
            morceaux.append(bloc)
        r.close()
        brut = b"".join(morceaux)
        encodage = r.encoding if r.encoding and r.encoding.lower() != "iso-8859-1" else None
        try:
            html = brut.decode(encodage or "utf-8")
        except (UnicodeDecodeError, LookupError):
            html = brut.decode("latin-1", errors="replace")
        return url, html
    raise SiteIllisible("Le site redirige trop de fois.")


class Extracteur(HTMLParser):
    IGNORES = {"script", "style", "noscript", "svg", "template", "iframe"}
    BLOCS = {"p", "div", "li", "br", "h1", "h2", "h3", "h4", "h5", "h6", "tr", "section",
             "article", "header", "footer", "address", "td", "dt", "dd", "nav", "ul"}
    ESPACES = {"a", "span", "button", "label", "strong", "em", "b", "i", "img"}

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.morceaux, self.liens, self.titre = [], [], ""
        self._ignore, self._dans_titre, self._lien = 0, False, None

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag in self.IGNORES:
            self._ignore += 1
        elif tag == "title":
            self._dans_titre = True
        elif tag == "a" and a.get("href"):
            self._lien = [a["href"], ""]
        elif tag == "meta" and a.get("name", "").lower() == "description" and a.get("content"):
            self.morceaux.append("\n" + a["content"] + "\n")
        if tag in self.BLOCS:
            self.morceaux.append("\n")
        elif tag in self.ESPACES:
            self.morceaux.append(" ")

    def handle_endtag(self, tag):
        if tag in self.IGNORES and self._ignore:
            self._ignore -= 1
        elif tag == "title":
            self._dans_titre = False
        elif tag == "a" and self._lien:
            self.liens.append(tuple(self._lien))
            self._lien = None
        if tag in self.BLOCS:
            self.morceaux.append("\n")
        elif tag in self.ESPACES:
            self.morceaux.append(" ")

    def handle_data(self, data):
        if self._ignore:
            return
        if self._dans_titre:
            self.titre += data
            return
        if self._lien is not None:
            self._lien[1] += data
        self.morceaux.append(data)

    def texte(self):
        lignes = [" ".join(l.split()) for l in "".join(self.morceaux).splitlines()]
        propres, vues = [], set()
        for l in lignes:
            if l and l not in vues:
                vues.add(l)
                propres.append(l)
        return "\n".join(propres)


def extraire(html):
    e = Extracteur()
    try:
        e.feed(html)
    except Exception:
        pass
    return e.titre.strip(), e.texte(), e.liens


def pages_utiles(base, liens):
    hote = urlparse(base).hostname
    choisies = []
    for href, texte in liens:
        if href.startswith(("mailto:", "tel:", "javascript:", "#")):
            continue
        url = urljoin(base, href).split("#")[0]
        if urlparse(url).hostname != hote or url.rstrip("/") == base.rstrip("/"):
            continue
        if url.lower().endswith((".pdf", ".jpg", ".jpeg", ".png", ".gif", ".zip", ".doc", ".docx")):
            continue
        cle = (url + " " + texte).lower()
        if any(m in cle for m in MOTS_UTILES) and url not in choisies:
            choisies.append(url)
    return choisies[: MAX_PAGES - 1]


def lire_site(url):
    """Retourne {"url", "titre", "texte", "pages"} ou leve SiteIllisible."""
    url = normaliser(url)
    url, html = telecharger(url)
    titre, texte, liens = extraire(html)
    blocs = [f"=== PAGE : {url} ===\n{texte[:MAX_TEXTE_PAGE]}"]
    lues = [url]
    for autre in pages_utiles(url, liens):
        try:
            u, h = telecharger(autre)
        except SiteIllisible:
            continue
        _, t, _ = extraire(h)
        if t:
            blocs.append(f"=== PAGE : {u} ===\n{t[:MAX_TEXTE_PAGE]}")
            lues.append(u)
        if sum(len(b) for b in blocs) > MAX_TEXTE_TOTAL:
            break
    tout = "\n\n".join(blocs)[:MAX_TEXTE_TOTAL]
    if len(tout) < 200:
        raise SiteIllisible(
            "Je n'arrive presque rien à lire sur ce site (il est peut-être fait d'images "
            "ou de JavaScript). Prenez plutôt un métier fictif."
        )
    return {"url": url, "titre": titre, "texte": tout, "pages": lues}
