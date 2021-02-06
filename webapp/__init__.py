from flask import Flask, render_template
from webapp.weather import get_weather
from webapp.model import db, News




def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)

    @app.route('/')
    def index():
        news_list = News.query.order_by(News.published.desc()).all()
        weather = get_weather(app.config['WEATHER_DEFAULT_CITY'])
        return render_template('index.html', weather=weather, news_list=news_list)

    return app
