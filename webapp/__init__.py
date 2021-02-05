from flask import Flask, render_template
from webapp.weather import get_weather
from webapp.vc_ru_news import get_python_news

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')

    @app.route('/')
    def index():
        news_list = get_python_news()
        weather = get_weather(app.config['WEATHER_DEFAULT_CITY'])
        return render_template('index.html', weather=weather, news_list=news_list)

    return app

