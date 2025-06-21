# 🥷 ForkBot

**ForkBot** is a lightweight, ninja-fast trade alert system built for options traders who use structured synthetic forks, conviction-based entries, and smart execution logic. It acts as an internal assistant that lets traders post trade alerts to Discord in real-time, using TradingView webhook signals.

---

## ⚙️ How It Works

ForkBot listens for JSON-formatted webhook messages and sends clean, color-coded trade alerts to a Discord channel. It supports multiple trade types — from 0DTE scalps to LEAP swing plays — and aligns with high-conviction fork planning logic.

### ✅ Core Features

- 🔗 **Webhook integration** (TradingView → ForkBot → Discord)
- 📊 **Synthetic Fork Triggers**: Manually input nightly fork levels
- 🔔 **Discord Alerts** with:
  - Symbol, strike, entry
  - Contract count, conviction level
  - Trade status (Open, Closed)
  - Type: 0DTE / Weekly / Swing / LEAP — color-coded
- 🧠 **Supports Strategic Scaling**: Min contract logic for conviction setups
- 📁 **Logs trades** into Excel (WIP phase)

---

## 📦 Tech Stack

- Python (Flask for server)
- Discord Webhooks
- TradingView Alerts
- Ngrok (for local tunnel testing)
- JSON (for webhook payloads)

---

## 🛠️ Setup Instructions

### 1. Clone the repo

```bash
git clone https://github.com/sfaz615/forkbot.git
cd forkbot
