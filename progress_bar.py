#!/usr/bin/env python
# encoding: utf-8
"""
进度条
"""

import sys
import time

TOTAL = 100


def precent_progress():
    for i in range(TOTAL):
        time.sleep(0.1)
        sys.stdout.write("{}/{}\r".format(i, TOTAL))
        sys.stdout.flush()


def circle_progress():
    item = ['-', '\\', '|', '/']
    for i in range(TOTAL):
        time.sleep(0.1)
        sys.stdout.write(item[i % 4] + '\r')
        sys.stdout.flush()


if __name__ == "__main__":
    circle_progress()

