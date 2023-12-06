#importing libraries
from textblob import TextBlob
#defining a textual variable containing several statements
sample_texts = ["I like programming.", "I can't stand injustice.", "I feel indifferent about documentation.", "coding is fun.", "I am frustrated with trigonometry."]

#running through all statement to extract sentiment out of them
for text in sample_texts:
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity
    subjectivity = analysis.sentiment.subjectivity

    if polarity > 0:
        sentiment = "Positive"
    elif polarity < 0:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    print(f"Text: {text}")
    print(f"Sentiment: {sentiment}")
    print(f"Polarity: {polarity}")
    print(f"Subjectivity: {subjectivity}")
    print("------")