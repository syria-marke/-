import streamlit as st
import pandas as pd

# 1. إعدادات الصفحة والواجهة
st.set_page_config(page_title="منصة الاستثمار الرقمي", page_icon="📈", layout="centered")

st.title("📈 منصة الاستثمار والتجارة الرقمية")
st.write("مرحباً بك في لوحة التحكم الاستثمارية الحية القائمة على العرض والطلب الحقيقي.")
st.markdown("---")

# 2. الثوابت المالية للنظام (نقطة الانطلاق التلقائية)
INITIAL_CASH = 1000.0       # السيولة الاحتياطية التي وضعتها أنت في الصندوق
TOTAL_TOKENS = 10000.0      # إجمالي عدد العملات المتاحة في المرحلة الأولى

# محاكاة بسيطة لتخزين البيانات (سيتم ربطها بـ Supabase لاحقاً لضمان الأمان الكامل)
if 'cash_pool' not in st.session_state:
    st.session_state.cash_pool = INITIAL_CASH
if 'tokens_sold' not in st.session_state:
    st.session_state.tokens_sold = 0.0
if 'user_tokens' not in st.session_state:
    st.session_state.user_tokens = 0.0

# 3. معادلة العرض والطلب التلقائية (AMM Formula)
tokens_remaining = TOTAL_TOKENS - st.session_state.tokens_sold
current_price = st.session_state.cash_pool / tokens_remaining

# 4. عرض البيانات الحية للمستثمرين
col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="💵 سعر العملة الحالي", value=f"${current_price:.4f}")
with col2:
    st.metric(label="📊 السيولة في الصندوق", value=f"${st.session_state.cash_pool:.2f}")
with col3:
    st.metric(label="🪙 العملات المتاحة للبيع", value=f"{tokens_remaining:.0f} عملة")

st.markdown("---")

# 5. محفظة المستخدم الحالية
st.subheader("💼 محفظتك الاستثمارية")
user_value = st.session_state.user_tokens * current_price
st.write(f"أنت تملك حالياً: **{st.session_state.user_tokens:.2f} عملة** (تساوي قيمتها: **${user_value:.2f}**)")

st.markdown("---")

# 6. تنفيذ عمليات الشراء والبيع (العرض والطلب التلقائي)
st.subheader("🛒 تنفيذ العمليات")

tab1, tab2 = st.tabs(["شراء العملة (طلب)", "بيع واسترداد كاش (عرض)"])

with tab1:
    buy_amount = st.number_input("أدخل المبلغ الذي تريد استثماره بالدولار ($):", min_value=0.0, step=5.0, key="buy")
    if st.button("تأكيد الشراء 🟢"):
        if buy_amount > 0:
            tokens_bought = buy_amount / current_price
            st.session_state.cash_pool += buy_amount
            st.session_state.tokens_sold += tokens_bought
            st.session_state.user_tokens += tokens_bought
            st.success(f"تمت العملية بنجاح! اشتريت {tokens_bought:.2f} عملة. السعر سيرتفع الآن تلقائياً.")
            st.rerun()

with tab2:
    sell_tokens = st.number_input("أدخل عدد العملات التي تريد بيعها للمنصة:", min_value=0.0, step=10.0, key="sell")
    if st.button("تأكيد البيع والتخارج 🔴"):
        if sell_tokens <= st.session_state.user_tokens and sell_tokens > 0:
            cash_out = sell_tokens * current_price
            st.session_state.cash_pool -= cash_out
            st.session_state.tokens_sold -= sell_tokens
            st.session_state.user_tokens -= sell_tokens
            st.success(f"تم التخارج بنجاح! استلمت ${cash_out:.2f} كاش. السعر سينخفض الآن تلقائياً لحفظ التوازن.")
            st.rerun()
        else:
            st.error("رصيدك من العملات غير كافٍ لإتمام هذه العملية.")

st.markdown("---")
st.caption("🔒 جميع العمليات محمية وموثقة تقنياً بناءً على عقود الاستثمار المشتركة.")
