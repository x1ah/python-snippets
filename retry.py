#!/usr/bin/env python
# encoding: utf-8

"""
retry function n times while run fail
"""

import requests


def retries(times=3):
    def wrap(func):
        def r(*args, **kw):
            t = 0
            while t < times:
                try:
                    func(*args, **kw)
                except requests.exceptions.ConnectTimeout:
                    t += 1
                else:
                    return
        return r
    return wrap


@retries(times=4)
def fetch_google():
    print('retry')
    resp = requests.get('https://google.com', timeout=0.1)
    return resp


if __name__ == "__main__":
    fetch_google()
