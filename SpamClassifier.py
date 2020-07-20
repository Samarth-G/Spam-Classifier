import joblib

loaded_classifier = joblib.load('MNBclassifier.pkl')
loaded_cv = joblib.load('CountVectorizer.pkl')

print("Spam Classifier")
value = [input("Enter text: ")]
value = loaded_cv.transform(value).toarray()

if loaded_classifier.predict(value) == [0]:
    print("-> Ham")
else:
    print("-> Spam")