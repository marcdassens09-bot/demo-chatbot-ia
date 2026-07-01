from flask import Flask, request, jsonify, render_template, send_from_directory
from anthropic import Anthropic
from dotenv import load_dotenv
import os
import smtplib
from email.mime.text import MIMEText

load_dotenv()

app = Flask(__name__)
client = Anthropic()

GMAIL_USER = "mpsolutionsia@gmail.com"
GMAIL_PASSWORD = os.environ.get("GMAIL_PASSWORD")

def envoyer_notification(nom, email, entreprise):
    print(f"Tentative envoi email pour {nom} - {email} - {entreprise}")
    try:
        msg = MIMEText(f"""
Nouveau prospect sur la demo !

Nom : {nom}
Email : {email}
Entreprise : {entreprise}

Contacte-le rapidement !
        """)
        msg['Subject'] = f"Nouveau prospect : {entreprise}"
        msg['From'] = GMAIL_USER
        msg['To'] = "marcdassens09@gmail.com"
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(GMAIL_USER, GMAIL_PASSWORD)
            server.send_message(msg)
        print("Email envoye avec succes !")
    except Exception as e:
        print(f"Erreur email : {e}")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/test-widget.html")
def test_widget():
    return send_from_directory("templates/static", "test-widget.html")
@app.route("/static/widget.js")
def serve_widget():
    return send_from_directory("templates/static", "widget.js")
@app.route("/prospect", methods=["POST"])
def prospect():
    data = request.json
    nom = data.get("nom", "")
    email = data.get("email", "")
    entreprise = data.get("entreprise", "")
    envoyer_notification(nom, email, entreprise)
    return jsonify({"status": "ok"})

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
        system=f"""Tu es un assistant virtuel professionnel et chaleureux pour {entreprise}.

LANGUE : Detecte automatiquement la langue du client et reponds TOUJOURS dans cette langue.

COMPORTEMENT :
- Reponds de facon naturelle et decontractee
- Ne repete jamais les memes formules
- Ne dis jamais super question ou tout autre compliment
- Va droit au but, sois concis et utile

VENTE INTELLIGENTE :
- Apres 3-4 echanges, propose : Je peux vous mettre en contact avec notre equipe si vous souhaitez en savoir plus !

URGENCES Ariege 09 :
- SAMU : 15 | Pompiers : 18 | Police : 17 | Urgences : 112
- Hopital Pamiers : 05 61 60 60 60
- Hopital Foix : 05 61 03 30 30

COMMERCES PROCHES :
- Super U et Leclerc Pamiers (25 min)
- Supermarche Le Fossat (15 min)

RANDONNEES :
- GR10 traversee Pyrenees a pied
- Veloroute des Pyrenees EV8
- Sentiers equestres et VTT

SITES TOURISTIQUES :
- Grotte du Mas-d-Azil (15 min)
- Cite medievale de Mirepoix (20 min)
- Chateau de Foix (30 min)
- Lac de Montbel (25 min) : baignade

Pour toute information sur les evenements actuels, meteo ou actualites, utilise la recherche web.""",
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