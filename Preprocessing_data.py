import numpy as np
from sklearn.preprocessing import MinMaxScaler

weights = numpy.array([[115.],[140.],[175.]]) #the .s are because this code needs floats and not integers

rescaled_weight = scaler.fit_transform(weights)
scaler = MinMaxScaler()
