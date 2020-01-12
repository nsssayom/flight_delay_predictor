import pandas as pd

weather_data = pd.read_csv("unified/flight.csv", dtype='unicode')

date_col = weather_data.pop("WEATHER_DELAY")

weather_data.insert(9, date_col.name, date_col)

weather_data.to_csv("flight_new.csv", index=False)