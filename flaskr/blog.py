"""
Time : 2020/11/17 13:55 
Author : Lyh
File : blog.py 

"""
from flask import (
    Blueprint,flash,g,redirect,url_for,request,render_template,
)
from werkzeug.exceptions import abort
from flaskr.db import get_db
from flaskr.auth import login_required

bp = Blueprint("blog",__name__)

@bp.route('/')
def index():
    db = get_db()
    cursor = db.cursor()
    cursor.execute('SELECT p.id, title, body, created, author_id, username'
        ' FROM post p JOIN user u ON p.author_id = u.id'
        ' ORDER BY created DESC')
    posts = cursor.fetchall()  # 元组
    print(posts) # (1, '啊啊啊', '啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊', datetime.datetime(2020, 11, 17, 16, 57, 53), 3, 'bbb'),

    return render_template('blog/index.html',posts=posts)



@bp.route('/create', methods=('GET', 'POST'))
@login_required
def create():
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            cursor = db.cursor()
            cursor.execute(
                'INSERT INTO post (title, body, author_id)'
                ' VALUES (%s, %s, %s)',
                (title, body, g.user[4])
            )
            db.commit()
            return redirect(url_for('blog.index'))

    return render_template('blog/create.html')


