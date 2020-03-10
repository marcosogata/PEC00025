import numpy as np
import matplotlib.pyplot as plt
from MRPy import MRPy

X = MRPy.from_file(test.invh)

X.attributes()
X.plot_time()