import os

from flask import Flask, Blueprint

from controllers.login import login
from controllers.referral_code import refcode
from controllers.signup import signup
from controllers.statement import statement
from database import migrate

app = Flask(__name__)

def register_blueprints():
    app.register_blueprint(signup)
    app.register_blueprint(refcode)
    app.register_blueprint(login)
    app.register_blueprint(statement)


if __name__ == '__main__':
    migrate()
    register_blueprints()
    app.run(
        host='0.0.0.0',
        debug=os.environ.get('FLASK_ENV', default='development') == 'development',
        port=int(os.environ.get("PORT", 5000))
    )
