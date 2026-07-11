import streamlit as st
import yfinance as yf
import plotly.graph_objects as go

# إعداد الصفحة
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
    st.title("📈 Evecon Prime v6 Dashboard")
    
    # اختيار العملة والفريم
    col1, col2 = st.columns(2)
    with col1:
        # استخدام قاموس ليكون العرض واضحاً
        assets = {"Gold": "GC=F", "EUR/USD": "EURUSD=X", "GBP/USD": "GBPUSD=X"}
        selected_name = st.selectbox("Select Asset", list(assets.keys()))
        ticker = assets[selected_name]
    with col2:
        interval = st.selectbox("Select Timeframe", ["5m", "15m", "1h", "4h", "1d"])

    # جلب البيانات
    data = yf.download(ticker, period="1d", interval=interval)

    # التحقق من وجود بيانات
    if not data.empty:
        # رسم الشارت
        fig = go.Figure(data=[go.Candlestick(x=data.index,
                        open=data['Open'],
                        high=data['High'],
                        low=data['Low'],
                        close=data['Close'])])
        
        fig.update_layout(title=f"{selected_name} Chart", xaxis_rangeslider_visible=False)
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.warning("جاري جلب البيانات، يرجى الانتظار...")

    if st.button("Logout"):
        st.session_state.logged_in = False
        st.rerun()
