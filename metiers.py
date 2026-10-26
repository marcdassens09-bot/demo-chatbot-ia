# Fiches FICTIVES pour la demo destinee aux experts-comptables (/comptable)
# Aucune de ces entreprises n'existe. Pas de vrai numero de telephone.

METIERS = {
    "plombier": {
        "emoji": "🔧",
        "metier": "Plombier-chauffagiste",
        "nom": "Martin Plomberie Chauffage",
        "artisan": "Julien Martin",
        "infos": """
Entreprise fictive de démonstration, basée à Lézat-sur-Lèze (Ariège). Chauffagiste et plombier depuis plus de 10 ans, une petite équipe d'artisans.
Labels : artisan RGE (QualiPAC pour les pompes à chaleur), Qualibat, Professionnel du Gaz.

Chauffage (toutes énergies) : installation de chaudières gaz et fioul, pompes à chaleur air/eau et air/air, remplacement d'un ancien chauffage, plancher chauffant, entretien annuel de chaudière, dépannage chaudière et chauffage.
Plomberie et salle de bain : création de salle de bain avec plan en 3D pour visualiser le projet avant les travaux, rénovation complète, remplacement de WC, douche, baignoire, lavabo, recherche et réparation de fuites, débouchage, chauffe-eau et ballon thermodynamique, adoucisseur d'eau.
Climatisation : climatisation réversible et gainable, entretien et dépannage.

Horaires : du lundi au vendredi 8h-12h et 13h30-18h. Samedi matin pour les urgences uniquement.
Urgences (fuite importante, plus d'eau chaude, plus de chauffage) : rappel dans l'heure en journée.
Zone : Lézat-sur-Lèze, Saverdun, Le Fossat, Artigat, Pamiers et 25 km autour.
Déplacement dépannage : 45 euros TTC, offert si les travaux sont acceptés.
Entretien chaudière gaz : à partir de 120 euros TTC.
Démarche pour un projet : le client décrit son projet, une visite sur place est fixée sous 7 jours, puis un devis gratuit et détaillé est envoyé.
""",
        "suggestions": [
            "J'ai une fuite sous l'évier",
            "Vous installez des pompes à chaleur ?",
            "Je voudrais refaire ma salle de bain",
            "Combien pour l'entretien de ma chaudière ?",
        ],
    },
    "electricien": {
        "emoji": "⚡",
        "metier": "Électricien",
        "nom": "Garcia Électricité",
        "artisan": "Thomas Garcia",
        "infos": """
Entreprise fictive de démonstration, basée à Saverdun (Ariège).
Services : dépannage électrique, mise aux normes, rénovation de tableau électrique, installation de bornes de recharge pour voiture électrique, éclairage, domotique, diagnostic avant vente.
Horaires : du lundi au vendredi 7h30-12h et 13h30-17h30.
Urgences (plus de courant, disjoncteur qui saute sans arrêt, odeur de brûlé) : rappel dans l'heure en journée. En cas de fumée ou de danger immédiat : couper le courant au disjoncteur général et appeler le 18 ou le 112.
Zone : Saverdun, Pamiers, Mazères, Lézat-sur-Lèze, Le Fossat et 30 km autour.
Déplacement dépannage : 50 euros TTC.
Borne de recharge : devis gratuit après visite technique.
""",
        "suggestions": [
            "Mon disjoncteur saute tout le temps",
            "Vous installez des bornes de recharge ?",
            "Je veux refaire mon tableau électrique",
            "Vous êtes ouverts le samedi ?",
        ],
    },
    "boulangerie": {
        "emoji": "🥖",
        "metier": "Boulangerie",
        "nom": "Boulangerie du Moulin",
        "artisan": "Sophie et Karim",
        "infos": """
Boulangerie-pâtisserie fictive de démonstration, à Pailhès (Ariège). Tenue par un couple : Karim au fournil, Sophie en boutique.
Le pain : levain naturel, pétrissage lent et façonnage à la main. Pain simple : farine, eau, sel, et rien d'autre. Farines bio en grande partie, œufs d'une ferme voisine, fruits de la région selon la saison.
Horaires : du mardi au samedi 6h30-13h et 15h30-19h, dimanche 7h-12h30. Fermé le lundi.

Pains au levain : pain du Moulin (farine semi-complète moulue à la meule), pain aux graines (tournesol, courge, pavot, lin), pain complet, pain aux noix, pain miel et noisettes, pain raisins et amandes, pain aux olives noires, tourte de seigle, pain d'épeautre, pain blanc, baguette tradition, pain de mie.
Viennoiseries : croissant, pain au chocolat, pain aux raisins, brioche nature, brioche aux pépites de chocolat, brioche aux pralines, roulé à la cannelle.
Pâtisseries : tarte aux pommes, tarte citron, tarte chocolat noisettes, flan, carrot cake, brownie, cookies (chocolat noir, chocolat et noisettes, avoine et coco).
Salé : fougasse aux olives et romarin, fougasse lardons et fromage, focaccia.
Gâteaux d'anniversaire et grosses quantités de pain : à commander au moins 48 heures à l'avance, par téléphone ou en boutique, à retirer en boutique.

Allergènes : la liste des allergènes de chaque produit est affichée en boutique ; pour une allergie, toujours confirmer avec l'équipe. Pas de produits certifiés sans gluten.
Paiement : espèces, carte bancaire.
""",
        "suggestions": [
            "Vous êtes ouverts le lundi ?",
            "Vous faites du pain au levain ?",
            "Je voudrais commander un gâteau pour samedi",
            "Vous avez du pain sans gluten ?",
        ],
    },
    "restaurant": {
        "emoji": "🍽",
        "metier": "Restaurant",
        "nom": "Restaurant Le Platane",
        "artisan": "l'équipe du Platane",
        "infos": """
Restaurant fictif de démonstration, à Pamiers (Ariège). Tenu par un couple : Antoine en cuisine, Lucie en salle.
Cuisine maison du marché : tout est fait sur place, desserts compris. Viandes d'éleveurs ariégeois, fromages de pays, légumes de maraîchers voisins, selon la saison.
Horaires : du mardi au samedi, midi 12h-14h et soir 19h-21h30. Dimanche midi uniquement (12h-14h30). Fermé le lundi.

Menu du jour : du mardi au samedi à midi. Il change TOUS LES JOURS, Antoine le choisit le matin selon le marché, et il est écrit sur l'ardoise. Entrée + plat + dessert 16,50 euros ; entrée + plat ou plat + dessert 13,50 euros ; plat seul 10,50 euros. Chaque jour, le plat existe aussi en version végétarienne.
Dimanche midi : menu du dimanche (entrée, plat, dessert) 26 euros, lui aussi différent chaque semaine.
Menu du jour à emporter : à commander avant 11h30, à retirer entre 12h et 12h30.

La carte (le soir, du mardi au samedi) :
Entrées : velouté de saison 8 euros, salade de chèvre chaud de l'Ariège au miel 10 euros, terrine de campagne maison 9 euros.
Plats : azinat (potée ariégeoise au chou) 18 euros, magret de canard sauce aux cèpes 22 euros, truite de l'Ariège au beurre blanc 19 euros, burger de bœuf gascon et frites maison 17 euros, risotto aux champignons (végétarien) 16 euros.
Desserts : croustade aux pommes 8 euros, crème brûlée 7 euros, assiette de fromages de pays 8 euros.
Menu enfant (moins de 12 ans) : plat, dessert et boisson 9 euros, midi et soir.

Groupes : jusqu'à 30 personnes, menu groupe sur demande (anniversaires, repas de famille, repas d'entreprise).
Terrasse ombragée sous le platane de mai à septembre.
Réservation conseillée le vendredi soir, le samedi et le dimanche.
Allergènes : la liste est disponible auprès de l'équipe ; pour une allergie, toujours la signaler à la réservation et la confirmer avec Lucie. Pas de cuisine certifiée sans gluten.
Paiement : carte bancaire, espèces, titres-restaurant le midi.
""",
        # Le menu du jour change chaque jour : voir menu_du_jour() plus bas.
        "menus_du_jour": True,
        "suggestions": [
            "C'est quoi le menu du jour ?",
            "Une table pour 4 samedi soir ?",
            "Vous avez des plats végétariens ?",
            "On est 25 pour un anniversaire",
        ],
    },
    "paysagiste": {
        "emoji": "🌳",
        "metier": "Paysagiste",
        "nom": "Jardins Delmas",
        "artisan": "Pierre Delmas",
        "infos": """
Entreprise de paysage fictive de démonstration, basée à Artigat (Ariège). Pierre Delmas, paysagiste depuis 15 ans, et un salarié.
Façon de travailler : pas de produits chimiques (désherbage à la main ou à la binette), outils sur batterie plus silencieux, déchets verts emmenés à la déchetterie ou broyés en paillage sur place si le client le souhaite.

Entretien : tonte, taille de haies et d'arbustes, désherbage des massifs et des allées, ramassage des feuilles, nettoyage de printemps et d'automne, débroussaillage de terrains en friche.
Arbres : élagage et taille des arbres fruitiers et d'ornement, abattage de petits arbres, dessouchage. Pour les grands arbres proches d'une maison ou d'une ligne électrique : visite obligatoire avant tout devis.
Création : jardin complet sur plan, engazonnement, haies et massifs, plantations (plantes adaptées au climat ariégeois et peu gourmandes en eau), arrosage automatique, allées en gravier, bordures, petits murets en pierre, terrasses en bois, pose de clôtures et de portails de jardin.

Horaires : du lundi au vendredi 8h-18h. Pas d'intervention le week-end.
Zone : Artigat, Le Fossat, Lézat-sur-Lèze, Pamiers, Saverdun et 30 km autour.
Tarifs : entretien de jardin 38 euros TTC de l'heure ; évacuation des déchets verts en plus, selon le volume. Création, élagage, abattage : sur devis.
Devis : gratuit, après une visite sur place fixée sous 10 jours ; le devis est envoyé par email dans la semaine qui suit.
Contrat d'entretien à l'année : passages réguliers (toutes les 2 semaines en saison, une fois par mois l'hiver), prix fixé au devis.
Par mauvais temps (pluie forte, gel), le passage est décalé et le client est prévenu.
Paiement : virement, chèque, CESU préfinancé.
Les travaux d'entretien de jardin chez les particuliers peuvent ouvrir droit à l'avantage fiscal des services à la personne selon les conditions en vigueur ; l'entreprise précise ce point sur le devis.
""",
        "suggestions": [
            "Il faut tailler une haie de 30 mètres",
            "Vous faites des contrats d'entretien ?",
            "Vous venez jusqu'à Pamiers ?",
            "C'est déductible des impôts ?",
        ],
    },
    "garagiste": {
        "emoji": "🚗",
        "metier": "Garagiste",
        "nom": "Garage des Coteaux",
        "artisan": "Nicolas Ferrer",
        "infos": """
Garage fictif de démonstration, à Saint-Ybars (Ariège). Garage indépendant toutes marques, tenu par Nicolas Ferrer et un mécanicien.
Entretien : vidange, révision selon le carnet d'entretien du constructeur, filtres, bougies, courroie de distribution, recharge de climatisation.
Réparation : freins (plaquettes, disques), embrayage, échappement, amortisseurs, batterie, démarreur, alternateur, diagnostic électronique des voyants.
Pneus : montage, équilibrage, géométrie, pneus hiver et 4 saisons, sur devis selon la taille.
Voitures hybrides et électriques : entretien courant seulement (freins, pneus, filtres, climatisation). Pas d'intervention sur la batterie haute tension : il faut voir le concessionnaire de la marque.
Contrôle technique : le garage ne le fait pas, mais prépare la voiture avant le passage et fait les réparations demandées après une contre-visite.
Pièces : d'origine ou de qualité équivalente, au choix du client, indiqué sur le devis.

Horaires : du lundi au vendredi 8h-12h et 14h-18h30, samedi 8h-12h. Fermé le dimanche.
Rendez-vous : en général sous une semaine pour un entretien. Devis gratuit avant toute réparation, rien n'est fait sans l'accord du client.
Tarifs : main-d'œuvre 65 euros TTC de l'heure ; vidange avec filtre à huile à partir de 89 euros TTC (petite citadine) ; diagnostic électronique 49 euros TTC, déduit si la réparation est faite au garage. Les autres prix dépendent du modèle de la voiture : sur devis.
Véhicule de courtoisie : une voiture de prêt, sur réservation, pour les réparations de plus d'une journée.
Dépannage : remorquage en journée dans un rayon de 20 km autour de Saint-Ybars. Pas de dépannage sur autoroute (il faut utiliser les bornes d'appel ou appeler le 112).
Paiement : carte bancaire, espèces, chèque.
Le garage ne peut pas faire de diagnostic à distance : seul un passage au garage permet de savoir ce qu'a la voiture et combien coûtera la réparation.
Sécurité : voyant rouge allumé, fumée, odeur de brûlé ou freins qui répondent mal : s'arrêter dès que possible en lieu sûr et ne pas reprendre la route.
""",
        "suggestions": [
            "Mon voyant moteur s'est allumé",
            "Combien pour une vidange ?",
            "Vous faites le contrôle technique ?",
            "Vous avez une voiture de prêt ?",
        ],
    },
}


