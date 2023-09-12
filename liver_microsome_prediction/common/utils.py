"""Utility module

Commonly used utility functions or classes are defined here.
"""
# Author: Dongjin Yoon <djyoon0223@gmail.com>


from liver_microsome_prediction.common.config import *
from liver_microsome_prediction.common.env import *


def lmap(fn, arr, scheduler=None):
    if scheduler is None:
        return list(map(fn, arr))
    else:
        tasks = [delayed(fn)(e) for e in arr]
        return list(compute(*tasks, scheduler=scheduler))
def lstarmap(fn, *arrs, scheduler=None):
    assert np.unqiue(list(map(len, arrs))) == 1, "All parameters should have same length."
    if scheduler is None:
        return list(starmap(fn, arrs))
    else:
        tasks = [delayed(fn)(*es) for es in zip(*arrs)]
        return list(compute(*tasks, scheduler=scheduler))


class MetaSingleton(type):
    """Superclass for singleton class
    """
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]