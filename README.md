# 🥷 ForkBot

**ForkBot** is a lightweight, ninja-fast trade alert system built for options traders using structured synthetic forks, conviction-based entries, and smart execution logic. It acts as an internal assistant that posts trade alerts to Discord in real-time via TradingView webhook signals.

---

## ⚙️ How It Works

ForkBot listens for JSON-formatted webhook messages and sends clean, color-coded trade alerts to a Discord channel. It supports multiple trade types — from 0DTE scalps to LEAP swing plays — and aligns with conviction-based fork logic.

## 📈 Trade Recap Example

Below is a real-world execution using ForkBot's alert logic. Entry was based on rejection at resistance, with conviction-level breakdowns tracked in real-time.

![VSC Trade Recap](charts/vsc_trade_recap_333_breakdown.jpeg)

---

## ✅ Core Features

- 🔗 **Webhook Integration**: TradingView → ForkBot → Discord  
- 📊 **Synthetic Fork Triggers**: Manually input nightly fork levels  
- 🔔 **Discord Alerts** with:
  - Symbol & Strike
  - Entry Price
  - Contract Count
  - Conviction Level
  - Trade Status: `Open` / `Closed`
  - Type: `0DTE`, `Weekly`, `Swing`, `LEAP` — *Color-coded*
- 🧠 **Strategic Scaling Support**: Minimum contract logic based on conviction
- 📁 **Trade Logging to Excel** *(WIP phase)*

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

