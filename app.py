import streamlit as st
import random
import time

# --- إعدادات متقدمة للواجهة ---
st.set_page_config(page_title="WePlay Ultimate", page_icon="👑", layout="wide")

# ستايل CSS احترافي بألوان النيون (Neon UI)
st.markdown("""
    <style>
    .stApp { background: #0b0e14; color: #e0e0e0; }
    .vip-card { background: linear-gradient(135deg, #ffd700 0%, #b8860b 100%); padding: 10px; border-radius: 10px; color: black; font-weight: bold; text-align: center; }
    .game-card { background: #1a1c24; border: 2px solid #333; padding: 20px; border-radius: 20px; box-shadow: 0 10px 20px rgba(0,0,0,0.5); }
    .stButton>button { background: linear-gradient(90deg, #00d2ff, #3a7bd5); border: none; color: white; border-radius: 30px; transition: 0.3s; }
    .stButton>button:hover { transform: scale(1.05); box-shadow: 0 0 15px #00d2ff; }
    </style>
    """, unsafe_allow_html=True)

# --- إدارة الحالة (Data State) ---
if 'points' not in st.session_state: st.session_state.points = 0
if 'level' not in st.session_state: st.session_state.level = 1

# --- القائمة الجانبية (بروفايل اللاعب) ---
with st.sidebar:
    st.markdown("<div class='vip-card'>🌟 VIP PLAYER</div>", unsafe_allow_html=True)
    st.image(f"https://api.dicebear.com/7.x/avataaars/svg?seed={st.session_state.get('my_name', 'Guest')}", width=100)
    st.subheader(f"الاسم: {st.session_state.get('my_name', 'زائر')}")
    st.write(f"🏆 النقاط: {st.session_state.points}")
    st.write(f"🆙 المستوى: {st.session_state.level}")
    st.progress(min(st.session_state.points % 100 / 100, 1.0))

# --- المحتوى الرئيسي ---
if 'my_name' not in st.session_state:
    st.title("🛡️ WePlay Ultimate")
    name = st.text_input("ادخل اسمك الأسطوري:")
    if st.button("دخول العالم 🌍"):
        if name:
            st.session_state.my_name = name
            st.rerun()
else:
    tab1, tab2, tab3 = st.tabs(["🎮 الألعاب", "🎨 لوحة الرسم", "🎁 المتجر والهدايا"])

    # --- تبويب الألعاب ---
    with tab1:
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("<div class='game-card'>", unsafe_allow_html=True)
            st.subheader("🕵️ WeParty")
            if st.button("كشف دوري السري"):
                role = random.choice(["القاتل المرعب 🔪", "المحقق الذكي 🔍", "مواطن مسالم 😇"])
                st.toast(f"تم تحديد دورك: {role}")
                st.success(f"أنت الآن: {role}")
            st.markdown("</div>", unsafe_allow_html=True)

        with col2:
            st.markdown("<div class='game-card'>", unsafe_allow_html=True)
            st.subheader("🎲 حجر الحظ")
            if st.button("ارمي الحجر"):
                num = random.randint(1, 6)
                st.write(f"الرقم هو: {num}")
                if num == 6:
                    st.session_state.points += 20
                    st.balloons()
                    st.success("مبروك! حصلت على 20 نقطة مكافأة!")
            st.markdown("</div>", unsafe_allow_html=True)

    # --- تبويب الرسم (تفاعلي) ---
    with tab2:
        st.subheader("🖍️ مساحة الإبداع (ارسم وتوقع)")
        st.info("هذه المساحة مخصصة لمشاركة الرسومات مع أصدقائك في الغرفة")
        color = st.sidebar.color_picker("لون القلم", "#00d2ff")
        st.write("استخدم أدوات المتصفح للرسم ومشاركة الشاشة مع أصدقائك!")
        # ملاحظة: يمكن إضافة مكتبة streamlit-drawable-canvas هنا لاحقاً

    # --- تبويب الهدايا (VIP) ---
    with tab3:
        st.subheader("💎 متجر الهدايا الخاصة")
        g1, g2, g3 = st.columns(3)
        with g1:
            if st.button("💍 خاتم ملكي"): st.snow()
        with g2:
            if st.button("👑 تاج ذهبي"): st.balloons()
        with g3:
            if st.button("🚀 صاروخ شهرة"): st.toast("لقد لفت انتباه الجميع!")

# --- تحديث النقاط تلقائياً ---
if st.session_state.points >= st.session_state.level * 100:
    st.session_state.level += 1
    st.sidebar.confetti()
            
