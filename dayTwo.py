import numpy as np
from sklearn import datasets
iris = datasets.load_iris()
digits = datasets.load_digits()
print(digits.images[0])