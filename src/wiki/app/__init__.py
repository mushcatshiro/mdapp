from flask import Flask, render_template
from flaskext.markdown import Markdown
from flask_sqlalchemy import SQLAlchemy
from wiki.config import config

db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    md = Markdown(app)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    db.init_app(app)

    from wiki.app.main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from wiki.app.api import api as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api')    

    register_error(app)

    return app


def register_error(app):
    @app.errorhandler(400)
    def bad_request(e):
        return render_template('error.html', error='bad request'), 400

    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('error.html', error='page not found'), 404

    @app.errorhandler(500)
    def internal_server_error(e):
        return render_template('error.html', error='internal server error'), 500
    
    @app.errorhandler(401)
    def unauthorized_error(e):
        return render_template('error.html', error='unauthorized'), 401