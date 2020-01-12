import warnings

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sb
import xgboost as xgb
from keras.callbacks import ModelCheckpoint
from keras.layers import Activation, Dense, Flatten
from keras.models import Sequential
from matplotlib import pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier, XGBRegressor
import pickle


warnings.filterwarnings('ignore')
warnings.filterwarnings('ignore', category=DeprecationWarning)

data = pd.read_csv("dataset/dataset.csv").sample(frac = 1)

print (data.describe())
print (data.head())
print (data.shape)
print (data.info())

feature_names = ['DayOfYear','DewPoint','Temperature','RelativeHumidity','Pressure','Windspeed']

X = data[['DayOfYear','DewPoint','Temperature','RelativeHumidity','Pressure','Windspeed']].values  # independent columns
y = data[['WEATHER_DELAY']].values  # target column i.e price range

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)

data_dmatrix = xgb.DMatrix(data=X_train,label=y_train,)

xg_reg = xgb.XGBRegressor(objective ='reg:squarederror', colsample_bytree = 0.3, learning_rate = 0.1, max_depth = 5, alpha = 10, n_estimators = 10)
xg_reg.fit(X_train,y_train)
preds = xg_reg.predict(X_test)
with open('models/xgb.pkl', 'wb') as f:
    pickle.dump(xg_reg, f)

# data_df = {
#      'test' : y_test.flatten(),
#      'pred' : preds.flatten(),
# }

# df = pd.DataFrame(data_df)
# df.to_csv("result.csv")

rmse = np.sqrt(mean_squared_error(y_test, preds))
print("RMSE: %f" % (rmse))
params = {"objective":"reg:squarederror",'colsample_bytree': 0.3,'learning_rate': 0.1, 'max_depth': 5, 'alpha': 10}
cv_results = xgb.cv(dtrain=data_dmatrix, params=params, nfold=3, num_boost_round=50,early_stopping_rounds=10,metrics="rmse", as_pandas=True, seed=123)
print (cv_results.head())

xgb.plot_tree(xg_reg,num_trees=0)
plt.rcParams['figure.figsize'] = [5, 3]
plt.show()

#xgb.plot_importance(xg_reg).set_yticklabels(feature_names)
#plt.rcParams['figure.figsize'] = [5, 5]
#plt.show()