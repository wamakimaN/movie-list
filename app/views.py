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
    newsapi = NewsApiClient(api_key="c2dc80373e954e7fbd0678a357875019")
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