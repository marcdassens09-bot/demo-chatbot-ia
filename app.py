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
        system=f"Tu es l'assistant virtuel de {entreprise}. Tu accueilles chaleureusement les clients et réponds à leurs questions sur les services, les tarifs et les horaires. Tu es professionnel, courtois et concis.",
        messages=historique
    )

    texte = reponse.content[0].text

    historique.append({
        "role": "assistant",
        "content": texte
    })

    return jsonify({"reponse": texte, "historique": historique})

port = int(os.environ.get("PORT", 5000))
app.run(host="0.0.0.0", port=port)