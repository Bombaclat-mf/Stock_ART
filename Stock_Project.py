import streamlit as st
import plotly.express as pe,yfinance as yf
import datetime as dt
date=dt.datetime.today()
ys = date - dt.timedelta(days=7)
Food="f"
st.title("BOMBACLAT Stock Tracker")
ticker_symbol = st.text_input("Ticker",Food)
start_date = st.date_input("Start Date",ys)
end_date = st.date_input("End Date",)
stockData = yf.download(ticker_symbol,start=start_date,end=end_date)
ticker = yf.Ticker(ticker_symbol)
historical_data = ticker.history(start=start_date,end=end_date)
if start_date is not None and end_date is not None:
    History,Grahp = st.tabs(['History Overview','Grahp',])
    close_data = stockData["Close"].squeeze() 
    with History:
        st.write("History Overview")
        st.write(historical_data)
    with Grahp:
        st.write("Grahp")
        line_charts= pe.line(stockData,x= stockData.index,y=close_data,title=ticker_symbol)
        line_charts.update_layout(
    yaxis=dict(
        tickprefix="",
        ticksuffix="$"))
        st.plotly_chart(line_charts)