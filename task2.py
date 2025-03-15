# -*- coding: utf-8 -*-
"""Task2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1nhLVGeAgU6nmSXB9pC9JO6X8SVNnzevF
"""

import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import re
import nltk
from nltk.corpus import stopwords

# Download NLTK stopwords
nltk.download('stopwords')

# Load datasets
data = pd.read_csv("/content/Playstore.csv")
reviews_data = pd.read_csv("/content/user review.csv")

# Filter for 'Health & Fitness' apps
df_health_apps = data[data['Category'] == 'Health & Fitness']['App Name'].unique()
matched_apps = [
    "30 Day Fitness Challenge - Workout at Home",
    "21-Day Meditation Experience",
    "10 Best Foods for You",
    "7 Day Food Journal Challenge"
]

# Filter reviews for matched apps and positive sentiment
filtered_reviews = reviews_data[
    (reviews_data['App'].isin(matched_apps)) &
    (reviews_data['Sentiment'] == 'Positive') &
    (reviews_data['Translated_Review'].notna())
]

# Combine all reviews into a single text
all_reviews_text = ' '.join(filtered_reviews['Translated_Review'].dropna())

# Text cleaning: remove non-alphabetic characters, lowercasing, and stopwords
stop_words = set(stopwords.words('english'))
additional_stopwords = {"best", "great", "good", "like", "well", "app"}  # Custom stopwords
stop_words.update(additional_stopwords)

# Cleaned text
cleaned_text = ' '.join(
    word for word in re.sub(r'[^a-zA-Z\s]', '', all_reviews_text.lower()).split()
    if word not in stop_words
)

# Generate and display the word cloud
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(cleaned_text)

plt.figure(figsize=(12, 6))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title("Word Cloud for Health & Fitness 5-Star Reviews")
plt.show()