import pandas as pd
import datetime
flight_data = pd.read_csv("unified/weather.csv", dtype='unicode')
flight_data['DATETIME'] = flight_data['DATE'].astype(str) + " " + flight_data['TIME'].astype(str)

date_col = flight_data.pop("DATETIME")
flight_data.insert(0, date_col.name, date_col)

columns = ['DATE']
flight_data.drop(columns, inplace=True, axis=1)

columns = ['TIME']
flight_data.drop(columns, inplace=True, axis=1)

flight_data.to_csv("Weather_new.csv", index=False)