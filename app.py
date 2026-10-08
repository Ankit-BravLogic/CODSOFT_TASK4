import streamlit as st
import joblib


# ---------------------------------------------------------
# Page Configuration
# ---------------------------------------------------------

st.set_page_config(
    page_title="SpamShield AI",
    page_icon="🛡️",
    layout="centered",
    initial_sidebar_state="collapsed"
)


# ---------------------------------------------------------
# Custom CSS
# ---------------------------------------------------------

st.markdown("""
<style>

    .main-title {
        font-size: 3rem;
        font-weight: 800;
        text-align: center;
        margin-bottom: 0.2rem;
    }

    .subtitle {
        text-align: center;
        font-size: 1.1rem;
        color: #9ca3af;
        margin-bottom: 2rem;
    }

    .info-card {
        padding: 1rem;
        border-radius: 12px;
        border: 1px solid rgba(128,128,128,0.25);
        background-color: rgba(128,128,128,0.05);
        text-align: center;
    }

    .result-title {
        font-size: 1.4rem;
        font-weight: 700;
    }

    .footer {
        text-align: center;
        color: #888888;
        font-size: 0.85rem;
        margin-top: 2rem;
    }

</style>
""", unsafe_allow_html=True)


# ---------------------------------------------------------
# Load Model and TF-IDF Vectorizer
# ---------------------------------------------------------

@st.cache_resource
def load_model():
    model = joblib.load("models/spam_model.pkl")
    vectorizer = joblib.load("models/tfidf_vectorizer.pkl")
    return model, vectorizer


model, tfidf = load_model()


# ---------------------------------------------------------
# Header
# ---------------------------------------------------------

st.markdown(
    '<div class="main-title">🛡️ SpamShield AI</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">AI-Powered SMS Spam Detection</div>',
    unsafe_allow_html=True
)

st.write(
    "Enter an SMS message below and let machine learning "
    "determine whether it is legitimate or spam."
)

st.divider()


# ---------------------------------------------------------
# Example Messages
# ---------------------------------------------------------

st.subheader("💡 Try an Example")

col1, col2 = st.columns(2)

with col1:
    if st.button(
        "📩 Legitimate Example",
        use_container_width=True
    ):
        st.session_state["message"] = (
            "Hey, are you coming to class today?"
        )

with col2:
    if st.button(
        "🚨 Spam Example",
        use_container_width=True
    ):
        st.session_state["message"] = (
            "Congratulations! You have won a free prize. "
            "Call now to claim your reward!"
        )


# ---------------------------------------------------------
# SMS Input
# ---------------------------------------------------------

message = st.text_area(
    "📱 Enter your SMS message",
    value=st.session_state.get("message", ""),
    placeholder=(
        "Example: Congratulations! You have won a free prize..."
    ),
    height=160
)


# ---------------------------------------------------------
# Message Statistics
# ---------------------------------------------------------

if message.strip():

    characters = len(message)
    words = len(message.split())

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Characters", characters)

    with col2:
        st.metric("Words", words)


st.write("")


# ---------------------------------------------------------
# Prediction
# ---------------------------------------------------------

if st.button(
    "🔍 Analyze Message",
    use_container_width=True,
    type="primary"
):

    if not message.strip():

        st.warning(
            "⚠️ Please enter an SMS message before analyzing."
        )

    else:

        # Convert message into TF-IDF features
        message_tfidf = tfidf.transform([message])

        # Make prediction
        prediction = model.predict(message_tfidf)[0]

        # Get model probabilities
        probabilities = model.predict_proba(message_tfidf)[0]

        ham_probability = probabilities[0] * 100
        spam_probability = probabilities[1] * 100

        st.divider()

        # -------------------------------------------------
        # SPAM RESULT
        # -------------------------------------------------

        if prediction == 1:

            st.error(
                "🚨 SPAM MESSAGE DETECTED"
            )

            st.markdown(
                '<div class="result-title">'
                '⚠️ This message may be unwanted or fraudulent.'
                '</div>',
                unsafe_allow_html=True
            )

            st.metric(
                "Spam Probability",
                f"{spam_probability:.2f}%"
            )

            st.progress(
                int(spam_probability)
            )

            st.write(
                "🔒 Recommendation: Avoid clicking unknown links, "
                "sharing personal information, or sending money."
            )

        # -------------------------------------------------
        # HAM RESULT
        # -------------------------------------------------

        else:

            st.success(
                "✅ LEGITIMATE MESSAGE (HAM)"
            )

            st.markdown(
                '<div class="result-title">'
                '👍 This message appears to be legitimate.'
                '</div>',
                unsafe_allow_html=True
            )

            st.metric(
                "Legitimate Probability",
                f"{ham_probability:.2f}%"
            )

            st.progress(
                int(ham_probability)
            )

            st.write(
                "This message does not appear to match "
                "the spam patterns learned by the model."
            )


# ---------------------------------------------------------
# How It Works
# ---------------------------------------------------------

st.divider()

with st.expander("🧠 How does SpamShield AI work?"):

    st.write(
        """
        **Step 1 — Text Processing**

        The SMS message is converted into numerical features
        using TF-IDF (Term Frequency-Inverse Document Frequency).

        **Step 2 — Machine Learning**

        A Multinomial Naive Bayes classifier analyzes the
        TF-IDF features.

        **Step 3 — Classification**

        The model predicts whether the message is:

        - 🟢 HAM — legitimate message
        - 🔴 SPAM — unwanted or suspicious message

        **Step 4 — Result**

        The application displays the predicted class and
        the model's predicted probability.
        """
    )


# ---------------------------------------------------------
# Model Information
# ---------------------------------------------------------

st.divider()

st.subheader("⚙️ Model Information")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(
        '<div class="info-card">'
        '<b>NLP</b><br>TF-IDF'
        '</div>',
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        '<div class="info-card">'
        '<b>Model</b><br>Naive Bayes'
        '</div>',
        unsafe_allow_html=True
    )

with col3:
    st.markdown(
        '<div class="info-card">'
        '<b>Task</b><br>Spam Detection'
        '</div>',
        unsafe_allow_html=True
    )


# ---------------------------------------------------------
# Footer
# ---------------------------------------------------------

st.markdown(
    """
    <div class="footer">
        Built with Python • Scikit-learn • Streamlit<br>
        CodSoft Machine Learning Internship • Task 4
    </div>
    """,
    unsafe_allow_html=True
)