import streamlit as st
from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Page config
st.set_page_config(page_title="Social Sentiment Analyzer", page_icon="🌐", layout="centered")

# Title
st.title("🌐 Social Sentiment Analyzer")
st.write("Analyze sentiment of text using **TextBlob** and **VADER** NLP models.")

# User input
text = st.text_area("✍️ Enter your text here:")

if st.button("Analyze Sentiment"):
    if text.strip():
        # --- TextBlob ---
        blob = TextBlob(text)
        polarity = blob.sentiment.polarity  # -1 (negative) to +1 (positive)

        # --- VADER ---
        analyzer = SentimentIntensityAnalyzer()
        vader_score = analyzer.polarity_scores(text)

        # Decide sentiment
        if polarity > 0:
            sentiment = "Positive 😀"
        elif polarity < 0:
            sentiment = "Negative 😡"
        else:
            sentiment = "Neutral 😐"

        # Show results in Streamlit
        st.subheader("📊 Results")
        st.write(f"**Final Sentiment:** {sentiment}")
        st.write(f"**TextBlob Polarity:** {polarity:.2f}")
        st.write(f"**VADER Scores:** {vader_score}")
    else:
        st.warning("⚠️ Please enter some text before analyzing.")
