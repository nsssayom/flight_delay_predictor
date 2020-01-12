import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor


import matplotlib.pyplot as plt

data = pd.read_csv("dataset/dataset.csv").sample(frac = 0.1)
X = data[['DayOfYear','DewPoint','Temperature','RelativeHumidity','Pressure','Windspeed']].values  # independent columns
y = data[['WEATHER_DELAY']].values  # target column i.e price range

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

print('Training Features Shape:', X_train.shape)
print('Training Labels Shape:', y_train.shape)
print('Testing Features Shape:', X_test.shape)
print('Testing Labels Shape:', y_test.shape)

rf = RandomForestRegressor(n_estimators = 1000, random_state = 42)
rf.fit(X_train, y_train.ravel())

y_pred = rf.predict(X_test)

errors = abs(y_pred - y_test)
print('Mean Absolute Error:', round(np.mean(errors), 2), 'degrees.')

# Calculate mean absolute percentage error (MAPE)
if (y_test > 0):
    mape = 100 * (errors / y_test)
    # Calculate and display accuracy
    accuracy = 100 - np.mean(mape)
print('Accuracy:', round(accuracy, 2), '%.')

# data_df = {
#     'test' : y_test.flatten(),
#     'pred' : y_pred.flatten(),
# }

# df = pd.DataFrame(data_df)
# df.to_csv("result.csv")