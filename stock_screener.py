import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.express as px

def get_nasdaq100_tickers():

    import requests
    headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"}
    res=requests.get("https://api.nasdaq.com/api/quote/list-type/nasdaq100",headers=headers)
    main_data=res.json()['data']['data']['rows']

    tickers = []
    for i in range(len(main_data)):
        tickers.append(main_data[i]['symbol'])
    
    return tickers

def fetch_data(tickers):
    data = {}
    for ticker in tickers:
        stock = yf.Ticker(ticker)
        hist = stock.history(period='3mo')
        hist['MACD'] = hist['Close'].ewm(span=12, adjust=False).mean() - hist['Close'].ewm(span=26, adjust=False).mean()
        hist['MACD_signal'] = hist['MACD'].ewm(span=9, adjust=False).mean()
        hist['MACDH'] = hist['MACD'] - hist['MACD_signal']
        data[ticker] = hist
    return data

def determine_status(macd, macdh):
    if macd > 0 and macdh > 0:
        return 'Highly Bullish'
    elif macd > 0 and macdh < 0:
        return 'Bullish'
    elif macd < 0 and macdh < 0:
        return 'Highly Bearish'
    elif macd < 0 and macdh > 0:
        return 'Bearish'
    return 'Neutral'

def get_stock_info(ticker):
    stock = yf.Ticker(ticker)
    info = stock.info
    return {
        'Company Name': info.get('longName', 'N/A'),
        'Sector': info.get('sector', 'N/A'),
        'Industry': info.get('industry', 'N/A'),
        'Market Cap': info.get('marketCap', 'N/A'),
        'PE Ratio': info.get('trailingPE', 'N/A'),
        'Dividend Yield': info.get('dividendYield', 'N/A')
    }

def main():
    st.title('Nasdaq 100 Stock Stock Dashboard')
    
    tickers = get_nasdaq100_tickers()
    data = fetch_data(tickers)
    
    stock_status = {}
    for ticker, df in data.items():
        latest_macd = df['MACD'].iloc[-1]
        latest_macdh = df['MACDH'].iloc[-1]
        stock_status[ticker] = determine_status(latest_macd, latest_macdh)
    
    status_options = list(set(stock_status.values()))
    selected_status = st.selectbox('Select a status:', status_options)
    
    filtered_tickers = [ticker for ticker, status in stock_status.items() if status == selected_status]
    selected_stock = st.selectbox('Select a stock:', filtered_tickers)
    
    if selected_stock in data:
        df = data[selected_stock]
        
        # Price Chart
        fig = px.line(df, x=df.index, y='Close', title=f'{selected_stock} Closing Price')
        st.plotly_chart(fig)
        
        # MACD Chart with Conditional Color for MACDH
        colors = ['green' if value > 0 else 'red' for value in df['MACDH']]
        
        fig_macd = px.line(df, x=df.index, y=['MACD'], title=f'{selected_stock} MACD Indicators')
        fig_macd.add_bar(x=df.index, y=df['MACDH'], name='MACDH', marker=dict(color=colors, opacity=0.5))

        st.plotly_chart(fig_macd)
        
        st.write(f'**Status:** {stock_status[selected_stock]}')
        st.write(f'**Latest MACD:** {round(df["MACD"].iloc[-1],2)}')
        st.write(f'**Latest MACDH:** {round(df["MACDH"].iloc[-1],2)}')
        
        # Fetch Stock Information
        stock_info = get_stock_info(selected_stock)
        st.subheader(f"Stock Information for {selected_stock}")
        st.write(f"**Company Name:** {stock_info['Company Name']}")
        st.write(f"**Sector:** {stock_info['Sector']}")
        st.write(f"**Industry:** {stock_info['Industry']}")
        st.write(f"**Market Cap:** {stock_info['Market Cap']:,}")
        st.write(f"**P/E Ratio:** {stock_info['PE Ratio']}")
        st.write(f"**Dividend Yield:** {stock_info['Dividend Yield']}")

if __name__ == '__main__':
    main()
