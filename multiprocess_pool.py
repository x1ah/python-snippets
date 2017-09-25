#!/usr/bin/env python
# encoding: utf-8

import multiprocessing

# 线程池
from multiprocessing.dummpy import Pool

# 进程池
# from multiprocessing import Pool

import requests

urls = [
    'http://x1ah.cn',
    'http://github.com',
    'http://baidu.com'
]

pool = Pool(multiprocessing.cpu_count() * 2)
pool.map(lambda url: requests.get(url), urls)
pool.close()
pool.join()
