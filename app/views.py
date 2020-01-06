from flask import render_template
from app import app
from .request import get_sources

@app.route('/')
def index():
    """
    view root page function that returns the index page and its data
    """
    cnn_news = get_sources("cnn")

    return render_template('index.html',cnn = cnn_news)
    