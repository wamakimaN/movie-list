from flask import render_template
from app import app
from newsapi import NewsApiClient

@app.route('/')
def index():
    newsapi = NewsApiClient(api_key = app.config['NEWS_API_KEY'])
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

