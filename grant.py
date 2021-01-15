import numpy as np
import scipy as sp
from scipy import optimize

def fit_func(x, a, b, c):
    return a*np.exp(x*b) + c
