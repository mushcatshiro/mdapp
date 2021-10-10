from flask import current_app, render_template, abort, request
import re
import os

from wiki.app import db
from wiki.app.model import FRecord
from wiki.app.main import main


@main.route('/')
def index():
    titles = FRecord.query.all()  
    return render_template('index.html', titles=titles)


@main.route('/page/<fname>')
def page(fname):
    if not fname.endswith('.md'):
        fname = fname + '.md'
    record = FRecord.query.filter_by(fname=fname).first()
    if record:
        current_app.logger.info(record)
        content_full_dir = os.path.join(record.parent_dir, record.fname)
        with open(content_full_dir, 'r') as rf:
            content = rf.read()
            # ![img](images/img.PNG)
            content = re.sub(
                r'(\!\[.+\]\()(images)(/.+\))',
                r'\1../static/\2\3',
                content
            )
        return render_template('page.html', content=content)
    else:
        abort(404)


@main.route('/search', methods=['POST'])
def search():
    fname = request.form['search']
    if not fname.endswith('.md'):
        fname = fname + '.md'
    record = FRecord.query.filter_by(fname=fname).first()
    if record:
        current_app.logger.info(record)
        content_full_dir = os.path.join(record.parent_dir, record.fname)
        with open(content_full_dir, 'r') as rf:
            content = rf.read()
            # ![img](images/img.PNG)
            content = re.sub(
                r'(\!\[.+\]\()(images)(/.+\))',
                r'\1../static/\2\3',
                content
            )
        return render_template('page.html', content=content)
    else:
        abort(404)