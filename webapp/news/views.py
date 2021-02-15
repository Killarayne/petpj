from flask import render_template, Blueprint, current_app, abort
from webapp.news.models import News
from webapp.weather import get_weather

blueprint = Blueprint('news', __name__)


@blueprint.route('/')
def index():
    news_list = News.query.filter(News.text.isnot(None)).order_by(News.published.desc()).all()
    weather = get_weather(current_app.config['WEATHER_DEFAULT_CITY'])
    return render_template('news/index.html', page_title='Новости', weather=weather, news_list=news_list)


@blueprint.route('/news/<int:news_id>')
def single_news(news_id):
    my_news = News.query.filter(News.id == news_id).first()
    if not my_news:
        abort(404)
    return render_template('news/single_news.html', page_title=my_news.title, news=my_news)
