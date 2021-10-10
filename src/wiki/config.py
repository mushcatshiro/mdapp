import os

from dotenv import load_dotenv
from flask import Flask


load_dotenv()
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    PROJECT_NAME = 'RANDOM_PROJECT_NAME'
    CONFIG_NAME = 'base'
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'R4nd0MS3cret'
    BASEDIR = basedir
    REMOTE_REPO_URL = os.environ.get('REMOTE_REPO_URL')
    STATIC_DIRECTORY = os.path.join(basedir, 'app', 'static')

    @staticmethod
    def init_app(app):
        pass

class POCConfig(Config):
    CONFIG_NAME = 'POC'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///poc.db'

    @classmethod
    def init_app(cls, app: Flask):
        Config.init_app(app)

        import logging
        from flask.logging import default_handler

        app.logger.removeHandler(default_handler)
        app.logger.setLevel(logging.INFO)

        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        
        logfile_handler = logging.FileHandler(
            os.path.join(
                cls.BASEDIR,
                f'{cls.CONFIG_NAME}-{cls.PROJECT_NAME}.log'
            )
        )
        logfile_handler.setFormatter(formatter)
        logfile_handler.setLevel(logging.INFO)
        app.logger.addHandler(logfile_handler)


config = {
    'default': POCConfig
}