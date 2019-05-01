from flask_sqlalchemy import SQLAlchemy
from flask import Flask
# 配置数据库连接
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:990617.zxz@localhost/memory_card_db?charset=utf8&autocommit=true'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True






db = SQLAlchemy(app)