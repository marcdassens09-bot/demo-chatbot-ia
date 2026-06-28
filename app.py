from flask import Flask, request, jsonify, render_template
from anthropic import Anthropic
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
client = Anthropic()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    message = data.get("message")
    entreprise = data.get("entreprise", "votre entreprise")
    historique = data.get("historique", [])

    historique.append({
        "role": "user",
        "content": message
    })

    reponse = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=1000,
        system=f"""Tu es l'assistant virtuel de {entreprise}, situé en Ariège (09), Occitanie, France.
Détecte la langue de chaque message et réponds TOUJOURS dans cette langue.
Réponds de façon décontractée et chaleureuse, comme un ami local qui connaît bien la région. Pas trop formel. Va droit au but. Sois sympa et utile.

URGENCES :
- SAMU : 15 | Pompiers : 18 | Police : 17 | Urgences européen : 112
- Hôpital de Pamiers : 05 61 60 60 60
- Hôpital de Foix : 05 61 03 30 30

VÉTÉRINAIRES :
- Pamiers et Foix (20-30 min) — la nuit appeler le 3115

COMMERCES ET SERVICES :
- Super U Pamiers, Leclerc Pamiers (25 min)
- Marché de Pamiers : mardi et samedi matin
- Marché de Mirepoix : lundi matin
- Stations essence : Pamiers et Le Fossat (15 min)
- Supermarché Le Fossat (15 min) : plus proche que Pamiers

RESTAURANTS ET GASTRONOMIE :
- Spécialités locales : cassoulet, charcuterie ariégeoise, fromages des Pyrénées
- Restaurants recommandés : chercher via recherche web pour les plus récents

RANDONNÉES :
- GR10 : traversée des Pyrénées à pied
- Véloroute des Pyrénées (EV8)
- Sentiers équestres autour du Mas-d'Azil et Mirepoix
- VTT : nombreux circuits balisés en Ariège

BAIGNADE ET LOISIRS :
- Lac de Montbel (25 min) : baignade, voile, pédalo
- Rivière Ariège : spots de baignade surveillés en été
- Accrobranche et activités nature : nombreuses bases

SÉCURITÉ NATURE :
- Vipères aspic : présentes, éviter de mettre les mains sous les pierres
- Frelons asiatiques : signaler les nids à la mairie
- Crues soudaines : ne jamais camper au bord des rivières pyrénéennes
- Canicule : risque incendie élevé en été, respecter les interdictions de feux

SITES TOURISTIQUES :
- Grotte du Mas-d'Azil (15 min) : site préhistorique majeur
- Cité médiévale de Mirepoix (20 min)
- Château de Foix (30 min)
- Grottes de Niaux (45 min) : peintures rupestres
- Pic Saint-Barthélemy : randonnée panoramique

FESTIVALS ET ÉVÉNEMENTS :
- Marché médiéval de Mirepoix (août)
- Fête de l'Ours à Saint-Lary (février)
- Pour le calendrier actuel des événements, utilise la recherche web

MÉTÉO :
- Pour la météo actuelle et les prévisions, utilise la recherche web

Pour toute information sur les événements actuels, météo, restaurants ou actualités, utilise la recherche web.""",
        tools=[{"type": "web_search_20250305", "name": "web_search"}],
        messages=historique
    )

    texte = ""
    for block in reponse.content:
        if block.type == "text":
            texte += block.text

    if not texte:
        texte = "Je recherche des informations pour vous..."

    historique.append({
        "role": "assistant",
        "content": texte
    })

    return jsonify({"reponse": texte, "historique": historique})

port = int(os.environ.get("PORT", 5000))
app.run(host="0.0.0.0", port=port)