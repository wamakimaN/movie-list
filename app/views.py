from flask import render_template
from app import app
from newsapi import NewsApiClient

@app.route('/')
def index():
    """
    view root page function that returns the index page and its data
    """

    return render_template('index.html')

@app.route('/aljazeera')
def aljazeera():
    newsapi = NewsApiClient(api_key = app.config["NEWS_API_KEY"])
    topheadlines = newsapi.get_top_headlines(sources="al-jazeera-english")
    articles = topheadlines['articles']
    desc = []
    news = []
    img = []
    for i in range(len(articles)):
        myarticles = articles[i]
        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
    mylist = zip(news,desc,img)
    return render_template('aljazeera.html', context = mylist)

@app.route('/cnn')
def cnn():
    newsapi = NewsApiClient(api_key= app.config["NEWS_API_KEY"])
    topheadlines = newsapi.get_top_headlines(sources="cnn")
    articles = topheadlines['articles']
    desc = []
    news = []
    img = []
    for i in range(len(articles)):
        myarticles = articles[i]
        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
    mylist = zip(news,desc,img)
    return render_template('cnn.html', context = mylist)

@app.route('/cnbc')
def cnbc():
    newsapi = NewsApiClient(api_key= app.config["NEWS_API_KEY"])
    topheadlines = newsapi.get_top_headlines(sources="cnbc")
    articles = topheadlines['articles']
    desc = []
    news = []
    img = []
    for i in range(len(articles)):
        myarticles = articles[i]
        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
    mylist = zip(news,desc,img)
    return render_template('cnbc.html', context = mylist)

@app.route('/bbc')
def bbc():
    newsapi = NewsApiClient(api_key= app.config["NEWS_API_KEY"])
    topheadlines = newsapi.get_top_headlines(sources="bbc-news")
    articles = topheadlines['articles']
    desc = []
    news = []
    img = []
    for i in range(len(articles)):
        myarticles = articles[i]
        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
    mylist = zip(news,desc,img)
    return render_template('bbc.html', context = mylist)

@app.route('/espn')
def espn():
    newsapi = NewsApiClient(api_key= app.config["NEWS_API_KEY"])
    topheadlines = newsapi.get_top_headlines(sources="espn")
    articles = topheadlines['articles']
    desc = []
    news = []
    img = []
    for i in range(len(articles)):
        myarticles = articles[i]
        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
    mylist = zip(news,desc,img)
    return render_template('espn.html', context = mylist)

@app.route('/reuters')
def reuters():
    newsapi = NewsApiClient(api_key= app.config["NEWS_API_KEY"])
    topheadlines = newsapi.get_top_headlines(sources="reuters")
    articles = topheadlines['articles']
    desc = []
    news = []
    img = []
    for i in range(len(articles)):
        myarticles = articles[i]
        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
    mylist = zip(news,desc,img)
    return render_template('reuters.html', context = mylist)