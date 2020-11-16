"""
@Time : 2020/11/16 11:31 
@Author : Lyh
@File : __init__.py.py
参考教程：https://dormousehole.readthedocs.io/en/latest/tutorial/factory.html

"""
import os
from flask import Flask

def create_app(test_config=None):
    # 创建应用实例
    app = Flask(__name__,instance_relative_config=True)
    # 进行初始配置
    app.config.from_mapping(
        SECKET_KEY = 'dev',
        DATABASE = os.path.join(app.instance_path,'flaskr.sqlite')
    )
    # 加载默认配置文件
    if test_config is None:
        app.config.from_pyfile('config.py',silent=True)
    else:
        # 用于测试
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/hello')
    def hello():
        return  "hello world"

    # 注册视图
    from . import auth
    app.register_blueprint(auth.bp)

    return app


