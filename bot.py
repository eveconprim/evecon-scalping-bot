import streamlit as st
import yfinance as yf
import plotly.graph_objects as go

st.set_page_config(page_title="Evecon Trade", layout="wide")

# --- منطق الدخول ---
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.title("🦅 Evecon Trade - Login")
    code = st.text_input("Access Code", type="password")
    if st.button("Login"):
        if code == "EVECON2026":
            st.session_state.logged_in = True
            st.rerun()
        else:
            st.error("Invalid Code!")
else:
    # --- الـ Dashboard ---
    st.title("📈 Evecon Trade Dashboard")
    
    # اختيار العملة والفريم
    col1, col2 = st.columns(2)
    with col1:
        ticker = st.selectbox("Select Asset", ["GC=F", "EURUSD=X", "GBPUSD=X"]) # GC=F هو الذهب
    with col2:
        interval = st.selectbox("Select Timeframe", ["1m", "5m", "15m", "1h", "1d"])

    # جلب البيانات
    data = yf.download(ticker, period="1d", interval=interval)

    # رسم الشارت
    fig = go.Figure(data=[go.Candlestick(x=data.index,
                    open=data['Open'],
                    high=data['High'],
                    low=data['Low'],
                    close=data['Close'])])
    
    fig.update_layout(title=f"{ticker} Chart", xaxis_rangeslider_visible=False)
    st.plotly_chart(fig, use_container_width=True)

    if st.button("Logout"):
        st.session_state.logged_in = False
        st.rerun()
