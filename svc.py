import numpy as np
import pandas as pd
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.svm import SVC

data = pd.read_csv('dataset/dataset.csv').sample(frac = 0.01)
result = pd.DataFrame()
result['WEATHER_DELAY'] = data.iloc[:,6]
data = data.iloc[:,0:6]          

x_train, x_test, y_train, y_test = train_test_split(data.values, result.values, test_size = 0.2)      

svc = SVC()
svc.fit(x_train, y_train.ravel())
prediction = svc.predict(x_test)


data_df = {
     'test' : y_test.flatten(),
     'pred' : prediction.flatten(),
}

df = pd.DataFrame(data_df)
df.to_csv("result.csv")




cm = confusion_matrix(y_test, prediction)
sum = 0
for i in range(cm.shape[0]):
    sum += cm[i][i]
    
accuracy = sum/x_test.shape[0]                
print(accuracy)
