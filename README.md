# Nasdaq 100 Stock Dashboard

This project is a **Streamlit-based dashboard** that tracks the **Nasdaq 100 stocks**, using **Yahoo Finance (yfinance)** for price data and **Plotly** for interactive visualizations. It includes **MACD indicators** and provides a categorized stock sentiment analysis.

## Features
- **Live Nasdaq 100 stock data**
- **MACD Indicator & Histogram** for trend analysis
- **Stock sentiment categorization** (Bullish, Bearish, etc.)
- **Interactive charts** for stock prices & MACD
- **Company information** (Sector, Market Cap, P/E Ratio, Dividend Yield)

## Installation

### Prerequisites
Ensure you have Python installed. Install the required dependencies using pip:
```bash
pip install streamlit yfinance pandas plotly requests
```

### Running the App
Run the Streamlit application with:
```bash
streamlit run app.py
```

## How It Works
1. **Fetches** the latest **Nasdaq 100 stock tickers**.
2. **Retrieves** historical stock prices from Yahoo Finance.
3. **Computes** MACD, MACD Signal, and MACD Histogram values.
4. **Classifies** stocks into **Bullish, Bearish, or Neutral** based on MACD trends.
5. **Displays** interactive visualizations for stock prices & MACD indicators.

## Usage
- Select a **market sentiment** category (e.g., Bullish, Bearish )
- Choose a **stock** from the filtered list
- View its **price chart & MACD analysis**
- Get **company details** like sector, market cap, and dividend yield

## Example Screenshot

<img width="892" alt="Screenshot 2568-02-17 at 16 00 54" src="https://github.com/user-attachments/assets/558714e7-e4a6-4fa5-b2b4-945241e2e0a6" />
<img width="906" alt="Screenshot 2568-02-17 at 16 05 08" src="https://github.com/user-attachments/assets/fc6ee0a3-93b5-41dc-ba81-f17e692777a0" />
<img width="442" alt="Screenshot 2568-02-17 at 16 07 07" src="https://github.com/user-attachments/assets/457667a5-e3ec-4079-b2bb-f4a420ad94ef" />

## Author
Developed by donliyen.

---
Enjoy tracking Nasdaq 100 stocks efficiently! 🚀

