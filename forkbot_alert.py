import requests

webhook_url = "https://discord.com/api/webhooks/your_webhook_here"

payload = {
    "username": "ForkBot 🥷",
    "avatar_url": "https://emojicdn.elk.sh/🥷",
    "embeds": [
        {
            "title": "📉 New ForkBot Trade Alert!",
            "description": "**Symbol:** TSLA\n**Strike:** 310p\n**Entry:** $0.10\n**Contracts:** 4\n**Conviction:** Medium\n**Status:** Open",
            "color": 14177041,
            "footer": {"text": "ForkBot VSC | Synthetic Fork Triggered"}
        }
    ]
}

response = requests.post(webhook_url, json=payload)

if response.status_code == 204:
    print("✅ Alert sent successfully!")
else:
    print(f"❌ Failed: {response.status_code} — {response.text}")

