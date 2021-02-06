import requests
from bs4 import BeautifulSoup
from datetime import datetime
from webapp.model import db, News


def get_html(url):
    try:
        result = requests.get(url)
        result.raise_for_status()
        return result.text
    except (requests.RequestException, ValueError):
        print('Сетевая ошибка')
        return False


def get_vc_news():
    html = get_html('https://vc.ru')
    if html:
        soup = BeautifulSoup(html, 'html.parser')
        all_news = soup.findAll('div', class_='news_item')
        for new in all_news:
            title = new.find('a').text
            url = new.find('a')['href']
            published = new.find('time').text
            try:
                published = datetime.strptime(published, '%y-%m-%d')
            except ValueError:
                published = datetime.now()
            save_news(title, url, published)


def save_news(title, url, published):
    news_exist = News.query.filter(News.url == url).count()
    print(news_exist)
    if not news_exist:
        news_news = News(title=title, url=url, published=published)
        db.session.add(news_news)
        db.session.commit()
