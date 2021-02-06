from webapp import create_app
from webapp.vc_ru_news import get_vc_news

app = create_app()
with app.app_context():
    get_vc_news()