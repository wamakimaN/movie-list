from flask import Flask,render_template
from newsapi import NewsApiClient

app = Flask(__name__)

@app.route('/')
def index():
    """
    view root page function that returns the index page and its data
    """

    return render_template('index.html')

@app.route('/aljazeera')
def aljazeera():
    newsapi = NewsApiClient(api_key = "32fc0e644efb4220b4d655e0ff7a2eb1")
    topheadlines = newsapi.get_top_headlines(sources="al-jazeera-english")
    articles = topheadlines['articles']
    desc = []
    news = []
    img = []
    url = []
    for i in range(len(articles)):
        myarticles = articles[i]
        url.append(myarticles['url'])
        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
    mylist = zip(news,desc,img,url)
    return render_template('aljazeera.html', context = mylist)

@app.route('/cnn')
def cnn():
    newsapi = NewsApiClient(api_key= "32fc0e644efb4220b4d655e0ff7a2eb1")
    topheadlines = newsapi.get_top_headlines(sources="cnn")
    articles = topheadlines['articles']
    desc = []
    news = []
    img = []
    url = []
    for i in range(len(articles)):
        myarticles = articles[i]
        url.append(myarticles['url'])
        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
    mylist = zip(news,desc,img,url)
    return render_template('cnn.html', context = mylist)

@app.route('/cnbc')
def cnbc():
    newsapi = NewsApiClient(api_key= "32fc0e644efb4220b4d655e0ff7a2eb1")
    topheadlines = newsapi.get_top_headlines(sources="cnbc")
    articles = topheadlines['articles']
    desc = []
    news = []
    img = []
    url = []
    for i in range(len(articles)):
        myarticles = articles[i]
        url.append(myarticles['url'])
        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
    mylist = zip(news,desc,img,url)
    return render_template('cnbc.html', context = mylist)

@app.route('/bbc')
def bbc():
    newsapi = NewsApiClient(api_key= "32fc0e644efb4220b4d655e0ff7a2eb1")
    topheadlines = newsapi.get_top_headlines(sources="bbc-news")
    articles = topheadlines['articles']
    desc = []
    news = []
    img = []
    url = []
    for i in range(len(articles)):
        myarticles = articles[i]
        url.append(myarticles['url'])
        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
    mylist = zip(news,desc,img,url)
    return render_template('bbc.html', context = mylist)

@app.route('/espn')
def espn():
    newsapi = NewsApiClient(api_key= "32fc0e644efb4220b4d655e0ff7a2eb1")
    topheadlines = newsapi.get_top_headlines(sources="espn")
    articles = topheadlines['articles']
    desc = []
    news = []
    img = []
    url = []
    for i in range(len(articles)):
        myarticles = articles[i]
        url.append(myarticles['url'])
        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
    mylist = zip(news,desc,img,url)
    return render_template('espn.html', context = mylist)

@app.route('/reuters')
def reuters():
    newsapi = NewsApiClient(api_key= "32fc0e644efb4220b4d655e0ff7a2eb1")
    topheadlines = newsapi.get_top_headlines(sources="reuters")
    articles = topheadlines['articles']
    desc = []
    news = []
    img = []
    url = []
    for i in range(len(articles)):
        myarticles = articles[i]
        url.append(myarticles['url'])
        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
    mylist = zip(news,desc,img,url)
    return render_template('reuters.html', context = mylist)

if __name__ == '__main__':
    app.debug = True
    app.run
