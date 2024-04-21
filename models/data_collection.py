import pandas as pd
import numpy as np
import yfinance as yf
import datetime
import requests
import newspaper



def download_stock_data(symbol, start_date, end_date):
    """
    Download stock data based on stock symbol, start date, and end date.
    
    Parameters:
    symbol (str): Stock symbol (e.g., AAPL for Apple Inc.).
    start_date (str): Start date in YYYY-MM-DD format.
    end_date (str): End date in YYYY-MM-DD format.
    
    Returns:
    pandas.DataFrame: Stock data for the specified symbol and date range.
    """
    # Download stock data
    stock_data = yf.download(symbol, start=start_date, end=end_date)
    
    return stock_data



def get_indepth_news(url): # Download news content of url
    article = newspaper.Article(url)
    article.download()
    article.parse()
    content = article.text
    return content

def extract_news(stock_symbol,days_ago=5):

    api_key='126502c867164eea8fb5918b3793869d'
    # Calculate the date 5 days ago from today
    date_5_days_ago = (pd.to_datetime("now") - datetime.timedelta(days=days_ago)).strftime("%Y-%m-%d")

    url = f"https://newsapi.org/v2/everything?q={stock_symbol}&from={date_5_days_ago}&apiKey={api_key}"

    data = requests.get(url)
    json_newsdata = data.json()
    title = []
    description = []
    url = []
    ld_content = []
    long_description = []

    for items in json_newsdata["articles"]:
        title.append(items["title"])
        description.append(items["description"])
        url.append(items["url"])
        ld_content.append(items["content"])
        try:
            long_description.append(get_indepth_news(url=items["url"]))
        except newspaper.ArticleException as e:
            print(f"Error fetching article: {e}")
            long_description.append(items["title"])

    dc = {
    "title":title,
    "description":description,
    "url":url,
    "long_description":long_description,
    "content":ld_content
    }
    news_data = pd.DataFrame(dc)
    return news_data