(function () {
  // === MP Solutions IA - Widget Chatbot ===
  const scriptTag = document.currentScript;
  const clientId = scriptTag.getAttribute("data-client") || "default";
  const apiBase = scriptTag.src.replace("/static/widget.js", "");

  const style = document.createElement("style");
  style.textContent = `
    #mpia-bubble {
      position: fixed; bottom: 20px; right: 20px; width: 60px; height: 60px;
      border-radius: 50%; background: linear-gradient(135deg, #0066cc, #00aaff);
      display: flex; align-items: center; justify-content: center;
      cursor: pointer; box-shadow: 0 4px 15px rgba(0,0,0,0.3); z-index: 999999;
      font-size: 28px; transition: transform 0.2s;
    }
    #mpia-bubble:hover { transform: scale(1.08); }
    #mpia-window {
      position: fixed; bottom: 95px; right: 20px; width: 340px; max-width: 90vw;
      height: 460px; max-height: 70vh; background: #fff; border-radius: 16px;
      box-shadow: 0 10px 40px rgba(0,0,0,0.25); display: none; flex-direction: column;
      overflow: hidden; z-index: 999999; font-family: 'Segoe UI', sans-serif;
    }
    #mpia-header {
      background: linear-gradient(135deg, #0066cc, #00aaff); color: #fff;
      padding: 14px 16px; font-weight: 600; display: flex; justify-content: space-between; align-items: center;
    }
    #mpia-close { cursor: pointer; font-size: 18px; }
    #mpia-messages { flex: 1; overflow-y: auto; padding: 12px; background: #f5f7fa; }
    .mpia-msg { margin-bottom: 10px; padding: 8px 12px; border-radius: 12px; max-width: 80%; font-size: 14px; line-height: 1.4; }
    .mpia-msg.user { background: #0066cc; color: #fff; margin-left: auto; }
    .mpia-msg.bot { background: #e8eaf0; color: #222; }
    #mpia-inputzone { display: flex; border-top: 1px solid #e0e0e0; padding: 8px; }
    #mpia-input { flex: 1; border: none; outline: none; padding: 8px; font-size: 14px; }
    #mpia-send { background: #0066cc; color: #fff; border: none; border-radius: 8px; padding: 8px 14px; cursor: pointer; margin-left: 6px; }
  `;
  document.head.appendChild(style);

  const bubble = document.createElement("div");
  bubble.id = "mpia-bubble";
  bubble.innerHTML = "💬";
  document.body.appendChild(bubble);

  const win = document.createElement("div");
  win.id = "mpia-window";
  win.innerHTML = `
    <div id="mpia-header">
      <span>Assistant IA</span>
      <span id="mpia-close">✕</span>
    </div>
    <div id="mpia-messages"></div>
    <div id="mpia-inputzone">
      <input id="mpia-input" type="text" placeholder="Écrivez votre message..." />
      <button id="mpia-send">Envoyer</button>
    </div>
  `;
  document.body.appendChild(win);

  const messagesEl = win.querySelector("#mpia-messages");
  const inputEl = win.querySelector("#mpia-input");
  let historique = [];

  function escapeHtml(str) {
    const div = document.createElement("div");
    div.textContent = str;
    return div.innerHTML;
  }

  function addMessage(text, sender) {
    const msg = document.createElement("div");
    msg.className = "mpia-msg " + sender;
    let safe = escapeHtml(text);
    safe = safe.replace(/\*\*(.+?)\*\*/g, "<strong>$1</strong>");
    msg.innerHTML = safe;
    messagesEl.appendChild(msg);
    messagesEl.scrollTop = messagesEl.scrollHeight;
  }

  addMessage("Bonjour 👋 Comment puis-je vous aider ?", "bot");

  bubble.addEventListener("click", () => {
    win.style.display = win.style.display === "flex" ? "none" : "flex";
  });
  win.querySelector("#mpia-close").addEventListener("click", () => {
    win.style.display = "none";
  });

  async function sendMessage() {
    const text = inputEl.value.trim();
    if (!text) return;
    addMessage(text, "user");
    inputEl.value = "";

    try {
      const res = await fetch(apiBase + "/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          message: text,
          entreprise: clientId,
          historique: historique,
        }),
      });
      const data = await res.json();
      historique = data.historique || historique;
      addMessage(data.reponse || "Désolé, je n'ai pas de réponse pour le moment.", "bot");
    } catch (err) {
      addMessage("Erreur de connexion, réessayez dans un instant.", "bot");
    }
  }

  win.querySelector("#mpia-send").addEventListener("click", sendMessage);
  inputEl.addEventListener("keypress", (e) => {
    if (e.key === "Enter") sendMessage();
  });
})();
