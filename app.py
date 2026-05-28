import streamlit as st
import pandas as pd

# 1. إعدادات الصفحة الكلية وثيم الألوان المخصص
st.set_page_config(page_title="أصول | للتبادل الرقمي", page_icon="💎", layout="centered")

# تطبيق كود CSS مخصص لتحسين مظهر الواجهة بالكامل واستهداف مستخدمي الهاتف
st.markdown("""
    <style>
    /* تغيير خلفية التطبيق لتبدو أكثر احترافية */
    .main {
        background-color: #f8fafc;
    }
    /* تصميم بطاقات عرض البيانات المخصصة */
    .metric-card {
        background-color: #ffffff;
        border-radius: 12px;
        padding: 20px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -1px rgba(0, 0, 0, 0.03);
        border: 1px solid #e2e8f0;
        text-align: center;
        margin-bottom: 15px;
    }
    .metric-title {
        font-size: 14px;
        color: #64748b;
        font-weight: bold;
        margin-bottom: 8px;
    }
    .metric-value {
        font-size: 24px;
        color: #0f172a;
        font-weight: 800;
    }
    /* تحسين شكل التبويبات Tabs */
    .stTabs [data-baseweb="tab"] {
        font-size: 16px;
        font-weight: bold;
        color: #475569;
    }
    .stTabs [data-baseweb="tab"][aria-selected="true"] {
        color: #2563eb;
        border-bottom-color: #2563eb;
    }
    </style>
""", unsafe_allow_html=True)

# 2. الهيدر الرئيسي للمنصة بتصميم أرقى
st.markdown("<h1 style='text-align: center; color: #1e3a8a; font-size: 28px;'>💎 منصة أصول للاستثمار الرقمي</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #475569; font-size: 15px;'>نظام التداول الذكي القائم على التوازن التلقائي للسيولة والعرض والطلب الفعلي</p>", unsafe_allow_html=True)
st.markdown("<div style='margin: 20px 0; border-bottom: 2px solid #e2e8f0;'></div>", unsafe_allow_html=True)

# 3. الثوابت المالية للنظام
INITIAL_CASH = 1000.0       
TOTAL_TOKENS = 10000.0      

if 'cash_pool' not in st.session_state:
    st.session_state.cash_pool = INITIAL_CASH
if 'tokens_sold' not in st.session_state:
    st.session_state.tokens_sold = 0.0
if 'user_tokens' not in st.session_state:
    st.session_state.user_tokens = 0.0

# حساب السعر بناءً على معادلة الـ AMM
tokens_remaining = TOTAL_TOKENS - st.session_state.tokens_sold
current_price = st.session_state.cash_pool / tokens_remaining

# 4. عرض البيانات المالية بالبطاقات الاحترافية الجديدة (متوافقة تماماً مع شاشات الهاتف)
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">💵 سعر العملة الحالي</div>
        <div class="metric-value" style="color: #16a34a;">${current_price:.4f}</div>
    </div>
    """, unsafe_allow_html=True)
with col2:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">📊 السيولة بالصندوق</div>
        <div class="metric-value">${st.session_state.cash_pool:.2f}</div>
    </div>
    """, unsafe_allow_html=True)
with col3:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">🪙 المتاح للبيع</div>
        <div class="metric-value" style="color: #2563eb;">{tokens_remaining:.0f}</div>
    </div>
    """, unsafe_allow_html=True)

# 5. محفظة المستخدم الحالية بتصميم صندوق مميز
st.markdown("<br>", unsafe_allow_html=True)
user_value = st.session_state.user_tokens * current_price
st.markdown(f"""
<div style="background-color: #f1f5f9; padding: 15px; border-radius: 8px; border-right: 5px solid #64748b; margin-bottom: 25px;">
    <span style="color: #334155; font-weight: bold;">💼 محفظتك الاستثمارية الحالية:</span>
    <span style="float: left; color: #0f172a; font-weight: bold;">{st.session_state.user_tokens:.2f} عملة <span style="color: #64748b; font-size:13px;">(تساوي ${user_value:.2f})</span></span>
</div>
""", unsafe_allow_html=True)

# 6. تنفيذ عمليات الشراء والبيع (العرض والطلب التلقائي)
st.markdown("<h3 style='color: #0f172a; font-size: 18px; margin-bottom: 15px;'>🛒 تنفيذ صفقات التداول</h3>", unsafe_allow_html=True)
tab1, tab2 = st.tabs(["🟢 شراء واستثمار (طلب)", "🔴 بيع وتخارج (عرض)"])

with tab1:
    st.markdown("<p style='color:#64748b; font-size:13px;'>أدخل المبلغ بالدولار الذي ترغب بضخه في الصندوق لشراء العملات:</p>", unsafe_allow_html=True)
    buy_amount = st.number_input("المبلغ المستثمر ($):", min_value=0.0, step=5.0, key="buy", label_visibility="collapsed")
    if st.button("تأكيد عملية الشراء والضخ 💳", use_container_width=True):
        if buy_amount > 0:
            tokens_bought = buy_amount / current_price
            st.session_state.cash_pool += buy_amount
            st.session_state.tokens_sold += tokens_bought
            st.session_state.user_tokens += tokens_bought
            st.success(f"تمت العملية بنجاح! السعر ارتفع تلقائياً نتيجة لزيادة الطلب والسيولة.")
            st.rerun()

with tab2:
    st.markdown("<p style='color:#64748b; font-size:13px;'>أدخل عدد العملات التي تريد بيعها للمنصة لاسترداد قيمتها كاش فوراً:</p>", unsafe_allow_html=True)
    sell_tokens = st.number_input("عدد العملات المراد بيعها:", min_value=0.0, step=10.0, key="sell", label_visibility="collapsed")
    if st.button("تأكيد البيع وسحب الكاش 💰", use_container_width=True):
        if sell_tokens <= st.session_state.user_tokens and sell_tokens > 0:
            cash_out = sell_tokens * current_price
            st.session_state.cash_pool -= cash_out
            st.session_state.tokens_sold -= sell_tokens
            st.session_state.user_tokens -= sell_tokens
            st.success(f"تم التخارج بنجاح واستلام ${cash_out:.2f}. السعر انخفض لحفظ التوازن المالي.")
            st.rerun()
        else:
            st.error("عذراً، الرصيد المتاح في محفظتك غير كافٍ لإتمام هذه الصفقة.")

st.markdown("<div style='margin: 30px 0; border-bottom: 1px solid #e2e8f0;'></div>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #94a3b8; font-size: 11px;'>🔒 النظام المالي محمي بمعادلات AMM الرياضية لضمان التوازن وحفظ الحقوق الاستثمارية.</p>", unsafe_allow_html=True)
