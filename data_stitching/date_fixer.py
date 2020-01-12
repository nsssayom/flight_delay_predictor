import pandas as pd
import datetime
flight_data = pd.read_csv("unified/flight.csv")

flight_data['DATE'] = pd.to_datetime(flight_data['DATE'])

flight_data.to_csv("flight_date_fixed.csv", index=False)