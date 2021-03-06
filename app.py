from flask import Flask
from controllers.api import route_api
from controllers.api.getToken import route_getToken
# app = Flask(__name__)

from appf import app

app.register_blueprint(route_api,url_prefix='/api')
app.register_blueprint(route_getToken,url_prefix='/getToken')


@app.route('/')
def hello_world():
    return 'Chen Xi 是只zhuzhu'


if __name__ == '__main__':
    app.run(

      port= 80,
             debug=True)
