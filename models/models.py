import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Download VADER lexicon if not already downloaded
nltk.download('vader_lexicon')

def analyze_sentiment(text):
    """
    Analyzes the sentiment of the given text using VADER sentiment analysis.
    
    Parameters:
        text (str): The text to analyze.
        
    Returns:
        str: The sentiment label ('positive', 'negative', 'neutral').
    """
    # Initialize the VADER sentiment analyzer
    sid = SentimentIntensityAnalyzer()
    # Analyze sentiment
    scores = sid.polarity_scores(text)
    
    # Classify sentiment
    if scores['compound'] >= 0.05:
        sents =  'positive'
    elif scores['compound'] <= -0.05:
        sents =  'negative'
    else:
        sents =  'neutral'
    return sents

def sentiment_append(dataframe): 
    sentiment = []
    for _,rows in dataframe.iterrows():
        sentiment.append(analyze_sentiment(rows["long_description"]))

    dataframe["sentiment"] = sentiment
    return dataframe