import streamlit as st

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="أصول VIP",
    page_icon="💎",
    layout="centered",
)

# =========================
# GLOBAL CSS
# =========================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@300;400;500;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Tajawal', sans-serif !important;
}

#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

.stApp {
    background: #0F172A;
    color: white;
}

.block-container {
    padding-top: 1rem;
    padding-bottom: 2rem;
    max-width: 450px;
}

/* ===== TITLE ===== */
.vip-title {
    text-align: center;
    font-size: 34px;
    font-weight: 800;
    color: #D4AF37;
    margin-bottom: 0;
}

.vip-subtitle {
    text-align: center;
    color: #CBD5E1;
    margin-top: 5px;
    margin-bottom: 25px;
    font-size: 14px;
}

/* ===== METRIC CARDS ===== */
.metric-card {
    background: linear-gradient(145deg, #111827, #1E293B);
    padding: 18px;
    border-radius: 18px;
    border-top: 4px solid #D4AF37;
    box-shadow: 0 10px 25px rgba(0,0,0,0.35);
    transition: all 0.35s ease;
    margin-bottom: 16px;
}

.metric-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 18px 35px rgba(0,0,0,0.55);
}

.metric-title {
    color: #CBD5E1;
    font-size: 14px;
    margin-bottom: 10px;
}

.metric-value {
    font-size: 28px;
    font-weight: 800;
    color: white;
}

.green-price {
    color: #10B981;
}

