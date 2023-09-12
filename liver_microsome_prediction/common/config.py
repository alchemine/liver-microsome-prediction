"""Configuration module

Commonly used constant parameters are defined in capital letters.
"""
# Author: Dongjin Yoon <djyoon0223@gmail.com>

from os.path import abspath, dirname, join


class PATH:
    root   = dirname(dirname(dirname(abspath(__file__))))
    data   = join(root, "data")
    train  = join(data, 'train.csv')
    test   = join(data, 'test.csv')
    sample = join(data, 'sample_submission.csv')
