#!/usr/bin/env python3
"""
A Basic flask application with localization
"""
from flask import Flask, render_template, request
from flask_babel import Babel, _


class Config(object):
    """
    Application configuration class
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


# Application and Babel Initialization
app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)

# Locale Selector Function


@babel.localeselector
def get_locale() -> str:
    """
    Determine the best match for the user's preferred language
    from the list of supported languages.

    Returns:
        str: The best match locale.
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])

# Route Handling


@app.route('/', strict_slashes=False)
def index() -> str:
    """
    Route handler for the root URL ('/').

    Returns:
        str: Rendered HTML template '3-index.html'.
    """
    return render_template('3-index.html')


# Running the Application
if __name__ == '__main__':
    """
    Run the Flask application with debug mode enabled.
    """
    app.run(debug=True)