# ---------- Menu du jour du restaurant fictif ----------
# 14 menus qui tournent : le menu change chaque jour et ne revient
# qu'au bout de deux semaines. Le chatbot ne connait QUE celui du jour.
MENUS = [
    ("Velouté de potiron", "Sauté de porc noir de Bigorre aux pommes", "Gratin de potiron et pommes de terre", "Croustade aux pommes"),
    ("Salade de lentilles du Puy", "Cuisse de poulet fermier rôtie, purée maison", "Galette de lentilles et légumes rôtis", "Crème caramel"),
    ("Œuf cocotte aux champignons", "Azinat (potée ariégeoise au chou)", "Chou farci aux légumes et au riz", "Tarte aux poires"),
    ("Carottes râpées à l'orange", "Filet de truite de l'Ariège, riz pilaf", "Curry de légumes et riz pilaf", "Mousse au chocolat"),
    ("Terrine de campagne maison", "Bœuf bourguignon, pâtes fraîches", "Pâtes fraîches aux champignons et à la crème", "Île flottante"),
    ("Soupe de légumes du jardin", "Saucisse de Toulouse, haricots blancs", "Haricots blancs mijotés à la tomate", "Riz au lait"),
    ("Salade de betteraves et chèvre frais", "Blanquette de veau à l'ancienne", "Blanquette de légumes au lait de coco", "Tarte au citron"),
    ("Poireaux vinaigrette", "Confit de canard, pommes sarladaises", "Omelette aux cèpes, pommes sarladaises", "Fromage blanc au miel"),
    ("Velouté de châtaignes", "Daube de bœuf à l'ariégeoise", "Lasagnes aux légumes d'automne", "Gâteau basque"),
    ("Salade de chèvre chaud", "Pavé de merlu, fondue de poireaux", "Tarte fine aux poireaux et au fromage de pays", "Compote maison et sablé"),
    ("Crème de lentilles", "Rôti de porc au lait, gratin dauphinois", "Gratin dauphinois et salade verte", "Flan pâtissier"),
    ("Céleri rémoulade", "Mounjetado (haricots et saucisse du pays)", "Mounjetado végétarien aux haricots tarbais", "Poire pochée au vin"),
    ("Assiette de charcuterie du pays", "Poulet basquaise, riz", "Piperade aux œufs et riz", "Moelleux au chocolat"),
    ("Soupe à l'oignon", "Hachis parmentier maison", "Parmentier de lentilles et patate douce", "Crumble pommes-cannelle"),
]

