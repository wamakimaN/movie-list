from flask import Flask

# Initializing application
app = Flask(__name__,instance_relative_config = True)

from app import views
