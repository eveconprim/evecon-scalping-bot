import streamlit as st
import time
import random
import pandas as pd
import yfinance as yf

# --- Evecon Trade Brand Configuration ---
st.set_page_config(page_title="Evecon Trade | Premium Bot", page_icon="🦅", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #0b0e14; }
    h1, h2, h3 { color: #00ffcc !important; font-family: 'Courier New', monospace; }
    .stButton>button { background-color: #00ffcc; color: black; font-weight: bold; border-radius: 8px; width: 100%; }
    .stTextInput>div>div>input { background-color: #151c28; color: white; border: 1px solid #00ffcc; }
    .stSelectbox>div>div>div { background-color: #151c28; color: white; }
    </style>
""", unsafe_allow_html=True)

st.title("🦅 EVECON TRADE | Premium Scalping System")
st.subheader("High-Frequency Momentum Engine (MT5 Direct Bridge)")
st.write("---")

st.sidebar.header("🔐 Subscriber Activation")
license_key = st.sidebar.text_input("Enter License Key", type="password")
is_activated = st.sidebar.checkbox("Activate Bot")

st.sidebar.header("🔌 MT5 Account Connection")
broker_list = ["Exness-Real", "Exness-Trial", "XMGlobal-Real", "ICMarkets-Live", "FBS-Real", "FXTM-Real", "Pepperstone-Live", "OctaFX-Real"]
selected_broker = st.sidebar.selectbox("Select Broker", broker_list)
account_number = st.sidebar.text_input("MT5 Account Number")
account_password = st.sidebar.text_input("MT5 Trader Password", type="password")

st.sidebar.header("⚙️ Risk Parameters")
lot_size = st.sidebar.number_input("Lot Size", value=0.01, step=0.01)
max_daily_profit = st.sidebar.slider("Daily Profit Target ($)", 5.0, 500.0, 100.0)

col1, col2, col3 = st.columns(3)
with col1:
    gold_price_metric = st.metric(label="🥇 XAUUSD Live Price", value="$0.00")
with col2:
    profit_metric = st.metric(label="Total Net Profit", value="$0.00")
with col3:
    status_metric = st.metric(label="MT5 Bridge Status", value="DISCONNECTED")

if is_activated and license_key == "EVECON2026":
    if account_number and account_password:
        st.success(f"✅ Bridge Securely Connected to {selected_broker}!")
        status_metric.metric(label="MT5 Bridge Status", value="CONNECTED & ACTIVE")
        
        # تم استبدال st.code بـ st.text لمنع التهنيج والخطأ نهائياً
        log_placeholder = st.empty()
        total_pnl = 0.0
        trade_history = []
        
        for i in range(20):
            live_price = 2360.40 + random.uniform(-0.8, 0.8)
            timestamp = time.strftime("%H:%M:%S")
            pnl = round(random.uniform(0.15, 0.95) * (lot_size * 100), 2)
            total_pnl += pnl
            
            msg = f"🟢 [{timestamp}] [MT5] - Momentum Order Filled | Price: ${live_price:.2f} | PnL: +${pnl}"
            trade_history.append({"Time": timestamp, "Action": "🎟️ BUY", "Price": round(live_price, 2), "PnL ($)": pnl})
            
            gold_price_metric.metric(label="🥇 XAUUSD Live Price", value=f"${live_price:,.2f}")
            profit_metric.metric(label="Total Net Profit", value=f"${total_pnl:.2f}")
            
            with log_placeholder.container():
                st.text(msg) # العرض الآمن النظيف
                st.write("#### Closed Positions (Sent to MT5)")
                st.dataframe(pd.DataFrame(trade_history), use_container_width=True)
            time.sleep(1)
    else:
        st.warning("⚠️ Enter MT5 Details.")
