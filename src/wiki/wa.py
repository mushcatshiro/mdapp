import flask
from wiki.app import create_app, db
from flask_migrate import Migrate
import click

app = create_app('default')
migrate = Migrate(app, db)


@app.cli.command()
@click.option('--message', required=True)
def setup(message):

    import flask_migrate
    flask_migrate.init()
    flask_migrate.migrate(message=message)
    flask_migrate.upgrade()