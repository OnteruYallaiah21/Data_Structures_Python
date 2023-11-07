
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import KFold, cross_val_score

from sklearn.tree import DecisionTreeRegressor, DecisionTreeClassifier


def find_optimal_depth(X, y, visualize=None):
    k_best = {}
    kf = KFold(n_splits=5, shuffle=True, random_state=44)
    for k in range(2, 200):
        model = DecisionTreeRegressor(max_depth=k)
        MSE = cross_val_score(model, X, y, scoring="neg_mean_squared_error", cv=kf)
        #k_best.update({np.sqrt(abs(np.mean(scores))): k})
        k_best.update({(np.mean(MSE)*-1): k})
        k_min = k_best[min(list(k_best.keys()))]
        #print(k_min )
        #print(max(list(k_best.keys())))
        #print(max(list(k_best.values())))
    if visualize:
        plt.figure(figsize=(15, 7))
        plt.errorbar(k_best.values(), k_best.keys(), fmt='o')
        plt.plot(k_best.values(), k_best.keys())
        plt.xlabel("Depth")
        plt.ylabel("Mean Squared Error")
        plt.savefig(visualize)
        plt.show()

    return k_min

# Try Regression Tree to predict Price
df = pd.read_csv('UsedCars.csv', usecols=['price', 'trim',	'isOneOwner',	'mileage',	'year',	'color',	'displacement',	'fuel',	'region',	'soundSystem',	'wheelType'])

X = df[['trim', 'isOneOwner',
        'mileage', 'year', 'color',
        'displacement', 'fuel', 'region',
        'soundSystem', 'wheelType']]

y = df['price']

# To convert all non numeric columns to numeric
#ListCatColumns
categorical_ix = X.select_dtypes(include=['object', 'bool']).columns

# List Num Columns
numerical_ix = X.select_dtypes(include=['int64', 'float64']).columns

# One-Hot Encoding Categorical Columns
x1_dummy = pd.get_dummies(X[categorical_ix], drop_first=True)

## Joining New dummified and Numerical columns
x_new = pd.concat([x1_dummy, X[numerical_ix]], axis=1, join='inner')

# print(x_new)
# x_new is all converted to dummy variables
X = x_new
#m use 5-fold to find max_depth and plot MSE vs Mex_depth
depth = find_optimal_depth(X, y, visualize="Homework7.png")
model = DecisionTreeRegressor(max_depth=depth)

model.fit(X, y)


#plt.figure(figsize=(10,8), dpi=150)
#plot_tree(model, feature_names=X.columns);
#plt.show()

score = model.score(X, y)
print("Best Choice of max_depth:", depth)
print("Model score accuracy", score)


