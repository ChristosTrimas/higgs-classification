import pandas as pd

from utils import *
from mlpnas import MLPNAS
from CONSTANTS import TOP_N


data = pd.read_csv('DATASETS/out.csv')
X = data.drop('labels', axis=1, inplace=False).values
y = data['labels']
# print(X.head())
# print(X.shape)
nas_object = MLPNAS(X, y)
data = nas_object.search()

get_top_n_architectures(TOP_N)
