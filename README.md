# Unified AI Observability Dashboard - InnovGenius

## Overview
This prototype provides a unified observability dashboard for monitoring both ML and LLM systems in banking. It integrates risk scoring, bias detection, hallucination monitoring, and compliance reporting.

## Features
- Login screen for enterprise-style access
- ML Observability: Accuracy, Precision, Recall, F1, bias detection by group
- LLM Observability: Latency, token usage, hallucination detection, cost tracking
- Governance: Compliance report generator, audit transparency
- Risk Engine: Real-time AI risk score with gauge visualization
- Live Risk Streaming: Dynamic chart showing risk fluctuations
- 🛡 Enterprise UI: Sidebar branding, alerts, system health indicators

## How to Run
1. Install requirements:
2. Run the app:
3. Open browser at `localhost:8501`.

## Demo Data
- `ml_data.csv` → contains columns `actual`, `predicted`, and optional `group` for bias detection.
- `llm_logs.csv` → contains columns `response`, `latency`, `tokens`.

## Team
**Team EEGineers** — InnovGenius Hackathon Prototype