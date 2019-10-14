import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import re
from pandas import DataFrame
from sklearn import linear_model
from statistics import mean, median,variance,stdev

X_edarabonConc = pd.DataFrame([0.01, 0.02, 0.03, 0.04, 0.05])
Y_absorbance = pd.DataFrame([0.1087, 0.2205, 0.3340, 0.4418, 0.5470])
x = np.array([0.01, 0.02, 0.03, 0.04, 0.05])
y = np.array([0.1087, 0.2205, 0.3340, 0.4418, 0.5470])

model = linear_model.LinearRegression()
model.fit(X_edarabonConc, Y_absorbance)

px = np.arange(min(x), max(y), 0.0001)[:, np.newaxis]
py = model.predict(px)

a = model.coef_
b = model.intercept_
Sx = stdev(x)
Sy = stdev(y)
cov = lambda item1, item2: sum([(i[0]-sum(item1)/len(item1)) * (i[1]-sum(item2)/len(item2)) for i in zip(item1, item2)]) / len(item1)
Sxy = cov(x, y)
R = Sxy/(Sx*Sy)

print("slope:a=" + str(a))
print("section:b=" + str(b))
print("standard_deviaton:Sx=" + str(Sx) + ", Sy=" + str(Sy))
print("covariance:Sxy=" + str(Sxy))
print("correlation_coeffcient_squared:R^2=" + str(R**2))

