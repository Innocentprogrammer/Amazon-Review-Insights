# Amazon-Review-Insights

-- This project performs sentiment analysis on customer reviews using Python and visualizes the insights using Power BI. The goal is to categorize customer sentiments (Positive, Negative, Neutral) based on the reviews provided, which can help businesses analyze customer satisfaction and make data-driven decisions.

# Project Overview

-- Customer reviews are a valuable source of feedback for businesses. This project analyzes text data from customer reviews to determine sentiment, which can help in understanding customer satisfaction. The analysis is performed using VADER Sentiment Analysis in Python, and the results are visualized using Power BI.

# Data Source

-- The dataset used in this project consists of customer reviews from an e-commerce platform. The data contains review text, customer ratings, and the review date.

### Raw Data: Amazon Reviews Dataset (or your data source).

### Setup Instructions

1. Clone the Repository
   Clone this repository to your local machine:
   git clone https://github.com/yourusername/customer-sentiment-analysis.git
2. Install Dependencies
   The project requires the following Python libraries:
   pandas
   nltk
   vaderSentiment
   pip install -r requirements.txt
3. Run Sentiment Analysis Script
   -- After setting up the environment, you can run the sentiment analysis script to process the raw customer reviews and generate sentiment labels.
   -- This script processes the raw review data, performs sentiment analysis using VADER, and outputs a processed CSV file containing sentiment labels (Positive, Negative, Neutral).

### Visualizations

    -- The sentiment analysis results are visualized using Power BI. Key visualizations include:
    -- Sentiment Distribution (Pie Chart): Shows the proportion of positive, negative, and neutral reviews.
    -- Sentiment Trends Over Time (Line Chart): Displays sentiment trends over different time periods.
    -- Rating vs Sentiment Analysis (Bar Chart): Analyzes sentiment based on customer ratings.The Power BI dashboard (sentiment_analysis_dashboard.pbix) can be opened in Power BI Desktop.
    -- The dashboard will display visual insights based on the sentiment analysis of customer reviews.
    -- Use the filters in Power BI to view trends by sentiment, date, or other parameters.

### Acknowledgments

    -- VADER Sentiment Analysis: Used for performing sentiment analysis on text data.
    -- Power BI: Used for creating interactive visualizations and dashboards.
    -- Kaggle: For providing the dataset used in this project.
