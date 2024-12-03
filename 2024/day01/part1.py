import numpy as np
import pandas as pd

input = pd.read_csv('2024/day01/input.txt', sep='   ', names=['seq1', 'seq2'])

print(np.sum(np.abs(np.sort(input['seq1']) - np.sort(input['seq2']))))