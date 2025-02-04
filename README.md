# BinanceAssistant

## Introduction / 介紹

A **Line Bot** integrated with an **LLM** (Large Language Model) and **Binance** APIs. This project helps users fetch real-time market data, place orders, and analyze holdings—all through a conversational interface on Line.

一個結合 **Line Bot**、大型語言模型 (LLM) 和 **Binance** API 的專案。使用者可以透過 Line 介面即時查詢市場資訊、下單交易，以及檢視持倉狀況。

---

### Example Bot Interaction / 機器人對話示例

- **Example 1: Query Real-Time Price** / **查詢即時價格**  
  <img src="./images/example1.jpg" alt="Example 1" width="400"/>

- **Example 2: Place an Order** / **下單交易**  
  <img src="./images/example2.jpg" alt="Example 2" width="400"/>

- **Example 3: Check Portfolio Holdings** / **查詢持倉**  
  <img src="./images/example3.jpg" alt="Example 3" width="400"/>
  
---

## Features / 功能特色

1. **Real-Time Price Checks**  **即時價格查詢**
   - Query current market price for any supported trading pair (e.g. BTCUSDT).
   - 查詢任何交易對的現行價格（如 BTCUSDT）。

2. **Order Placement**  **下單交易**
   - Place buy/sell orders on Binance using natural language (supports Spot Testnet).
   - 透過自然語言指令在 Binance 下單（支援測試網）。

3. **Portfolio Holdings**  **持倉查詢**
   - View account balances and holdings via simple text commands.
   - 快速查看帳戶各種幣種的餘額與持倉狀態。

4. **LLM-Driven Dialogues**  **LLM 對話**
   - Uses OpenAI’s function-calling to interpret user intents and route requests to Binance.
   - 利用 OpenAI 的 Function Calling 自動判斷使用者需求，呼叫對應的 Binance API。
   
---

## Project Structure / 專案架構

```plaintext
BinanceAssistant/
├── README.md
├── .env                      # API keys and credentials
├── requirements.txt          # Python dependencies
└── src/
    ├── main.py               # Flask entry point for Line webhook
    ├── bot/
    │   └── line_bot.py       # Handles incoming messages and calls LLM logic
    ├── services/
    │   ├── llm_service.py    # Defines function schemas and interacts with OpenAI
    │   ├── binance_service.py# Interfaces with Binance API
    │   └── ...
    └── utils/
        └── config.py         # Loads environment variables
```

---

## Installation / 安裝

1. **Clone the repository**  **複製專案** 
     ```bash
     git clone https://github.com/yourusername/BinanceAssistant.git
     cd BinanceAssistant
     ```

2. **Create and activate a virtual environment**  **建立並啟用虛擬環境**
     ```bash
     python -m venv .venv
     source .venv/bin/activate  # Mac/Linux
     .\.venv\Scripts\activate   # Windows
     ```

3. **Install dependencies**  **安裝套件**
     ```bash
     pip install -r requirements.txt
     ```

4. **Set up environment variables** in `.env`  **設定 `.env` 檔案**  
     ```bash
     LINE_CHANNEL_SECRET=YOUR_LINE_CHANNEL_SECRET
     LINE_CHANNEL_ACCESS_TOKEN=YOUR_LINE_CHANNEL_ACCESS_TOKEN
     BINANCE_API_KEY=YOUR_BINANCE_API_KEY
     BINANCE_API_SECRET=YOUR_BINANCE_API_SECRET
     OPENAI_API_KEY=YOUR_OPENAI_API_KEY
     ```

---

## License / 授權
 
  This project does not provide an open-source license. All rights reserved.  
  Please contact the owner for permission if you intend to use or modify this code.

  本專案目前未提供公開授權條款，保留一切權利。  
  如需使用或修改本專案程式碼，請先聯繫專案擁有者取得許可。
