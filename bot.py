import streamlit as st

# إعداد الصفحة
st.set_page_config(page_title="Evecon Trade - Login", page_icon="🦅")

# قاعدة بيانات وهمية للأكواد (بعدين نربطها بجدول)
VALID_CODES = ["EVECON2026", "VIP123"]

def main():
    st.title("🦅 Evecon Trade Platform")
    st.subheader("Please enter your access code")

    code = st.text_input("Access Code", type="password")
    
    if st.button("Login"):
        if code in VALID_CODES:
            st.session_state.logged_in = True
            st.success("Welcome back, Youssef!")
            st.rerun()
        else:
            st.error("Invalid Code!")

# منطق الجلسة
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    main()
else:
    st.title("Dashboard")
    st.write("Welcome to your Evecon Prime v6 workspace!")
    if st.button("Logout"):
        st.session_state.logged_in = False
        st.rerun()
