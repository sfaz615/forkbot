# 🥷 ForkBot

**ForkBot** is a lightweight, ninja-fast trade alert system built for options traders using structured synthetic forks, conviction-based entries, and smart execution logic. It acts as an internal assistant that posts trade alerts to Discord in real-time via TradingView webhook signals.

---

## ⚙️ How It Works

ForkBot listens for JSON-formatted webhook messages and sends clean, color-coded trade alerts to a Discord channel. It supports multiple trade types — from 0DTE scalps to LEAP swing plays — and aligns with conviction-based fork logic.


---

## ✅ Core Features

- 🔗 **Webhook Integration**: TradingView → ForkBot → Discord  
- 📊 **Synthetic Fork Triggers**:   Contract minimums scale based on fork strength
- 🔔 **Discord Alerts** with:
  - Symbol & Strike
  - Entry Price
  - Contract Count
  - Conviction Level
  - Trade Status: `Open` / `Closed`
  - Type: `0DTE`, `Weekly`, `Swing`, `LEAP` — *Color-coded*
- 🧠 **Strategic Scaling Support**: Contract minimums scale based on fork strength
- 📁 **Logging Support** (WIP): Trade journaling to Excel for P&L tracking

---

## 📦 Tech Stack

- Python (Flask)
- Discord Webhooks
- TradingView Alerts
- Ngrok (for local tunnel testing)
- JSON (for webhook payloads)

---

## 🛠️ Status

✅ Operational  
🧪 Testing & Logging Ongoing  
🚀 Feature Expansion Planned

---

> Built with focus, conviction, and operator energy.  
> *“We don’t wait for permission — we trigger forks.”*

