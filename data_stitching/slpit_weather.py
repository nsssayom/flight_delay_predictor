import pandas as pd

#flight_data = pd.read_csv("unified/flight.csv")
weather_data = pd.read_csv("unified/merged.csv", dtype='unicode')

#flight_with_wban = pd.merge(flight_data, station_data, left_on='ORIGIN', right_on='STATION', how='left')
#flight_with_wban.to_csv("flight_with_wban.csv", index=False)

weather_data['DATE_'], weather_data['TIME_'] = weather_data['DATE'].str.split("T",1).str
weather_data.to_csv("weather_splitted.csv", index=False)