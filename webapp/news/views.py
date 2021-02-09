from flask import render_template, Blueprint, current_app
from webapp.news.models import News
from webapp.weather import get_weather


blueprint = Blueprint('news', __name__)


@blueprint.route('/')
def index():
    news_list = News.query.order_by(News.published.desc()).all()
    weather = get_weather(current_app.config['WEATHER_DEFAULT_CITY'])
    return render_template('news/index.html', weather=weather, news_list=news_list)
