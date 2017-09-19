#!/usr/bin/env python
# encoding: utf-8
"""
进度条
"""

import sys
import time

TOTAL = 100

for i in range(TOTAL):
    time.sleep(0.1)
    sys.stdout.write("{}/{}\r".format(i, TOTAL))
    sys.stdout.flush()
