import streamlit as st

# 1. إعدادات الصفحة الكلية
st.set_page_config(page_title="أصول VIP | للاستثمار الرقمي", page_icon="👑", layout="centered")

# 2. كود التصميم الفاخر (CSS Injections)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@400;500;700;900&display=swap');
    
    /* تغيير الخط العام لكل التطبيق */
    * { font-family: 'Tajawal', sans-serif !important; }
    
    /* لون الخلفية الأساسي */
    .stApp { background-color: #FAFAFA; }
    
    /* إخفاء القوائم العلوية والسفلية الافتراضية لستريم ليت لتبدو كمنصة خاصة */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* تصميم البطاقات المالية الفخمة */
    .premium-card {
        background: #FFFFFF;
        border-radius: 16px;
        padding: 20px;
        text-align: center;
        border: 1px solid #F1F5F9;
        border-top: 4px solid #D4AF37; /* لمسة ذهبية ملكية من الأعلى */
        box-shadow: 0 10px 30px -10px rgba(0, 0, 0, 0.08);
        transition: all 0.3s ease;
        margin-bottom: 15px;
    }
    .premium-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 35px -10px rgba(212, 175, 55, 0.25);
    }
    .premium-title {
        color: #64748B;
        font-size: 13px;
        font-weight: 700;
        margin-bottom: 5px;
        letter-spacing: 0.5px;
    }
    .premium-value {
        color: #0F172A;
        font-size: 26px;
        font-weight: 900;
    }
    
    /* تصميم محفظة المستخدم (بستايل البطاقة البنكية السوداء) */
    .wallet-box {
        background: linear-gradient(135deg, #0F172A 0%, #1E293B 100%);
        border-radius: 16px;
        padding: 25px;
        margin: 15px 0 35px 0;
        box-shadow: 0 15px 30px -10px rgba(15, 23, 42, 0.4);
        border: 1px solid #334155;
        position: relative;
        overflow: hidden;
    }
    /* تأثير العلامة المائية داخل المحفظة */
    .wallet-box::after {
        content: "👑";
        position: absolute;
        left: -10px;
        top: -10px;
        font-size: 100px;
        opacity: 0.03;
        transform: rotate(-15deg);
    }
    .wallet-flex {
        display: flex;
        justify-content: space-between;
        align-items: center;
        position: relative;
        z-index: 1;
    }
    
    /* التبويبات (Tabs) الفاخرة */
    .stTabs [data-baseweb="tab"] { font-size: 16px; font-weight: 700; color: #94A3B8; }
    .stTabs [data-baseweb="tab"][aria-selected="true"] { color: #D4AF37 !important; border-bottom-color: #D4AF37 !important; }
    
    /* الأزرار الملكية */
    div[data-testid="stButton"] > button {
        background: linear-gradient(135deg, #D4AF37 0%, #AA8C2C 100%) !important;
        color: #FFFFFF !important;
        border: none !important;
        border-radius: 12px !important;
        font-weight: 800 !important;
        font-size: 16px !important;
        padding: 12px !important;
        box-shadow: 0 4px 15px rgba(212, 175, 55, 0.3) !important;
        transition: all 0.3s !important;
    }
    div[data-testid="stButton"] > button:hover {
        transform: scale(1.03) !important;
        box-shadow: 0 8px 25px rgba(212, 175, 55, 0.5) !important;
    }
    </style>
""", unsafe_allow_html=True)

# 3. العناوين الرئيسية
st.markdown("<h1 style='text-align: center; color: #0F172A; font-size: 32px; font-weight: 900; margin-top: 10px;'>👑 منصة <span style='color: #D4AF37;'>أصول</span> VIP</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #64748B; font-size: 15px; margin-bottom: 30px;'>بوابة الاستثمار الرقمي وإدارة الثروات المتقدمة</p>", unsafe_allow_html=True)

# 4. الثوابت وإعداد الجلسة
INITIAL_CASH = 1000.0       
TOTAL_TOKENS = 10000.0      

if 'cash_pool' not in st.session_state: st.session_state.cash_pool = INITIAL_CASH
if 'tokens_sold' not in st.session_state: st.session_state.tokens_sold = 0.0
if 'user_tokens' not in st.session_state: st.session_state.user_tokens = 0.0

tokens_remaining = TOTAL_TOKENS - st.session_state.tokens_sold
current_price = st.session_state.cash_pool / tokens_remaining

# 5. عرض البطاقات المالية (السعر، السيولة، المتاح)
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown(f"""
    <div class="premium-card">
        <div class="premium-title">سعر العملة</div>
        <div class="premium-value" style="color: #10B981;">${current_price:.4f}</div>
    </div>
    """, unsafe_allow_html=True)
with col2:
    st.markdown(f"""
    <div class="premium-card">
        <div class="premium-title">سيولة الصندوق</div>
        <div class="premium-value">${st.session_state.cash_pool:.2f}</div>
    </div>
    """, unsafe_allow_html=True)
with col3:
    st.markdown(f"""
    <div class="premium-card">
        <div class="premium-title">المتاح للبيع</div>
        <div class="premium-value" style="color: #D4AF37;">{tokens_remaining:.0f}</div>
    </div>
    """, unsafe_allow_html=True)

# 6. المحفظة الاستثمارية (Black Card Design)
user_value = st.session_state.user_tokens * current_price
st.markdown(f"""
<div class="wallet-box">
    <div class="wallet-flex">
        <div style="text-align: right;">
            <div style="font-size: 13px; color: #94A3B8; margin-bottom: 4px;">💼 رصيد محفظتك الاستثمارية</div>
            <div style="font-size: 22px; font-weight: 800; color: #FFFFFF;">{st.session_state.user_tokens:.2f} <span style="font-size: 14px; color: #D4AF37;">عملة</span></div>
        </div>
        <div style="text-align: left; background: rgba(255,255,255,0.05); padding: 10px 15px; border-radius: 10px; border: 1px solid rgba(255,255,255,0.1);">
            <div style="font-size: 11px; color: #94A3B8; margin-bottom: 2px;">القيمة النقدية الحالية</div>
            <div style="font-size: 18px; font-weight: 700; color: #10B981;">${user_value:.2f}</div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# 7. التداول والعمليات
tab1, tab2 = st.tabs(["🟢 أمر شراء مستثمر", "🔴 أمر بيع وتخارج"])

with tab1:
    st.markdown("<p style='color:#64748b; font-size:14px; font-weight:500;'>المبلغ المراد ضخه في منصة أصول ($):</p>", unsafe_allow_html=True)
    buy_amount = st.number_input("", min_value=0.0, step=10.0, key="buy", label_visibility="collapsed")
    if st.button("تأكيد أمر الشراء 💳", use_container_width=True):
        if buy_amount > 0:
            tokens_bought = buy_amount / current_price
            st.session_state.cash_pool += buy_amount
            st.session_state.tokens_sold += tokens_bought
            st.session_state.user_tokens += tokens_bought
            st.success(f"تم تنفيذ الصفقة! تمت إضافة {tokens_bought:.2f} عملة لمحفظتك.")
            st.rerun()

with tab2:
    st.markdown("<p style='color:#64748b; font-size:14px; font-weight:500;'>عدد العملات المراد بيعها وسحبها كاش:</p>", unsafe_allow_html=True)
    sell_tokens = st.number_input("", min_value=0.0, step=10.0, key="sell", label_visibility="collapsed")
    if st.button("تأكيد التخارج وسحب الرصيد 🏦", use_container_width=True):
        if sell_tokens <= st.session_state.user_tokens and sell_tokens > 0:
            cash_out = sell_tokens * current_price
            st.session_state.cash_pool -= cash_out
            st.session_state.tokens_sold -= sell_tokens
            st.session_state.user_tokens -= sell_tokens
            st.success(f"تم التخارج بنجاح! تم تحويل ${cash_out:.2f} إلى رصيدك النقدي.")
            st.rerun()
        else:
            st.error("رصيد محفظتك من العملات غير كافٍ.")

st.markdown("<div style='margin-top: 40px; text-align: center; color: #CBD5E1; font-size: 11px;'>جميع المعاملات مشفرة ومؤمنة بواسطة خوارزميات التوازن المالي التلقائي (AMM) &copy; 2026</div>", unsafe_allow_html=True)
