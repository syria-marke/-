import streamlit as st

# 1. تفعيل العرض الكامل لمنع التصميم الرفيع
st.set_page_config(page_title="أصول VIP", page_icon="👑", layout="wide")

# كود CSS مخصص لكسر قيود المقاسات الافتراضية والتحكم في أبعاد الهاتف
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@500;700;900&display=swap');
    
    * { font-family: 'Tajawal', sans-serif !important; }
    
    /* جعل التطبيق يمتد بالكامل بدون حواف ضيقة */
    .block-container {
        padding-top: 1rem !important;
        padding-bottom: 1rem !important;
        padding-left: 1rem !important;
        padding-right: 1rem !important;
        max-width: 100% !important;
    }
    
    .stApp {
        background: linear-gradient(180deg, #0B111E 0%, #060913 100%);
    }
    
    #MainMenu, footer, header { visibility: hidden; }
    
    /* تصميم حاوية عرض البطاقات أفقياً */
    .metrics-container {
        display: flex;
        gap: 10px;
        justify-content: space-between;
        margin-bottom: 20px;
    }
    
    .custom-card {
        flex: 1;
        background: #0E1726;
        border: 1px solid #1E293B;
        border-radius: 12px;
        padding: 12px 5px;
        text-align: center;
        box-shadow: 0 4px 20px rgba(0,0,0,0.3);
    }
    
    .card-title {
        color: #64748B;
        font-size: 11px;
        font-weight: 500;
        margin-bottom: 4px;
    }
    
    .card-value {
        font-size: 18px;
        font-weight: 900;
    }
    
    /* بطاقة المحفظة العريضة الفخمة */
    .vip-wallet {
        background: linear-gradient(135deg, #111827 0%, #1F2937 100%);
        border: 1px solid #D4AF37;
        border-radius: 16px;
        padding: 20px;
        margin: 20px 0;
        box-shadow: 0 8px 32px rgba(212, 175, 55, 0.15);
    }
    
    .wallet-header {
        color: #D4AF37;
        font-size: 14px;
        font-weight: 700;
        margin-bottom: 10px;
    }
    
    /* تحسين الأزرار */
    div[data-testid="stButton"] > button {
        background: linear-gradient(135deg, #D4AF37 0%, #AA8C2C 100%) !important;
        color: #060913 !important;
        border: none !important;
        border-radius: 10px !important;
        font-weight: 700 !important;
        font-size: 15px !important;
        padding: 10px !important;
        box-shadow: 0 4px 15px rgba(212, 175, 55, 0.2) !important;
    }
    </style>
""", unsafe_allow_html=True)

# العنوان العلوي الفخم
st.markdown("<h2 style='text-align: center; color: #FFFFFF; font-weight: 900; margin-bottom: 5px;'>👑 VIP أصول</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #64748B; font-size: 13px; margin-bottom: 25px;'>منصة تداول واستثمار رقمية ذكية</p>", unsafe_allow_html=True)

# الثوابت المالية ونظام الحسابات
INITIAL_CASH = 1000.0
TOTAL_TOKENS = 10000.0

if 'cash_pool' not in st.session_state: st.session_state.cash_pool = INITIAL_CASH
if 'tokens_sold' not in st.session_state: st.session_state.tokens_sold = 0.0
if 'user_tokens' not in st.session_state: st.session_state.user_tokens = 0.0

tokens_remaining = TOTAL_TOKENS - st.session_state.tokens_sold
current_price = st.session_state.cash_pool / tokens_remaining

# عرض البطاقات أفقياً بعرض الشاشة لمنع التراكم العمودي الرفيع
st.markdown(f"""
<div class="metrics-container">
    <div class="custom-card">
        <div class="card-title">سعر التوكن</div>
        <div class="card-value" style="color: #10B981;">${current_price:.4f}</div>
    </div>
    <div class="custom-card">
        <div class="card-title">سيولة المجمع</div>
        <div class="card-value" style="color: #FFFFFF;">${st.session_state.cash_pool:.0f}</div>
    </div>
    <div class="custom-card">
        <div class="card-title">المتوفر</div>
        <div class="card-value" style="color: #38BDF8;">{tokens_remaining:.0f}</div>
    </div>
</div>
""", unsafe_allow_html=True)

# المحفظة بستايل البطاقة الفخمة العريضة
user_value = st.session_state.user_tokens * current_price
st.markdown(f"""
<div class="vip-wallet">
    <div class="wallet-header">👑 محفظة المستثمر VIP</div>
    <div style="display: flex; justify-content: space-between; align-items: center;">
        <div style="font-size: 24px; font-weight: 900; color: #FFFFFF;">{st.session_state.user_tokens:.2f} <span style="font-size: 14px; color: #64748B;">TOKEN</span></div>
        <div style="font-size: 16px; color: #10B981; font-weight: 700;">القيمة: ${user_value:.2f}</div>
    </div>
</div>
""", unsafe_allow_html=True)

# لوحة التحكم في الصفقات (أزرار عريضة ومتجاوبة)
tab1, tab2 = st.tabs(["🟢 شراء الأصول", "🔴 بيع وتخارج"])

with tab1:
    buy_amount = st.number_input("أدخل مبلغ الشراء ($):", min_value=0.0, step=10.0, key="buy_vip")
    if st.button("شراء الآن 💳", use_container_width=True):
        if buy_amount > 0:
            tokens_bought = buy_amount / current_price
            st.session_state.cash_pool += buy_amount
            st.session_state.tokens_sold += tokens_bought
            st.session_state.user_tokens += tokens_bought
            st.rerun()

with tab2:
    sell_tokens = st.number_input("عدد التوكنات للمراد بيعها:", min_value=0.0, step=10.0, key="sell_vip")
    if st.button("تأكيد البيع النقدي 🏦", use_container_width=True):
        if sell_tokens <= st.session_state.user_tokens and sell_tokens > 0:
            cash_out = sell_tokens * current_price
            st.session_state.cash_pool -= cash_out
            st.session_state.tokens_sold -= sell_tokens
            st.session_state.user_tokens -= sell_tokens
            st.rerun()
