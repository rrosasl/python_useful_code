# Using decision trees

from sklearn import tree
x = [[0,0],[1,1]]
Y = [0,1] #From sklearn documentation

clf = tree.DecisionTreeClassifier()
clf = clf.fit(X,Y)

clf.predict(features_test)

# Min_samples_split
# Decision trees continues to split the data. Min samples split says determines what is the minimum of elements that need to be contained
clf = tree.DecisionTreeClassifier(Min_samples_split = 50) #Default is 2
clf = clf.fit(X,Y)

clf.predict(features_test)

"""
Entropy
Entropy controls how a decision tree decides where to split the data
Entropy def: Measure of impurity in a bunch of examples
IF all examples are the same class entroypy = 0, there's no impurity
If entroypy = 1, there's full impurity

Entropy formula: - Sum [pi * np.log2(pi)] where pi = fraction of elements in a class (e.g. if there's a sample of 4 and 2 are e.g. slow, pi = 0.5)

Information Gain
information gain = entropy(parent) - weighted average of entropy_children
"""
