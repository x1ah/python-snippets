# coding: utf-8

from flask_skeleton.views import second_bp


@second_bp.route('/test')
def test_s():
    return 'test'
