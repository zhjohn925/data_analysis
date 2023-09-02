############################################
# Sklearn (Machine Learning)
############################################

from sklearn.linear_model import LinearRegression
# from sklearn.datasets._samples_generator import make_blobs
# from sklearn.model_selection import train_test_split
# from sklearn.svm import SVC
# from sklearn.ensemble import RandomForestClassifier

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

sns.set()
# generate some data
N = 30
x = np.arange(N)
type(x)                  # <class 'numpy.ndarray'>
len(x)                   # 30
x.shape                  # (30,) is one-dimension array
y = 4*x - 7 + (10*np.random.randn(N))
type(y)                  # <class 'numpy.ndarray'>
len(y)                   # 30 

# A scatter plot is a visual representation of how two variables 
# relate to each other. You can use scatter plots to explore the 
# relationship between two variables.
# plt.scatter(x, y)
# plt.show()

type(np.newaxis)         # <class 'NoneType'>
x2 = x[:, np.newaxis]    # gives two-dimension array    
x2[3][0]                 # 3
model = LinearRegression(fit_intercept=True)
model.fit(x[:, np.newaxis], y)
yfit = model.predict(x[:, np.newaxis])   # use same x to predict y, or different x to predict y 
plt.scatter(x, y)
plt.plot(x, yfit, color='red')
plt.show()



