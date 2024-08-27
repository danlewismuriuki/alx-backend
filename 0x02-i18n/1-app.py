from flask import Flask, render_template
from flask import request
from flask_babel import Babel


"""
1-app.py
--------

This Flask application demonstrates how to integrate
    Flask-Babel for internationalization (i18n).
It includes the setup for locale and timezone configurations,
    as well as basic route handling.

Requirements:
- Flask
- Flask-Babel

Configuration:
- Supported Languages: English ('en') and French ('fr')
- Default Locale: English ('en')
- Default Timezone: UTC

Setup:
1. Install Flask and Flask-Babel:
   $ pip3 install flask flask_babel

2. Run the application:
   $ flask --app 1-app run
"""


app = Flask(__name__)

babel = Babel(app)


# @babel.localeselector
def get_locale():
    """
    Determine the best match for the user's preferred language
    from the list of supported languages.

    Returns:
        str: The best match locale.
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


babel.locale_selector_func = get_locale


@app.route("/")
def hello_world():
    """
    Route handler for the root URL ('/').

    Returns:
        str: Rendered HTML template '1-index.html'.
    """
    return render_template('./1-index.html')


if __name__ == '__main__':
    """
    Run the Flask application with debug mode enabled.
    """
    app.run(debug=True)
