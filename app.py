from flask import Flask, request, jsonify, render_template
from anthropic import Anthropi
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
Ne répète pas les mêmes formules. Va droit au but. Sois concis et utile.

URGENCES :
- SAMU : 15
- Pompiers : 18
- Police : 17
- Numéro européen : 112
- Hôpital de Pamiers : 05 61 60 60 60
- Hôpital de Foix : 05 61 03 30 30

VÉTÉRINAIRES PROCHES :
- Pamiers et Foix (environ 20-30 min) — conseiller d'appeler le 3115 la nuit

RANDONNÉES EN ARIÈGE :
- GR10 : traversée des Pyrénées à pied
- Véloroute des Pyrénées (EV8)
- Sentiers équestres autour du Mas-d'Azil et Mirepoix
- Grotte du Mas-d'Azil (15 min) : site préhistorique majeur

FESTIVALS ET ÉVÉNEMENTS :
- Festival Rio Loco (Toulouse, juin)
- Festival de Mirepoix (été)
- Marché médiéval de Mirepoix
- Fête de l'Ours à Saint-Lary (février)
- Pour le calendrier précis, utilise la recherche web pour trouver les événements actuels

SITES TOURISTIQUES PROCHES :
- Grotte du Mas-d'Azil (15 min)
- Cité médiévale de Mirepoix (20 min)
- Château de Foix (30 min)
- Lac de Montbel (25 min)
- Grottes de Niaux (45 min)

Si on te demande des infos sur les événements actuels ou le calendrier, utilise la recherche web."""
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