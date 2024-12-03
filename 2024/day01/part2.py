import numpy as np
import pandas as pd

input = pd.read_csv('2024/day01/input.txt', sep='   ', names=['seq1', 'seq2'])

countMultiply = np.vectorize(lambda x: x * (input['seq2'] == x).sum())

products = countMultiply(input['seq1'])

print(products.sum())