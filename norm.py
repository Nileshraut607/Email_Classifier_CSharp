import os
from sklearn import *
from collections import Counter
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split as tts
from sklearn.metrics import accuracy_score
import _pickle as c

def save(clf, name):
    with open(name, 'wb') as fp:
        c.dump(clf, fp)
    print ("saved")


def make_dict():
    direc = "emails/"
    files = os.listdir(direc)
    emails = [direc + email for email in files]
    words = []
    c = len(emails)
    for email in emails:
        f = open(email,encoding="latin-1")
        blob = f.read()
        words += blob.split(" ")
        print (c)
        c -= 1

    for i in range(len(words)):
        if not words[i].isalpha():
            words[i] = ""

    dictionary = Counter(words)
    del dictionary[""]
    return dictionary.most_common(3000)


def make_dataset(dictionary):
    direc = "emails/"
    files = os.listdir(direc)
    emails = [direc + email for email in files]
    feature_set = []
    labels = []
    c = len(emails)

    for email in emails:
        data = []
        f = open(email,encoding="latin-1")
        words = f.read().split(' ')
        for entry in dictionary:
            data.append(words.count(entry[0]))
        feature_set.append(data)

        if "ham" in email:
            labels.append(0)
        if "spam" in email:
            labels.append(1)
        print (c)
        c = c - 1
    return feature_set, labels


d = make_dict()
features, labels = make_dataset(d)

x_train, x_test, y_train, y_test = tts(features, labels, test_size=0.2)

clf = MultinomialNB()
clf.fit(x_train, y_train)

preds = clf.predict(x_test)
print (accuracy_score(y_test, preds))
save(clf, "text-classifier.mdl")

def load(clf_file):
    with open(clf_file, 'rb') as f:
        lines = [x.decode('latin-1').strip() for x in f.readlines()]
    return lines

lines = load("text-classifier.mdl")


while True:
    features = []
    inp = input(">").split()
    if inp[0] == "exit":
        break
    for word in d:
        features.append(inp.count(word[0]))
    res1 = clf.predict([features])
    print (res1)
