import pandas as pd

flight_data = pd.read_csv("unified/dataset.csv")
station_data = pd.read_csv("unified/lcd-stations.csv")

flight_with_wban = pd.merge(flight_data, station_data, left_on='ORIGIN', right_on='STATION', how='left')
flight_with_wban.to_csv("flight_with_wban.csv", index=False)