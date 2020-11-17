"""
Time : 2020/11/17 10:24 
Author : Lyh
File : auth2.py 

"""
"""
Time : 2020/11/16 16:25 
Author : Lyh
File : auth.py 
参考;https://dormousehole.readthedocs.io/en/latest/tutorial/views.html
"""
import functools

from flask import (
    Blueprint,flash,g,redirect,render_template,request,session,url_for
)
from werkzeug.security import check_password_hash,generate_password_hash


from flaskr.db2 import get_db

bp = Blueprint('auth',__name__,url_prefix='/auth')


@bp.route('/register',methods=('GET','POST'))
def register():
    print('a----------------')
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        cursor = db.cursor()
        error = None

        if not username:
            error = "UserName is required"
        elif not password:
            error = "Password= is required"

        elif cursor.execute('select id from user where username=%s', username):
            error = 'User {} is already registered.'.format(username)
        if error is None:
            cursor.execute("insert into user (username,password) values(%s,%s)",[username,generate_password_hash(password)])
            db.commit()
            return redirect(url_for('auth.login'))

        flash(error)

    return render_template('auth/register.html')

@bp.route('/login',methods=('GET','POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        cursor = db.cursor()
        error = None
        cursor.execute(
            'SELECT * FROM user WHERE username = %s', (username,)
        )
        user = cursor.fetchone()
        print(user)

        if user is None:
            error = 'Incorrect username.'
        elif not check_password_hash(user[2], password):
            error = 'Incorrect password.'

        if error is None:
            session.clear()
            session['user_id'] = user[0]
            return redirect(url_for('index'))

        flash(error)

    return render_template('auth/login.html')

@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        cursor = get_db().cursor()
        cursor.execute(
            'SELECT * FROM user WHERE id = %s', (user_id,)
        )
        g.user = cursor.fetchone()


@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

# 装饰器
def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))

        return view(**kwargs)

    return wrapped_view











