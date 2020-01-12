import pandas as pd

flight_data = pd.read_csv("unified/dataset.csv")
flight_data.WEATHER_DELAY.fillna(value=0, inplace=True)
flight_data.to_csv("dataset_weather_zero.csv", index=False)