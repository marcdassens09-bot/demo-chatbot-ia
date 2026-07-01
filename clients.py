# Fiches clients - une fiche par entreprise
# Ajoute un nouveau bloc pour chaque nouveau client

CLIENTS = {
    "default": {
        "nom": "notre entreprise",
        "secteur": "artisanat",
        "description": "une entreprise locale",
        "infos": "Aucune information specifique disponible pour ce client."
    },
    "plombier": {
        "nom": "Plomberie Dupont",
        "secteur": "plomberie",
        "description": "une entreprise de plomberie et de depannage",
        "infos": """
Services : depannage fuite d'eau, installation sanitaire, chauffe-eau, debouchage canalisation.
Horaires : du lundi au vendredi 8h-18h, urgences 7j/7.
Zone d'intervention : Ariege et communes limitrophes.
Devis gratuit sur demande.
"""
    },
    "restaurant": {
        "nom": "Le Bon Repas",
        "secteur": "restauration",
        "description": "un restaurant traditionnel",
        "infos": """
Cuisine : traditionnelle francaise, produits locaux et de saison.
Horaires : du mardi au dimanche, 12h-14h et 19h-22h. Ferme le lundi.
Reservation conseillee le week-end.
Menu du jour a midi en semaine.
"""
    },
    "artisan": {
        "nom": "Artisan Renov",
        "secteur": "renovation batiment",
        "description": "une entreprise de renovation et travaux",
        "infos": """
Services : renovation interieure, peinture, isolation, petits travaux.
Horaires : du lundi au vendredi 8h-17h.
Devis gratuit, deplacement dans un rayon de 30km.
"""
    },
}

def get_client(client_id):
    return CLIENTS.get(client_id, CLIENTS["default"])
