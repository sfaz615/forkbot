from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

DISCORD_WEBHOOK_URL = "https://discord.com/api/webhooks/your_webhook_here"

TYPE_COLORS = {
    "0DTE": 0xFF5733,
    "Weekly": 0x3498DB,
    "Put": 0x8E44AD,
    "LEAP": 0x2ECC71,
    "Default": 0x95A5A6
}

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()

    symbol = data.get("symbol", "TSLA")
    strike = data.get("strike", "")
    entry = data.get("entry", "")
    contracts = data.get("contracts", "")
    conviction = data.get("conviction", "")
    status = data.get("status", "Open")
    trade_type = data.get("type", "Default")

    color = TYPE_COLORS.get(trade_type, TYPE_COLORS["Default"])

    payload = {
        "embeds": [
            {
                "title": "🥷 Synthetic Fork Triggered",
                "description": f"**{symbol} {strike}**\nEntry: `{entry}` | Contracts: `{contracts}`\nConviction: **{conviction}** | Status: `{status}`",
                "color": color,
                "footer": {
                    "text": f"Trade Type: {trade_type}"
                }
            }
        ]
    }

    response = requests.post(DISCORD_WEBHOOK_URL, json=payload)
    return jsonify({"message": "Alert sent", "status_code": response.status_code})

if __name__ == '__main__':
    app.run(debug=True)
