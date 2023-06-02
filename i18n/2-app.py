#!/usr/bin/env python3
"""
i18n flask app
"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config(object):
    """
    Configuration Class for Babel
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


def get_locale():
    """
    Determine the best match with our supported languages.
    """
    return (request.args.get('locale')
            if request.args.get('locale') in app.config['LANGUAGES']
            else request.accept_languages.best_match(app.config['LANGUAGES']))


@app.route('/')
def index():
    """
    Rendering the inex.html file
    """
    return render_template('2-index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