JOURS = ["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche"]
MOIS = ["janvier", "février", "mars", "avril", "mai", "juin", "juillet",
        "août", "septembre", "octobre", "novembre", "décembre"]


def maintenant_france():
    """Date et heure en France (le serveur Render est a l'heure UTC)."""
    from datetime import datetime, timedelta, timezone
    try:
        from zoneinfo import ZoneInfo
        return datetime.now(ZoneInfo("Europe/Paris"))
    except Exception:
        return datetime.now(timezone.utc) + timedelta(hours=1)


def date_en_clair(moment):
    return f"{JOURS[moment.weekday()]} {moment.day} {MOIS[moment.month - 1]} {moment.year}"


HISTORIQUE_JOURS = 14  # le chatbot se souvient des menus des 2 dernieres semaines


def _menu_de(jour_date):
    """Le menu servi un jour donne (None le lundi : ferme)."""
    if jour_date.weekday() == 0:
        return None
    entree, plat, vege, dessert = MENUS[jour_date.toordinal() % len(MENUS)]
    nom = "menu du dimanche (26 euros)" if jour_date.weekday() == 6 else "menu du jour"
    return (f"{nom} : entrée : {entree} ; plat : {plat}, ou en version végétarienne : {vege} ; "
            f"dessert : {dessert}")


