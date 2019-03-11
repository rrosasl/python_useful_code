'''
GridSearchCV is a way of systematically working through multiple combinations of parameter tunes, cross-validating as it goes to determine which tune gives the best performance. The beauty is that it can work through many combinations in only a couple extra lines of code.
'''

#Example using SVM (support vector machine)
from sklearn.model_selection import grid_search

parameters = {'kernel':('linear', 'rbf'), 'C':[1,10]} #These parameters are only because it's SVM if it were e.g. a DecisionTreeClassifier it could be Min_samples_split

svr = svm.SVC()
clf = grid_search.GridSearchCV(svr,parameters)
clf.fit(features_train, labels_train)

clf.best_params_
