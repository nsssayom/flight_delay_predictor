import pandas as pd
import datetime
flight_data = pd.read_csv("unified/weather.csv", dtype='unicode')

flight_data['TIME'] = flight_data['TIME'].astype(str).str[:2] + ":" + flight_data['TIME'].astype(str).str[-2:] + ":00"

flight_data.to_csv("weather_time_fixed.csv", index=False)


import pandas as pd
import numpy as np
import datetime

flight_data = pd.read_csv("dataset/dataset.csv", dtype='unicode')

flight_data['DATETIME'] = pd.to_datetime(flight_data['DATETIME']).dt.dayofyear

flight_data.to_csv("dataset.csv", index=False)
