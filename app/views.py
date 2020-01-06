from flask import render_template
from app import app
from .request import get_sources,get_news

@app.route('/')
def index():
    """
    view root page function that returns the index page and its data
    """
    bbc = "BBC"

    cnn = "CNN"

    cnbc = "CNBC"

    aljazeera = "Aljazeera"

    espn = "ESPN"

    bbc_sport = "BBC Sports"

    source_names = []


    source_names.append(bbc)
    source_names.append(cnn)
    source_names.append(cnbc)
    source_names.append(aljazeera)
    source_names.append(espn)
    source_names.append(bbc_sport)



    return render_template('index.html',bbc = bbc,cnn = cnn,cnbc = cnbc,aljazeera = aljazeera,espn = espn, bbc_sport = bbc_sport,source_names = source_names)