from flask import jsonify, current_app
from threading import Thread

from wiki.app import db
from wiki.app.api import api
from wiki.app.api.async_tasks import (
    async_clone_task,
    async_index_task,
    async_pull_task,
    async_delete_task,
    async_index_task
)


@api.route('/clone')
def clone():
    Thread(
        target=async_clone_task,
        args=(
            current_app.config['REMOTE_REPO_URL'],
            current_app.config['STATIC_DIRECTORY']
        )
    ).start()
    return jsonify({"status": "executed"})


@api.route('/pull')
def pull():
    Thread(target=async_pull_task).start()
    return jsonify({"status": "executed"})


@api.route('/delete')
def delete():
    Thread(target=async_delete_task).start()
    return jsonify({"status": "executed"})


@api.route('/index_records')
def index_records():
    Thread(
        target=async_index_task,
        args=(
            current_app._get_current_object(),
            db,
            current_app.config['STATIC_DIRECTORY']
        )
    ).start()
    return jsonify({"status": "executed"})