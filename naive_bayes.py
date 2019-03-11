import numpy as np
from sklearn.naive_bayes import GaussianNB

t0 = time() #Measure how much time it takes
clf = GaussianNB()
clf.fit(features_train, labels_train)
print "training time:", round(time()-t0,3),"s"

pred = clf.predict(features_test)
print "predict time:", round(time()-t0,3),"s"


from sklearn.metrics import accuracy_score
acc_score = accuracy_score(labels_test,pred)
print acc_score
