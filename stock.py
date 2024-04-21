import streamlit as st
import yfinance as yf
import datetime

#create a header
st.header("Stock App Analysis")

stock= 'amzn'
data = yf.Ticker(stock)
hist=data.history(period='1d',start="2024-01-01", end="2024-01-31")

option = st.selectbox('Name of the stock?', ("GOOG","AMZN"))
st.write ('You Selected: ',option)

start_date= st.date_input("Select Date", datetime.date(2017,7,6))
st.write(start_date)



# Tuple Unpacking
col1, col2, col3 = st.columns(3)

with col1:
    # Extract Stock Name
    stock = st.selectbox(
        'Name of the Stock?',
        ('GOOG', 'AAPL', 'MSFT', 'AMZN')
    )

with col2:
    # Input the start date
    start_date = st.date_input("Start Date", datetime.date(2024, 1, 1))

with col3:
    # Input the start date
    end_date = st.date_input("End Date", datetime.date(2024, 1, 31))

# Printing Stock Name
st.write('You selected:', stock)

# Yfinance Data Extraction
data = yf.Ticker(stock)
hist = data.history(period='1d', start=start_date, end=end_date)
st.write(hist)

# Display Charts
st.line_chart(hist)




