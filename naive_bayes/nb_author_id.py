#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 1 (Naive Bayes) mini-project. 

    Use a Naive Bayes Classifier to identify emails by their authors
    
    authors and labels:
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###

# let's see some of the emails, and learn a bit of python at the same time
#print features_train  # no idea what this is going to do...
 # ok so apparently the training set is a gigantic sparse set of arrays
 # the test set must of course be the same
 # and it doesn't look like I have access here to the original emails?!?
 # going looking for email_preprocess now...


from sklearn.naive_bayes import GaussianNB
clf = GaussianNB()
t0 = time() 
clf.fit(features_train, labels_train)
print "training time:", round(time()-t0, 3), "s"

t1 = time()
print(clf.predict(features_test))
print "prediction time:", round(time()-t1, 3), "s"

print(clf.score(features_test, labels_test))

#########################################################


