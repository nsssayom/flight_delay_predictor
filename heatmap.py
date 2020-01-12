import warnings
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sb
from keras.callbacks import ModelCheckpoint
from keras.layers import Activation, Dense, Flatten
from keras.models import Sequential
from matplotlib import pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor

warnings.filterwarnings('ignore')
warnings.filterwarnings('ignore', category=DeprecationWarning)

data = pd.read_csv("dataset/dataset.csv")
#X = data[['DATETIME','WBAN','DewPoint','Temperature','RelativeHumidity','Pressure','Visibility','WindDirection','WindSpeed']].values  # independent columns
#y = data[['WEATHER_DELAY']].values  # target column i.e price range

#X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

#columns = ['WBAN']
#data.drop(columns, inplace=True, axis=1)


C_mat = data.corr()
fig = plt.figure(figsize = (15,15))

sb.heatmap(C_mat, annot = True, fmt = '.1g', vmax = 1.0, square = True)
plt.show()
data.dropna()
print (data.describe())
