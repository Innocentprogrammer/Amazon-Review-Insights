import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
nltk.download('vader_lexicon')


# Load dataset
df = pd.read_csv("C:/Users/acer/Downloads/cleaned_reviews.csv")

# Initialize sentiment analyzer
sia = SentimentIntensityAnalyzer()

# Compute sentiment scores
df['Sentiment Score'] = df['cleaned_review'].apply(lambda x: sia.polarity_scores(str(x))['compound'])

# Classify as Positive, Negative, or Neutral
def classify_sentiment(score):
    if score > 0.05:
        return "Positive"
    elif score < -0.05:
        return "Negative"
    else:
        return "Neutral"

df['Sentiment'] = df['Sentiment Score'].apply(classify_sentiment)

# Save processed data for Power BI
df.to_csv("processed_reviews.csv", index=False)
