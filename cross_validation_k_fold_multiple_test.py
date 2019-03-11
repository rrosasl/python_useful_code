'''
#Cross validation (K-fold CV)

There's another option
Cross validation means that you do the train_test_split and running the algorithms multiple times. In that way you use ALL your data for learning and ALL your data for testing. It will take longer to train but it will give you better accuracy
'''

from sklearn.model_selection import KFold
obs_number = len(df) #How many observations you have
fold_num = 2 #How many 'folds' there will be
kf = KFold(obs_number, fold_num, shuffle=True) #fold_num is how many folds you want to look at. this will gilve you x = fold_num e.g. 2 lists. one with the indicies of all the data points that you will use on your training and testing data set.
#If you don't put shuffle=True then it will give you horrible results as it will separate the data without shuffling, which may be very inconvenient if there's a particular logic to the order of the data set
features = df.column_of_interest_X
labels = df.column_of_interest_Y
from sklearn import tree

for train_indices, test_indices in kf:
    features_train = [features[ii] for ii in train_indices]
    fetures_test = [features[ii] for ii in test_indices
    labels_train = [labels[ii] for ii in train_indices]
    labels_test = [lables[ii] for ii in test_indices]

    #Example using Decision tree but it can be any algorithm
    clf = tree.DecisionTreeClassifier()
    clf.fit(features_train,labels_train)
    pred = clf.predict(features_test)
