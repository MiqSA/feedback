# -*- coding: utf-8 -*-

from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap

# config import
from config import app_config, app_active

config = app_config[app_active]


def create_app(config_name):
    app = Flask(__name__, template_folder='templates')

    app.secret_key = config.SECRET
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')

    Bootstrap(app)

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/register/')
    def register():
        return render_template('register.html')

    @app.route('/register/', methods=['POST'])
    def register_post():
        number = int(request.form['number'])
        return render_template('register.html', number=number)

    return app