/* ===== WALLET CARD ===== */
.wallet-card {
    background: linear-gradient(135deg, #050816, #111827, #1E293B);
    border-radius: 24px;
    padding: 24px;
    margin-top: 20px;
    margin-bottom: 25px;
    position: relative;
    overflow: hidden;
    border: 1px solid rgba(212,175,55,0.25);
    box-shadow: 0 12px 35px rgba(0,0,0,0.5);
}

.wallet-card::before {
    content: "";
    position: absolute;
    width: 200px;
    height: 200px;
    background: rgba(212,175,55,0.08);
    border-radius: 50%;
    top: -80px;
    right: -50px;
}

.wallet-chip {
    width: 50px;
    height: 38px;
    border-radius: 10px;
    background: linear-gradient(145deg, #D4AF37, #AA8C2C);
    margin-bottom: 22px;
}

.wallet-title {
    color: #D4AF37;
    font-size: 14px;
    font-weight: 600;
}

.wallet-balance {
    font-size: 32px;
    font-weight: 800;
    margin-top: 10px;
}

.wallet-usd {
    color: #CBD5E1;
    margin-top: 8px;
    font-size: 15px;
}

/* ===== TABS ===== */
.stTabs [data-baseweb="tab-list"] {
    gap: 12px;
    border-bottom: 1px solid rgba(255,255,255,0.1);
}

.stTabs [data-baseweb="tab"] {
    color: #CBD5E1;
    background-color: transparent;
    padding: 10px 18px;
    font-weight: 700;
}

.stTabs [aria-selected="true"] {
    color: #D4AF37 !important;
    border-bottom: 3px solid #D4AF37 !important;
}

/* ===== INPUTS ===== */
.stNumberInput input {
    background-color: #111827 !important;
    color: white !important;
    border-radius: 12px !important;
    border: 1px solid rgba(255,255,255,0.08) !important;
}

/* ===== BUTTONS ===== */
.stButton > button {
    width: 100%;
    border: none;
    border-radius: 14px;
    background: linear-gradient(135deg, #D4AF37, #AA8C2C);
    color: white;
    font-weight: 800;
    padding: 14px;
    transition: all 0.25s ease;
    font-size: 16px;
    letter-spacing: 0.5px;
}

.stButton > button:hover {
    transform: scale(1.03);
    box-shadow: 0 10px 25px rgba(212,175,55,0.35);
}

/* ===== INFO BOX ===== */
.info-box {
    background: #111827;
    padding: 16px;
    border-radius: 16px;
    margin-top: 18px;
    border-left: 4px solid #D4AF37;
    color: #E2E8F0;
}

/* ===== MOBILE OPTIMIZATION ===== */
@media (max-width: 480px) {
    .wallet-balance {
        font-size: 26px;
    }

    .metric-value {
        font-size: 24px;
    }

    .vip-title {
        font-size: 28px;
    }
}
</style>
""", unsafe_allow_html=True)

# =========================
# SESSION STATE
# =========================
INITIAL_CASH_POOL = 1000.0
TOTAL_TOKENS = 10000

if "cash_pool" not in st.session_state:
    st.session_state.cash_pool = INITIAL_CASH_POOL

if "tokens_sold" not in st.session_state:
    st.session_state.tokens_sold = 0.0

if "user_tokens" not in st.session_state:
    st.session_state.user_tokens = 0.0

# =========================
# PRICE FUNCTION
# =========================
available_tokens = TOTAL_TOKENS - st.session_state.tokens_sold

if available_tokens <= 0:
    available_tokens = 1

current_price = st.session_state.cash_pool / available_tokens

# =========================
# HEADER
# =========================
st.markdown('<div class="vip-title">💎 أصول VIP</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="vip-subtitle">منصة تداول واستثمار رقمية فاخرة للأصول الذكية</div>',
    unsafe_allow_html=True
)

# =========================
# METRIC CARDS
# =========================
st.markdown(f"""
<div class="metric-card">
    <div class="metric-title">سعر التوكن الحالي</div>
    <div class="metric-value green-price">${current_price:.4f}</div>
</div>
""", unsafe_allow_html=True)

st.markdown(f"""
<div class="metric-card">
    <div class="metric-title">سيولة المجمع النقدي</div>
    <div class="metric-value">${st.session_state.cash_pool:,.2f}</div>
</div>
""", unsafe_allow_html=True)

st.markdown(f"""
<div class="metric-card">
    <div class="metric-title">التوكنات المتوفرة</div>
    <div class="metric-value">{available_tokens:,.0f}</div>
</div>
""", unsafe_allow_html=True)

# =========================
# WALLET CARD
# =========================
wallet_value = st.session_state.user_tokens * current_price

st.markdown(f"""
<div class="wallet-card">
    <div class="wallet-chip"></div>

    <div class="wallet-title">
        محفظة المستثمر VIP
    </div>

    <div class="wallet-balance">
        {st.session_state.user_tokens:,.2f} TOKEN
    </div>

    <div class="wallet-usd">
        القيمة الحالية: ${wallet_value:,.2f}
    </div>
</div>
""", unsafe_allow_html=True)

# =========================
# TABS
# =========================
buy_tab, sell_tab = st.tabs(["شراء", "بيع"])

# =========================
# BUY TAB
# =========================
with buy_tab:

    st.markdown("### 🚀 شراء الأصول")

    buy_amount = st.number_input(
        "أدخل مبلغ الشراء بالدولار",
        min_value=1.0,
        step=1.0,
        placeholder="مثال: 100"
    )

    estimated_tokens = buy_amount / current_price

    st.markdown(f"""
    <div class="info-box">
        ستحصل تقريباً على <b>{estimated_tokens:.2f}</b> توكن
    </div>
    """, unsafe_allow_html=True)

    if st.button("شراء الآن 💰"):

        tokens_bought = buy_amount / current_price

        st.session_state.cash_pool += buy_amount
        st.session_state.tokens_sold += tokens_bought
        st.session_state.user_tokens += tokens_bought

        st.success("تم تنفيذ عملية الشراء بنجاح ✅")

        st.rerun()

# =========================
# SELL TAB
# =========================
with sell_tab:

    st.markdown("### 💸 بيع الأصول")

    sell_tokens = st.number_input(
        "عدد التوكنات المراد بيعها",
        min_value=0.0,
        step=1.0,
        placeholder="مثال: 50"
    )

    estimated_value = sell_tokens * current_price

    st.markdown(f"""
    <div class="info-box">
        القيمة التقديرية للبيع: <b>${estimated_value:.2f}</b>
    </div>
    """, unsafe_allow_html=True)

    if st.button("بيع الآن 🔥"):

        if sell_tokens <= 0:
            st.error("يرجى إدخال كمية صحيحة")

        elif sell_tokens > st.session_state.user_tokens:
            st.error("رصيدك غير كافٍ لإتمام العملية")

        else:

            sell_value = sell_tokens * current_price

            if sell_value > st.session_state.cash_pool:
                st.error("السيولة الحالية غير كافية")

            else:
                st.session_state.cash_pool -= sell_value
                st.session_state.tokens_sold -= sell_tokens
                st.session_state.user_tokens -= sell_tokens

                st.success("تم تنفيذ عملية البيع بنجاح ✅")

                st.rerun()

# =========================
# FOOTER INFO
# =========================
st.markdown("""
<br>

<div style="
text-align:center;
color:#64748B;
font-size:13px;
">
أصول VIP • نظام تداول ذكي يعتمد على خوارزمية AMM
</div>
""", unsafe_allow_html=True)
