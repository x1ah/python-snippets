# coding: utf-8

from flask import Flask

from flask_skeleton.views import (
    first_bp, second_bp, third_bp
)


app = Flask(__name__)

app.register_blueprint(first_bp, url_prefix='/first')
app.register_blueprint(second_bp, url_prefix='/second')
app.register_blueprint(third_bp, url_prefix='/third')


@app.before_request
def before_request():
    # do sth before app request
    pass


if __name__ == "__main__":
    app.run()
