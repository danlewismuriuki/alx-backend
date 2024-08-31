#!/usr/bin/env python3
"""
A basic Flask application demonstrating localization with Flask-Babel.

This application is configured to support multiple languages
    (English and French).
It uses Babel to determine the user's preferred language and
    render the appropriate
language in the templates.

Usage:
    - Run this script to start the Flask server.
    - Access the root URL to view the localized content.
"""

from flask import Flask, render_template, request
from flask_babel import Babel, _
from flask import g
from typing import Union


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


@app.route('/', strict_slashes=False)
def index() -> str:
    """
    Render the home page with localized content.

    This route handler renders the '3-index.html' template, which displays
    localized content based on the user's preferred language.

    Returns:
        str: Rendered HTML template '3-index.html'.
    """
    return render_template('6-index.html')


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


if __name__ == '__main__':
    """
    Run the Flask application with debug mode enabled.

    The application starts a Flask web server on localhost
        with debug mode enabled,
    allowing you to view localization in action and develop interactively.
    """
    app.run(debug=True)
