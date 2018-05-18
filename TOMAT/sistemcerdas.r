#####################################
###decision tree : dibawah + randomForest + randomForest
#membagi data
library(readxl)
tomat <- read_excel("E:/VRI/IPB/kuliah/Sem6/PCD/PCD/TOMAT/tomatKematangan.xlsx")
tomat$kematangan <- as.factor(tomat$kematangan)
set.seed(1234)#ini buat ngerandom
ind <- sample(2, nrow(tomat), replace=TRUE, prob=c(0.7,0.3))#ini buat misahin data ke n data -> 2 kalo disini : 70% 30%
trainData <- tomat[ind==1,] # kode 1 buat 0.7 -> 70%
testData <- tomat[ind==2,] # ini buat 0.3 -> 30%

#partykit Library -> menggunakan nilai statistik 
library(partykit)
modelctree <- ctree(kematangan ~ .,data = trainData) #Species = class ,,  . = semua atribut kita pake
predctree <- predict(modelctree, testData[,-4]) # -5 = apus atribut ke-5
table(predctree, testData$kematangan)
plot(predctree, testData$kematangan)

#rpart library -> menggunakan nilai bias
library(rpart)
modelrpart <- rpart(kematangan ~ .,data = trainData)
predrpart <- predict(modelrpart, type="class", testData[,-4])
table(predrpart, testData$kematangan)
plot(predrpart)

#SVM
#e1071 library
library(e1071)
svm.model <- svm(kematangan ~ .,data = trainData, cost = 100, gamma =1)
svm.pred <- predict(svm.model, testData[,-4])
table(pred = svm.pred, true = testData[,4])
plot(svm.pred, testData$kematangan)

#tambahan
#confusion matrix= library caret
library(caret)
confusionMatrix(svm.pred, testData$kematangan)

###note
# ?"namafungsi"   -> untuk summon help
# help("namafungsi")   -> untuk summon help

