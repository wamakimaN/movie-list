from flask import render_template
from app import app


@app.route('/')
def index():
    """
    view root page function that returns the index page and its data
    """
    