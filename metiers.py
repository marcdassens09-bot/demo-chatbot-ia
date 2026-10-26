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
Entreprise de paysage fictive de démonstration, basée à Artigat (Ariège).
Services : tonte, taille de haies, élagage, débroussaillage, création de jardins, plantations, entretien à l'année par contrat.
Horaires : du lundi au vendredi 8h-18h.
Zone : Artigat, Le Fossat, Lézat-sur-Lèze, Pamiers, Saverdun et 30 km autour.
Devis gratuit après visite sur place.
Contrat d'entretien annuel possible (passages réguliers).
Les travaux d'entretien de jardin chez les particuliers peuvent ouvrir droit à l'avantage fiscal des services à la personne selon les conditions en vigueur ; l'entreprise précise ce point sur le devis.
""",
        "suggestions": [
            "Il faut tailler une haie de 30 mètres",
            "Vous faites des contrats d'entretien ?",
            "Vous venez jusqu'à Pamiers ?",
            "C'est déductible des impôts ?",
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


def menu_du_jour(moment=None):
    """Texte ajoute aux infos du restaurant : le menu d'aujourd'hui, et rien d'autre."""
    moment = moment or maintenant_france()
    jour = moment.weekday()
    quand = date_en_clair(moment)
    regle = ("Le menu change chaque jour. Tu ne connais QUE celui d'aujourd'hui : pour un autre jour "
             "(demain, samedi, la semaine prochaine…), dis qu'Antoine le choisit le matin même selon "
             "le marché et qu'il n'est pas encore connu. N'invente jamais un menu.")
    if jour == 0:
        return (f"AUJOURD'HUI ({quand}) : le restaurant est fermé (fermé le lundi), donc pas de menu du jour. "
                + regle)
    entree, plat, vege, dessert = MENUS[moment.date().toordinal() % len(MENUS)]
    nom = "MENU DU DIMANCHE (26 euros)" if jour == 6 else "MENU DU JOUR (servi à midi)"
    return (f"{nom} D'AUJOURD'HUI, {quand} : entrée : {entree} ; plat : {plat}, "
            f"ou en version végétarienne : {vege} ; dessert : {dessert}. " + regle)
