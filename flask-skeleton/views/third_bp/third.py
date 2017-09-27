# coding: utf-8

from flask_skeleton.views import third_bp


@third_bp.route('/test')
def test_t():
    return 'test'
