import sklearn
from sklearn import tree
#Supervised Learning
features = [[70, 1], [80, 1], [155, 0], [110, 0],[160, 0],[95, 1],[105, 1], [115, 1]]

#apple 70-120grams
#orange 100-160grams
#1 = smooth
#0 - bumpy

labels = [0, 0, 1, 1, 1, 0, 0, 0]
#0 = apple
#1 = orange

#Decision Tree
clf = tree.DecisionTreeClassifier()

# fit = training algorithm  fit = Finding Patterns in Data
clf = clf.fit(features, labels)

print clf.predict([[160, 0]]) # Expected 1 for orange
print clf.predict([[155, 0]]) # Expected 1 for orange
print clf.predict([[127, 1]]) # Expected 0 for apple
print clf.predict([[100, 1]]) # Expected 0 for apple
print clf.predict([[85, 1]])  # Expected 0 for apple
print clf.predict([[109,1]])  # Expected 0 for apple
