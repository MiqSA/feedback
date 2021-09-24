# -*- coding: utf-8 -*-

from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap

# config import
from config import app_config, app_active

from model.sendemail import enviar

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
        return render_template('register.html', number=0, group=None)

    @app.route('/register/', methods=['POST'])
    def register_post():
        number = int(request.form['number'])
        group = request.form['group']
        return render_template('register.html', number=number, group=group)

    @app.route('/answers/<num>', methods=['POST'])
    @app.route('/answers/')
    def answers(num=0):
        emails = []
        end_email = input('Email: ')
        senha = input('Senha: ')
        for i in range(int(num)):
            email = request.form['email'+str(i)]
            nome = request.form['name' + str(i)]
            enviar(email, nome, end_email, senha)
            emails.append(email)

        return render_template('answers.html', number=num, emails=emails)

    return app
