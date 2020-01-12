import pandas as pd

weather_data = pd.read_csv("unified/flight_date_fixed.csv", dtype='unicode')

weather_data['TIME'] = weather_data['TIME'].str.rjust(4, '0')

weather_data.to_csv("flight_date_fixed.csv", index=False)