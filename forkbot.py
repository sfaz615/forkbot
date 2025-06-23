from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

DISCORD_WEBHOOK_URL = "https://discord.com/api/webhooks/your_webhook_here" 
COLOR_MAP = {
    "0DTE": 0xFF5733,     # Orange
    "Weekly": 0x3498DB,   # Blue
    "LEAP": 0x2ECC71,     # Green
    "Other": 0x9B59B6     # Purple
}

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()

    if not data:
        return jsonify({"error": "Invalid JSON"}), 400

    # Extract trade info
    symbol = data.get("symbol", "TSLA")
    strike = data.get("strike", "???")
    entry = data.get("entry", "N/A")
    contracts = data.get("contracts", 1)
    conviction = data.get("conviction", "Moderate")
    status = data.get("status", "Open")
    trade_type = data.get("type", "Other")

    color = COLOR_MAP.get(trade_type, COLOR_MAP["Other"])

    embed = {
        "title": f"🌀 Synthetic Fork Triggered — {symbol}",
        "color": color,
        "fields": [
            {"name": "Strike", "value": strike, "inline": True},
            {"name": "Entry", "value": f"${entry}", "inline": True},
            {"name": "Contracts", "value": str(contracts), "inline": True},
            {"name": "Conviction", "value": conviction, "inline": True},
            {"name": "Status", "value": status, "inline": True},
            {"name": "Type", "value": trade_type, "inline": True}
        ],
        "footer": {
            "text": "ForkBot v1 • ⚔️ Adaptive Trade Logic"
        }
    }

    payload = {
        "embeds": [embed],
        "username": "ForkBot 🥷",
        "avatar_url": "https://raw.githubusercontent.com/sfaz615/forkbot/main/assets/forkbot_icon.png"  # Optional if hosted
    }

    try:
        response = requests.post(DISCORD_WEBHOOK_URL, json=payload)
        response.raise_for_status()
        return jsonify({"message": "Alert sent successfully!"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(port=5000)
