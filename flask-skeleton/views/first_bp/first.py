# coding: utf-8

from flask_skeleton.views import first_bp


@first_bp.route('/test')
def test():
    return 'test'
