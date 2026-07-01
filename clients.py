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
    "camping": {
        "nom": "Camping Les Eychecadous",
        "secteur": "camping et hebergement touristique",
        "description": "un camping familial 3 etoiles a Artigat en Ariege",
        "infos": """
Situe en bordure de la riviere Leze, cadre naturel et calme.
Hebergements : 39 emplacements pour tente/caravane/camping-car, 9 bungalows toiles, 4 mobil-homes.
Piscine ouverte du 15 mai au 15 septembre.
Services : buvette, restauration snack, wifi gratuit, animaux acceptes.
Telephone : 05 67 44 51 65.
Horaires d'accueil : basse saison 9h-12h et 16h-19h, haute saison 8h-13h et 15h-20h.
Arrivee entre 15h et 19h, depart entre 9h et 11h.
"""
    },
    "kine": {
        "nom": "Cabinet Kine Bien-Etre",
        "secteur": "kinesitherapie",
        "description": "un cabinet de kinesitherapie",
        "infos": """
Prises en charge : reeducation post-operatoire, kinesitherapie du sport, massages therapeutiques.
Horaires : du lundi au vendredi 8h-19h, samedi matin sur rendez-vous.
Consultations uniquement sur rendez-vous, prescription medicale requise.
Prise en charge Securite Sociale et mutuelles.
"""
    },
}

def get_client(client_id):
    return CLIENTS.get(client_id, CLIENTS["default"])
