import urllib.request, json
from app import app
from .models import news

News = news.News

# Getting api key
api_key = app.config['NEWS_API_KEY']

# Getting the movie base url
news_url = app.config["NEWS_API_BASE_URL"]

# getting the sources url
source_url= app.config["SOURCES_API_BASE_URL"]

def get_news(id):
    get_news_url = news_url.format(id, api_key)
    
    with urllib.request.urlopen(get_news_url) as url:
        news_data = url.read()
        news_response = json.loads(news_data)

        news_articles = None

        if news_response['articles']:
            news_articles_list = news_response['articles']
            news_articles = process_articles(news_articles_list)  
           
    return news_articles    

def process_articles(news_list):
    """
    Function that processes the news sources and transforms them to a list of objects
    """
    
    news_articles = []   
    
    for news in news_list:
        
        author = news.get('author')
        title = news.get('title')
        description = news.get('description')
        url = news.get('url')
        urlToImage = news.get('urlToImage')
        publishedAt = news.get('publishedAt')
        
        if urlToImage:
            news_object = News(author, title, description, url, urlToImage, publishedAt)
            news_articles.append(news_object)
          
    return news_articles