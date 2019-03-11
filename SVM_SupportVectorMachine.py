#SVM stands for support vector machine and it is used to classify
# SVM aims to maximize distance between the data and the separating line between two classes
# Similar in purpose to Naive Bayes
# We need training feautures and labels
# Then we fit the model
# Then we predict

from sklearn import svm

features_train = [[0,0], [1,1]]
labels_train = [0,1]

X = features_train
y = labels_train

clf = svm.SVC()
clf.fit(X,y)

pred clf.predict(feautures_test)

# Test accuracy_score
import numpy as np
from sklearn.metrics import accuracy_score
print(accuracy_score(labels_test, pred))

## Kernel: linear classifier to solve non-linear problems. Some kernels can be taken out of the box from Sklearn

#In this case we will use SVC (Support Vector classifier).
from sklearn import svc
clf = SVC(kernel = 'linear') #This will use a linear kernel. Other options include linear, poly, rbf, sigmoid, precomputed

## SVM C Parameter
# C controls trade-off between smooth decision boundary and classifying training points correctly. A larger C means it will get more training data correct (higher risk of overfitting)

## SVM Gamma Parameter
# Defines how far the influence of a single training example reaches
