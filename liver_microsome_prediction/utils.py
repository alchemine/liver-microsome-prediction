"""Utility module

Utility functions or classes are defined here.
"""

from liver_microsome_prediction.common import *

from scipy import stats
from sklearn.compose import make_column_transformer
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer


# def process_targets(df, targets, prefix='boxcox_'):
#     for target in targets:
#         min_pos    = df[df[target] > 0][target].min()
#         df[target] = df[target].clip(min_pos, 100)
#         df[prefix+target], _ = stats.boxcox(df[target])
#     return df

num_pipeline = make_pipeline(
    SimpleImputer(),
    StandardScaler()
)

def get_num_preprocessor():
    return make_column_transformer(
        (num_pipeline, ['AlogP', 'Molecular_Weight', 'Num_H_Acceptors', 'Num_H_Donors', 'Num_RotatableBonds', 'LogD', 'Molecular_PolarSurfaceArea']),
        remainder='drop'
    )
