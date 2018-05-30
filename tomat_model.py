from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import RandomForestRegressor

import pandas as pd
import numpy as np

import pickle

from sklearn.metrics import confusion_matrix

#import dataset
dataKematangan = pd.read_csv('tomatKematangan.csv')
dataBerat = pd.read_csv('tomatBerat.csv')

#split data test dan data train
trainKematangan=dataKematangan.sample(frac=0.8,random_state=200)
testKematangan= dataKematangan.sample(frac=0.2,random_state=200)

trainBerat=dataBerat.sample(frac=0.8,random_state=200)
testBerat= dataBerat.sample(frac=0.2,random_state=200)

#mengambil class dari dataset
kematanganTrain = trainKematangan["kematangan"]
beratTrain = trainBerat["berat"]

#memisahkan class dari dataset
trainKematangan = trainKematangan.drop(["kematangan"], axis=1)
trainBerat = trainBerat.drop(["berat"], axis=1)


#membuat model menggunakan random forest
modelKematangan = RandomForestClassifier(max_depth=10, random_state=0)
modelKematangan.fit(trainKematangan,kematanganTrain)

modelBerat = RandomForestRegressor(max_depth=20, random_state=0)
modelBerat.fit(trainBerat,beratTrain)


###### data test
kematanganTestAsli = testKematangan["kematangan"]
testKematangan=testKematangan.drop(["kematangan"], axis=1)

beratTestAsli = testBerat["berat"]
testBerat=testBerat.drop(["berat"], axis=1)


####prediksi data test menggunakan model random forest
kematanganPredict = modelKematangan.predict(testKematangan)  #nnti ini test : inputan baru
beratPredict = modelBerat.predict(testBerat)
print(beratPredict)
print(beratTestAsli)

####confusion matrix
print(confusion_matrix(kematanganTestAsli, kematanganPredict))




# save the model to disk
filename = 'modelTomatKematangan.sav'
pickle.dump(modelKematangan, open(filename, 'wb'))

filename = 'modelTomatBerat.sav'
pickle.dump(modelKematangan, open(filename, 'wb'))





# load the model from disk
loaded_model = pickle.load(open(filename, 'rb'))
kematanganPredict = loaded_model.predict(testKematangan)  #nnti ini test : inputan baru
#print(kematanganPredict)
