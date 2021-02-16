from flask import render_template, Blueprint, current_app, abort, flash, Request, url_for, redirect
from webapp.news.models import News, Comment
from webapp.weather import get_weather
from webapp.news.forms import Comment_form
from flask_login import current_user, login_required
from webapp.db import db

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
    comment_form = Comment_form(news_id=my_news.id)
    return render_template('news/single_news.html', page_title=my_news.title, news=my_news, comment_form=comment_form)


@blueprint.route('/news/comment', methods=['POST'])
@login_required
def add_comment():
    form = Comment_form()
    if form.validate_on_submit():
        comment = Comment(text=form.comment_text.data, news_id=form.news_id.data, user_id=current_user.id)
        db.session.add(comment)
        db.session.commit()
        flash('Комментарий успешно добавлен')
    else:
        for field, errors in form.errors.items():
            for error in errors:
                flash('ошибка в поле {}: {}'.format(getattr(form, field).label.text, error))
    return redirect(Request.referrer)
