from datetime import datetime as dt
from flask_sqlalchemy import SQLAlchemy
from git import Repo
import logging
import os
import shutil
import json


from wiki.app.model import FRecord


logger = logging.getLogger(__name__)


def async_clone_task(remote_repo_url, static_path):
    if not os.path.exists(static_path): 
        Repo.clone_from(
            remote_repo_url,
            static_path
        )
    logger.info(f"clonning completed at {dt.now()}")


def async_pull_task(static_path):
    Repo(
        os.path.join(static_path, ".git")
    ).remote('origin').pull()


def async_delete_task(static_path):
    shutil.rmtree(static_path)


def async_index_task(app, db: SQLAlchemy, static_path):
    """
    go through entire static_path except .git/
    identify all files and parent dir
    for each file to store to db
    table id, parent dir, fname
    """
    records = []
    for root, dirs, files in os.walk(static_path):
        for file in files:
            if '.git' not in root\
                and '.git' not in file\
                and file.endswith('.md'):
                records.append((root, file))
    logger.info(records)
    with app.app_context():
        table_exists = db.session.execute(
            """
            SELECT name 
            FROM sqlite_master 
            WHERE type ='table'
                AND name NOT LIKE 'sqlite_%'
                AND name = 'frecord'
            """
        ).fetchone()
        logger.info(table_exists)
        if not table_exists:
            logger.error('table does not exists')
            raise Exception
        for record in records:
            entry = FRecord.query.filter_by(fname=record[1]).first()
            if not entry:
                d = {
                    'parent_dir': record[0],
                    'fname': record[1]
                }
                frecord = FRecord(**d)
                db.session.add(frecord)
                db.session.commit()
                logger.info(f'inserted entry: {json.dumps(d)}')
            else:
                logger.info('record exists in database')