def menu_du_jour(moment=None):
    """Texte ajoute aux infos du restaurant : le menu d'aujourd'hui et ceux des 2 dernieres semaines."""
    from datetime import timedelta
    moment = moment or maintenant_france()
    aujourd_hui = moment.date()
    lignes = []
    for n in range(HISTORIQUE_JOURS + 1):
        jour = aujourd_hui - timedelta(days=n)
        etiquette = "AUJOURD'HUI" if n == 0 else ("hier" if n == 1 else f"il y a {n} jours")
        menu = _menu_de(jour) or "fermé (fermé le lundi), pas de menu"
        lignes.append(f"- {date_en_clair(jour)} ({etiquette}) : {menu}")
    regle = ("Le menu change chaque jour. Tu connais celui d'aujourd'hui et ceux des deux dernières "
             "semaines (liste ci-dessus), avec leur date : utilise la date exacte quand on te parle "
             "d'hier, de samedi dernier, etc. Pour un jour à venir (demain, samedi prochain…), dis "
             "qu'Antoine le choisit le matin même selon le marché et qu'il n'est pas encore connu. "
             "Au-delà de deux semaines, dis que tu ne l'as plus. N'invente jamais un menu.")
    return "MENUS DU RESTAURANT (le menu du jour est servi à midi) :\n" + "\n".join(lignes) + "\n" + regle
