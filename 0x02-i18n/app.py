#!/usr/bin/env python3
"""
A basic Flask application demonstrating localization with Flask-Babel.
"""

from flask import Flask, render_template, request
from flask_babel import Babel, _, format_datetime
from flask import g
from typing import Union
import pytz
from pytz import UnknownTimeZoneError
from datetime import datetime


class Config(object):
    """
    Application configuration class for localization and timezone settings.

    This class defines the configuration settings for the Flask application,
    particularly those related to localization and timezone.

    Attributes:
        LANGUAGES (list): Supported languages for localization.
        BABEL_DEFAULT_LOCALE (str): Default locale for the application.
        BABEL_DEFAULT_TIMEZONE (str): Default timezone for the application.
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


# Application and Babel Initialization
app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user(user_id) -> Union[dict, None]:
    """
    Retrieve a user from the mock user table by user ID.
    """
    return users.get(user_id)


@babel.localeselector
def get_locale() -> str:
    """
    Determine the best match for the user's preferred language.

    This function uses the `accept_languages` attribute of the request object
    to determine the best match for the user's preferred language from the list
    of supported languages.

    Returns:
        str: The best-matched locale string, such as 'en' or 'fr'.
    """
    # Check if 'locale' parameter is in the request and is
    # a supported language
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale

    # Check user settings next
    if g.user and g.user['locale'] in app.config['LANGUAGES']:
        return g.user['locale']

    # Check request headers last
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone() -> str:
    """
    Determine the best match for the user's time zone.
    """
    timezone = request.args.get('timezone')
    if timezone:
        try:
            pytz.timezone(timezone)
            return timezone
        except UnknownTimeZoneError:
            pass

    if g.user and 'timezone' in g.user:
        user_timezone = g.user['timezone']
        try:
            pytz.timezone(user_timezone)
            return user_timezone
        except UnknownTimeZoneError:
            pass
    return 'UTC'


@app.route('/', methods=['GET'], strict_slashes=False)
def hello_world() -> str:
    """Renders a Basic Template for Babel Implementation"""
    timezone = get_timezone()
    tz = pytz.timezone(timezone)
    current_time = datetime.now(tz)
    current_time = format_datetime(datetime=current_time)
    return render_template("index.html", current_time=current_time)


@app.before_request
def before_request():
    """
    Function to be run before each request in the Flask app.
    """
    user_id = request.args.get('login_as')
    if user_id and user_id.isdigit():
        user_id = int(user_id)
        g.user = get_user(user_id)
    else:
        g.user = None


@babel.timezoneselector
def get_timezone() -> str:
    """
    1 Find timezone parameter in URL parameters
    2 Find time zone from user settings
    3 Default to UTC
    """
    try:
        if request.args.get("timezone"):
            timezone = request.args.get("timezone")
            tz = pytz.timezone(timezone)

        elif g.user and g.user.get("timezone"):
            timezone = g.user.get("timezone")
            tz = pytz.timezone(timezone)
        else:
            timezone = app.config["BABEL_DEFAULT_TIMEZONE"]
            tz = pytz.timezone(timezone)

    except pytz.exceptions.UnknownTimeZoneError:
        timezone = "UTC"

    return timezone


if __name__ == '__main__':
    """
    Run the Flask application with debug mode enabled.

    The application starts a Flask web server on localhost
        with debug mode enabled,
    allowing you to view localization in action and develop interactively.
    """
    app.run(debug=True)
