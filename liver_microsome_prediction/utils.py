"""Utility module

Utility functions or classes are defined here.
"""

from liver_microsome_prediction.common import *

from scipy import stats


def process_targets(df, targets, prefix='boxcox_'):
    for target in targets:
        min_pos    = df[df[target] > 0][target].min()
        df[target] = df[target].clip(min_pos, 100)
        df[prefix+target], _ = stats.boxcox(df[target])
    return df
