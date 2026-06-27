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

    # Premier appel avec recherche web
    reponse = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=1000,
        system=f"Tu es l'assistant virtuel de {entreprise}. Tu réponds aux questions des clients. Si on te demande des actualités ou informations récentes sur un secteur, utilise la recherche web. Tu es professionnel et concis.",
        tools=[{"type": "web_search_20250305", "name": "web_search"}],
        messages=historique
    )

    # Extraire uniquement le texte
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
