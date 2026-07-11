import streamlit as st
import MetaTrader5 as mt5
import pandas as pd
import time

# إعداد واجهة Streamlit
st.set_page_config(page_title="Evecon Trade", layout="wide")
st.title("Premium Scalping System")
st.subheader("High-Frequency Momentum Engine (MT5 Direct Bridge)")

# كود الربط مع MT5
if not mt5.initialize():
    st.error("خطأ: تعذر الاتصال بـ MetaTrader 5. تأكد أن المنصة مفتوحة على جهازك.")
else:
    st.success("تم الربط بنجاح مع MT5")

# تحديث الواجهة
st.write("البوت جاهز للعمل...")
