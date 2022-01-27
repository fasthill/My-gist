from sklearn.metrics import classification_report

# mnistPred = model.predict_classes(x= mnistData) # => predicr_classes 없어짐.
# mnistData : data dataframe, mnistLabels: label series
# model : pre-saved sequential model

mnistPred = model.predict(x = mnistData) 
mnistPred = np.argmax(mnistPred, axis=1)

print(classification_report(mnistLabels, mnistPred))
