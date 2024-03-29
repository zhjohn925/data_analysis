############################################
# Sklearn (Machine Learning)
############################################

import sys, argparse
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.linear_model import LinearRegression

# generate data sets
from sklearn.datasets._samples_generator import make_blobs

if __name__ == "__main__" :
    parser = argparse.ArgumentParser() 
    ml_options = ['demo_data', 'svc', 'ensemble']
    parser.add_argument("ml_option", default='-', choices=ml_options, help="specify option of machine learning")
    args = parser.parse_args()

    ml_option = args.ml_option
    if ml_option in ["demo_data", "svc", "ensemble"] :
        X, y = make_blobs(n_samples=500, centers=3, cluster_std=1.2)
        type(X)    # <class 'numpy.ndarray'>
        type(y)    # <class 'numpy.ndarray'>
        X.shape    # (500, 2)
        y.shape    # (500, ) 
        X[:,0]     # returns the first column
        X[:,1]     # returns the second column
        plt.scatter(X[:, 0], X[:, 1], c=y, cmap='autumn')
        if ml_option == "demo_data" :
            plt.show()
        elif ml_option in ["svc", "ensemble"] :
            from sklearn.model_selection import train_test_split
            # The function splits the input data (X and y) into two subsets (X_train, y_train, and X_test, y_test) 
            # according to the specified test size.
            # You can then use X_train and y_train to train your machine learning model, and X_test (It is unseen data 
            # that the model has not encountered during training.) to evaluate its performance on unseen data, 
            # typically by measuring metrics like accuracy and etc.
            # X:  This is the input feature data
            # y:  This is the target variable or label data 
            # test_size: indicates that 33% of the data will be reserved for testing, and the 
            #            remaining 67% will be used for training.
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33)
            if ml_option == "svc" :
                from sklearn.svm import SVC
                mdl = SVC(gamma='auto')
                mdl.fit(X_train, y_train)
                y_predict = mdl.predict(X_test)
                acc = 100*np.sum(y_predict == y_test) / y_test.size
                print("Accuracy is :", acc, "%")
            else :  # ml_option == "ensemble" :
                from sklearn.ensemble import RandomForestClassifier
                mdl = RandomForestClassifier(n_estimators=20)
                mdl.fit(X_train, y_train)
                y_predict = mdl.predict(X_test)
                acc = 100*np.sum(y_predict == y_test) / y_test.size
                print("Accuracy is :", acc, "%")
        else :
            pass




