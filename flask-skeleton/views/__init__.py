# coding: utf-8

from flask import g, Blueprint


first_bp = Blueprint('first_bp', __name__, template_folder='templates/first', static_folder='static')
second_bp = Blueprint('second_bp', __name__, template_folder='templates/second', static_folder='static')
third_bp = Blueprint('third_bp', __name__)


@first_bp.before_request
def first_bp_before_request():
    # do sth in this blueprint
    pass


__all__ = [
    'first_bp',
    'second_bp',
    'third_bp'
]


import flask_skeleton.views.first_bp
import flask_skeleton.views.second_bp
import flask_skeleton.views.third_bp
