"""
@Time : 2020/11/16 11:31 
@Author : Lyh
@File : __init__.py.py
参考教程：https://dormousehole.readthedocs.io/en/latest/tutorial/factory.html

"""
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


def create_app(test_config=None):
    # 创建应用实例
    app = Flask(__name__, instance_relative_config=True)
    # 进行初始配置
    app.config.from_mapping(
        SECKET_KEY='dev',
        SESSION_TYPE="filesystem",
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost:3306/flask_demo'
    # 创建数据库对象
    # db = SQLAlchemy(app)

    # 加载默认配置文件
    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        # 用于测试
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/hello')
    def hello():
        return "hello world"

    # 注册数据库
    from . import db
    db.init_app(app)

    # 注册视图
    from . import auth
    app.register_blueprint(auth.bp)

    return app
