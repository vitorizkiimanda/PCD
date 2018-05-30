from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import numpy as np

import pickle

from sklearn.metrics import confusion_matrix

data = pd.read_csv('tomatKematangan.csv')
#print(data)

train=data.sample(frac=0.8,random_state=200)
test= data.sample(frac=0.2,random_state=200)

kematanganTrain = train["kematangan"]
#print(kematangan)

train = train.drop(["kematangan"], axis=1)
#print(train)

model = RandomForestClassifier(max_depth=2, random_state=0)
model.fit(train,kematanganTrain)


######test
kematanganTest = test["kematangan"]
test=test.drop(["kematangan"], axis=1)


####predict
kematanganPredict = model.predict(test)  #nnti ini test : inputan baru
#print(kematanganPredict)


####confusion matrix
print(confusion_matrix(kematanganTest, kematanganPredict))




# save the model to disk
filename = 'modelTomat.sav'
pickle.dump(model, open(filename, 'wb'))


# load the model from disk
loaded_model = pickle.load(open(filename, 'rb'))
kematanganPredict = loaded_model.predict(test)  #nnti ini test : inputan baru
print(kematanganPredict)
