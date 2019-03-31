__author__ = 'Ran'

from flask import Flask  # flask
from flask_sqlalchemy import SQLAlchemy  # sql
from flask_login import LoginManager
from app import config  # config
from flask_caching import Cache
from datetime import timedelta

#实例化app
app = Flask(__name__)

#引入全局配置
app.config.from_object(config)

#配置flasklogin
login_manager = LoginManager()
login_manager.session_protection = None
login_manager.login_view = ''
login_manager.init_app(app=app)

#跨域密匙
app.secret_key = '\x12my\x0bVO\xeb\xf8\x18\x15\xc5_?\x91\xd7h\x06AC'

#绑定对象
db = SQLAlchemy(app)

#创建数据库
#db.create_all()

#配置缓存
cache = Cache(app, config={'CACHE_TYPE': 'simple'})
cache.init_app(app, config={'CACHE_TYPE': 'simple'})