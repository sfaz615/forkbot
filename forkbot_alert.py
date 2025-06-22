import requests

webhook_url = 'https://discord.com/api/webhooks/1385692833964359873/XKZyY5avJhSlfse_VDz1lSoRJ5Ym2u2FnjF15A1qjx0OAGOKEHpz9XzcCI1SB6FKO6J7'

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

