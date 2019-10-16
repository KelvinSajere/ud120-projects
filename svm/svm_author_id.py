#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("./tools/")
from email_preprocess import preprocess
from sklearn import svm
from sklearn import tree


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()
print("This is the size of my features :",len(features_train))
# features_train = features_train[:round(len(features_train)/100)]
# labels_train = labels_train[:round(len(labels_train)/100)]
print("This is the size of my features :",len(features_train))

#########################################################
### your code goes here ###
t0 = time()
clf = svm.SVC(kernel="rbf", C=10000)
clf.fit(features_train,labels_train)
print ("Training time :: ",time()-t0)

pred= clf.predict(features_test)
print("Prediction result accuracy:", clf.score(features_test, labels_test))
print("The prediction of index 10 is: ", pred[10])
print("The prediction of index 26 is: ", pred[26])
print("The prediction of index 50 is: ", pred[50])
print("No. of predicted to be in the 'Chris'(1): %r" % sum(pred))
#########################################################


