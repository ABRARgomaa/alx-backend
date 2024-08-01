#!/usr/bin/env python3
"""
app module
"""

from flask import Flask, render_template, request, g
from flask_babel import Babel, timezone as babel_timezone
import pytz

app = Flask(__name__)


class Config:
    """
    configure langs
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


@babel.localeselector
def get_locale():
    """
    get locale method
    """
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    if g.user and g.user.get('locale') in app.config['LANGUAGES']:
        return g.user['locale']
    return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user():
    """
    get_user function
    """
    user_id = request.args.get('login_as')
    if user_id:
        try:
            user_id = int(user_id)
            return users.get(user_id)
        except ValueError:
            pass
    return None


@app.before_request
def before_request():
    """
    befor_request function
    """
    g.user = get_user()


@babel.timezoneselector
def get_timezone():
    """
    get timezone method
    """
    timezone = request.args.get('timezone')
    if timezone:
        try:
            pytz.timezone(timezone)
            return timezone
        except pytz.UnknownTimeZoneError:
            pass

    if g.user and g.user.get('timezone'):
        try:
            pytz.timezone(g.user['timezone'])
            return g.user['timezone']
        except pytz.UnknownTimeZoneError:
            pass

    return app.config['BABEL_DEFAULT_TIMEZONE']


@app.route('/')
def index():
    """
    index method
    """
    return render_template('./7-index.html')


if __name__ == '__main__':
    app.run(debug=True)
