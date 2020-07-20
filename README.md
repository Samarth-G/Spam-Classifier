# Spam Classifier

Spam/Ham classification through ML <br>
Python : <b>Sklearn - Multinomial Naive Bayes</b>

## Overview

<i>[BaseCode.ipynb](BaseCode.ipynb) </i>- Contains the code to train and test the classifier and vectorizer

<i>MNBclassifier.pkl</i> - Trained MultinomialNB model on spam data <br>
<i>CountVectorizer.pkl</i>- Fitted vectroizer to pre-process data

<i>[SpamClassifier.py](SpamClassifier.py)</i> - Ready to use spam classifier

## Usage

```bash
>>> python SpamClassifier.py
Spam Classifier
Enter text: Hey what's up?
-> Ham
>>>
```

## MNB Classifier
```python
from sklearn.metrics import classification_report 
print(classification_report(y_test, y_pred))

              precision    recall  f1-score   support

           0       0.99      0.98      0.99      1128
           1       0.88      0.93      0.90       165

    accuracy                           0.97      1293
   macro avg       0.93      0.96      0.94      1293
weighted avg       0.98      0.97      0.97      1293
```

```python
from sklearn.metrics import confusion_matrix
print("Confusion Matrix")
print(confusion_matrix(y_test, y_pred))

Confusion Matrix
[[1106   22]
 [  11  154]]
```
https://gist.github.com/Samarth-G/8511dfc5c750907d64245dcfddb181b0
