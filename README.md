# ⚡ E-Commerce Price Sentinel (Open-Core Radar)

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![ThinkConnect IA](https://img.shields.io/badge/Powered%20by-ThinkConnect%20IA-1E293B.svg)](https://thinkconnect.com.ar/radar-precios)

A lightweight, production-grade Python tool to track e-commerce product prices, detect competitor margin discrepancies, and audit Buy Box leakages in real-time.

---

## 🔍 Why This Matters

In competitive retail (Sports Nutrition, Consumer Electronics, Hardware, Cosmetics), **a 5% price difference often means losing 80% of Google Shopping and Marketplace sales (the Buy Box)**. 

Most monitoring solutions are either bloated enterprise tools costing thousands per month or brittle scraping scripts that break on dynamic layouts. **E-Commerce Price Sentinel** provides a robust, modular baseline to track catalog deltas effortlessly.

---

## 🚀 Key Features

- **Multi-Store Tracking**: Compare baseline product prices against direct market rivals.
- **Discrepancy Calculation**: Highlights exact price gaps (EUR / USD) and percentage differences.
- **Alert Thresholds**: Flag products exceeding healthy variance margins (e.g. > 10% discrepancy).
- **Export Formats**: Outputs formatted terminal tables, structured JSON, and CSV audits.
- **Anti-Bot Resilient**: Headers normalization and clean user-agent rotation architecture.

---

## 📦 Quick Start

### 1. Installation

```bash
git clone https://github.com/charliemza/ecommerce-price-sentinel.git
cd ecommerce-price-sentinel
pip install -r requirements.txt
```

### 2. Run a Sample Price Audit

```bash
python -m price_sentinel.main
```

### 3. Output Preview

```text
========================================================================================
E-COMMERCE PRICE SENTINEL AUDIT REPORT - 2026-10-23
Store Target: Your Store vs. Competitors (Nutritienda / Bulevip)
========================================================================================
Product                          Target Price    Competitor      Gap (EUR)    Gap (%)   Status
----------------------------------------------------------------------------------------
Gold Standard Whey 2.27kg        89.99 €         79.90 €         +10.09 €     +11.2%    ⚠️ BUY BOX LOSS
ISO 100 Hydrolyzed 2.2kg         74.99 €         62.99 €         +12.00 €     +19.0%    🚨 CRITICAL
Creatine Monohydrate 750g        53.90 €         35.32 €         +18.58 €     +34.5%    🚨 CRITICAL
100% Whey Professional 2.35kg    76.49 €         71.90 €          +4.59 €      +6.0%    ⚠️ UNBALANCED
Animal Pak 44 Packs              54.90 €         51.95 €          +2.95 €      +5.4%    ⚠️ UNBALANCED
----------------------------------------------------------------------------------------
Average Overpricing Discrepancy: +15.2% | Estimated Weekly Margin Leakage: High
========================================================================================
```

---

## 🛠️ Architecture & Usage

You can define products and competitor targets in `config/targets.json`:

```json
[
  {
    "sku": "ON-WHEY-227",
    "name": "Optimum Nutrition Gold Standard Whey 2.27kg",
    "target_price": 89.99,
    "competitors": [
      { "name": "Nutritienda", "price": 79.90 },
      { "name": "Bulevip", "price": 81.50 }
    ]
  }
]
```

---

## 💼 Enterprise & Production Deployments

Looking for a fully managed, hands-off infrastructure?

**ThinkConnect IA** provides full-scale deployment and managed operations:
- 🔄 **24/7 Automated Scraping & Scheduled Runs** on dedicated servers.
- 📱 **Real-time WhatsApp & Slack Alerts** whenever a competitor alters prices.
- 📑 **Vector PDF Executive Audits** delivered to your inbox weekly.
- 🛡️ **Anti-DDoS / Cloudflare Turnstile Bypass Engine** for high-security storefronts.
- 🔌 **Native Integrations**: Shopify, WooCommerce, PrestaShop, and custom ERPs.

👉 **Learn more and request a tailored pilot:** [https://thinkconnect.com.ar/radar-precios](https://thinkconnect.com.ar/radar-precios)  
📩 **Direct Engineering Contact:** `carlos@thinkconnect.com.ar`

---

## 📄 License

This open-core module is released under the [MIT License](LICENSE).
