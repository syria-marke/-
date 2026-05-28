import streamlit as st

# =========================================================
# PAGE CONFIG
# =========================================================
st.set_page_config(
    page_title="أصول VIP",
    page_icon="💚",
    layout="centered",
)

# =========================================================
# SESSION STATE
# =========================================================
INITIAL_CASH_POOL = 1000.0
TOTAL_TOKENS = 10000

if "cash_pool" not in st.session_state:
    st.session_state.cash_pool = INITIAL_CASH_POOL

if "tokens_sold" not in st.session_state:
    st.session_state.tokens_sold = 1250.0

if "user_tokens" not in st.session_state:
    st.session_state.user_tokens = 125.50

# =========================================================
# AMM PRICE
# =========================================================
available_tokens = TOTAL_TOKENS - st.session_state.tokens_sold

if available_tokens <= 0:
    available_tokens = 1

current_price = st.session_state.cash_pool / available_tokens

wallet_value = st.session_state.user_tokens * current_price

# =========================================================
# CSS
# =========================================================
st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@300;400;500;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Tajawal', sans-serif !important;
}

#MainMenu {
    visibility: hidden;
}

header {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

.stApp {
    background:
    radial-gradient(circle at top right, rgba(16,185,129,0.15), transparent 25%),
    radial-gradient(circle at bottom left, rgba(16,185,129,0.08), transparent 25%),
    #020617;

    color: white;
}

.block-container {
    max-width: 430px;
    padding-top: 1rem;
    padding-bottom: 3rem;
}

/* =========================================================
TITLE
========================================================= */

.vip-title {
    text-align: center;
    font-size: 34px;
    font-weight: 800;
    color: white;
    margin-bottom: 0;
}

.vip-sub {
    text-align: center;
    color: #94A3B8;
    margin-top: 5px;
    margin-bottom: 25px;
    font-size: 14px;
}

/* =========================================================
METRIC CARDS
========================================================= */

.metric-grid {
    display: grid;
    grid-template-columns: repeat(3,1fr);
    gap: 10px;
    margin-bottom: 18px;
}

.metric-card {
    background: linear-gradient(145deg,#07111f,#0b1727);
    border: 1px solid rgba(16,185,129,0.18);
    border-radius: 18px;
    padding: 15px;
    box-shadow: 0 8px 25px rgba(0,0,0,0.35);
    transition: 0.3s ease;
}

.metric-card:hover {
    transform: translateY(-4px);
    border-color: #10B981;
}

.metric-title {
    color: #94A3B8;
    font-size: 12px;
    margin-bottom: 8px;
}

.metric-value {
    color: white;
    font-size: 22px;
    font-weight: 800;
}

.metric-green {
    color: #10B981;
}

/* =========================================================
WALLET
========================================================= */

.wallet-card {
    position: relative;
    overflow: hidden;

    background:
    linear-gradient(135deg,#04110d,#071d16,#0b1727);

    border-radius: 26px;
    padding: 24px;
    margin-top: 18px;
    margin-bottom: 22px;

    border: 1px solid rgba(16,185,129,0.3);

    box-shadow:
    0 15px 40px rgba(0,0,0,0.45),
    0 0 30px rgba(16,185,129,0.08);
}

.wallet-card::before {
    content: "";
    position: absolute;
    width: 220px;
    height: 220px;
    border-radius: 50%;

    background: radial-gradient(circle, rgba(16,185,129,0.18), transparent 70%);

    top: -100px;
    right: -70px;
}

.wallet-title {
    color: #FACC15;
    font-size: 15px;
    font-weight: 700;
}

.wallet-balance {
    margin-top: 14px;
    font-size: 34px;
    font-weight: 800;
}

.wallet-value {
    color: #CBD5E1;
    margin-top: 10px;
}

/* =========================================================
TABS
========================================================= */

.stTabs [data-baseweb="tab-list"] {
    gap: 10px;
    margin-bottom: 10px;
}

.stTabs [data-baseweb="tab"] {
    background: #07111f;
    border-radius: 14px;
    height: 52px;
    color: white;
    font-weight: 700;
    border: 1px solid rgba(255,255,255,0.05);
}

.stTabs [aria-selected="true"] {
    background: linear-gradient(135deg,#16A34A,#10B981);
    color: white !important;
}

/* =========================================================
INPUTS
========================================================= */

.stNumberInput > div {
    background: transparent !important;
}

.stNumberInput input {
    background: #07111f !important;
    border: 1px solid rgba(16,185,129,0.25) !important;
    color: white !important;
    border-radius: 16px !important;
    height: 58px !important;
    font-size: 24px !important;
    font-weight: 700 !important;
}

/* =========================================================
BUTTONS
========================================================= */

.stButton button {
    width: 100%;
    height: 58px;

    border: none;
    border-radius: 18px;

    background:
    linear-gradient(135deg,#16A34A,#10B981);

    color: white;
    font-size: 20px;
    font-weight: 800;

    transition: 0.3s ease;

    box-shadow:
    0 12px 30px rgba(16,185,129,0.25);
}

.stButton button:hover {
    transform: scale(1.02);
}

/* =========================================================
BUY BOX
========================================================= */

.buy-box {
    background:
    linear-gradient(145deg,#07111f,#0b1727);

    border-radius: 24px;
    padding: 22px;

    border: 1px solid rgba(16,185,129,0.15);

    margin-top: 10px;
}

.buy-title {
    text-align: center;
    font-size: 34px;
    font-weight: 800;
    margin-bottom: 8px;
}

.buy-sub {
    text-align: center;
    color: #94A3B8;
    margin-bottom: 20px;
}

/* =========================================================
INFO BOX
========================================================= */

.info-box {
    background: rgba(16,185,129,0.08);

    border: 1px solid rgba(16,185,129,0.25);

    padding: 18px;

    border-radius: 18px;

    margin-top: 18px;

    color: white;
}

.big-green {
    color: #22C55E;
    font-size: 22px;
    font-weight: 800;
}

/* =========================================================
FOOTER
========================================================= */

.footer-box {
    margin-top: 20px;

    background:
    linear-gradient(145deg,#07111f,#0b1727);

    border-radius: 20px;

    padding: 16px;

    border: 1px solid rgba(16,185,129,0.1);

    color: #CBD5E1;
}

/* =========================================================
MOBILE
========================================================= */

@media (max-width: 480px){

    .metric-grid {
        grid-template-columns: 1fr;
    }

    .wallet-balance {
        font-size: 28px;
    }

    .buy-title {
        font-size: 28px;
    }

}

</style>
""", unsafe_allow_html=True)

# =========================================================
# HEADER
# =========================================================
st.markdown("""
<div class="vip-title">
💎 أصول VIP
</div>

<div class="vip-sub">
منصة تداول واستثمار رقمية ذكية
</div>
""", unsafe_allow_html=True)

# =========================================================
# METRICS
# =========================================================
st.markdown(f"""
<div class="metric-grid">

<div class="metric-card">
<div class="metric-title">
سعر التوكن
</div>

<div class="metric-value metric-green">
${current_price:.4f}
</div>
</div>

<div class="metric-card">
<div class="metric-title">
سيولة المجمع
</div>

<div class="metric-value">
${st.session_state.cash_pool:,.0f}
</div>
</div>

<div class="metric-card">
<div class="metric-title">
المتوفر
</div>

<div class="metric-value">
{available_tokens:,.0f}
</div>
</div>

</div>
""", unsafe_allow_html=True)

# =========================================================
# WALLET
# =========================================================
st.markdown(f"""
<div class="wallet-card">

<div class="wallet-title">
👑 محفظة المستثمر VIP
</div>

<div class="wallet-balance">
{st.session_state.user_tokens:,.2f} TOKEN
</div>

<div class="wallet-value">
القيمة الحالية: ${wallet_value:,.2f}
</div>

</div>
""", unsafe_allow_html=True)

# =========================================================
# TABS
# =========================================================
buy_tab, sell_tab = st.tabs(["شراء", "بيع"])

# =========================================================
# BUY
# =========================================================
with buy_tab:

    st.markdown("""
    <div class="buy-box">

    <div class="buy-title">
    🚀 شراء الأصول
    </div>

    <div class="buy-sub">
    استثمر الآن وكن جزءاً من النمو
    </div>

    </div>
    """, unsafe_allow_html=True)

    buy_amount = st.number_input(
        "أدخل مبلغ الشراء بالدولار",
        min_value=1.0,
        value=100.0,
        step=10.0
    )

    estimated_tokens = buy_amount / current_price

    st.markdown(f"""
    <div class="info-box">
    ستحصل تقريباً على

    <div class="big-green">
    {estimated_tokens:,.2f} TOKEN
    </div>
    </div>
    """, unsafe_allow_html=True)

    if st.button("شراء الآن 💚"):

        tokens_bought = buy_amount / current_price

        st.session_state.cash_pool += buy_amount
        st.session_state.tokens_sold += tokens_bought
        st.session_state.user_tokens += tokens_bought

        st.success("تم تنفيذ عملية الشراء بنجاح ✅")

        st.rerun()

# =========================================================
# SELL
# =========================================================
with sell_tab:

    st.markdown("""
    <div class="buy-box">

    <div class="buy-title">
    💸 بيع الأصول
    </div>

    <div class="buy-sub">
    قم ببيع التوكنات بسهولة
    </div>

    </div>
    """, unsafe_allow_html=True)

    sell_tokens = st.number_input(
        "أدخل كمية التوكن",
        min_value=0.0,
        value=10.0,
        step=1.0
    )

    estimated_value = sell_tokens * current_price

    st.markdown(f"""
    <div class="info-box">

    ستحصل على

    <div class="big-green">
    ${estimated_value:,.2f}
    </div>

    </div>
    """, unsafe_allow_html=True)

    if st.button("بيع الآن 🔥"):

        if sell_tokens > st.session_state.user_tokens:

            st.error("الرصيد غير كافٍ")

        else:

            sell_value = sell_tokens * current_price

            st.session_state.cash_pool -= sell_value
            st.session_state.tokens_sold -= sell_tokens
            st.session_state.user_tokens -= sell_tokens

            st.success("تم تنفيذ عملية البيع بنجاح ✅")

            st.rerun()

# =========================================================
# FOOTER
# =========================================================
st.markdown("""
<div class="footer-box">

🔒 جميع العمليات مشفرة وآمنة

<br><br>

يعتمد النظام على خوارزمية AMM الذكية

</div>
""", unsafe_allow_html=True)
