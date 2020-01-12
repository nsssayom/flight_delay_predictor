import pandas as pd

flight_data = pd.read_csv("unified/flight.csv")
station_data = pd.read_csv("unified/weather.csv")

#flight_data.dropna()
#station_data.dropna()

flight_data['DATETIME'] = pd.to_datetime(flight_data['DATETIME'])
station_data['DATETIME'] = pd.to_datetime(station_data['DATETIME'])

merged = pd.merge_asof(flight_data.sort_values('DATETIME'), 
                        station_data.sort_values('DATETIME'), 
                        by='WBAN', 
                        on='DATETIME', 
                        allow_exact_matches=True, 
                        direction='nearest')
dropped = merged.dropna(subset=['HourlyDewPointTemperature'])
dropped.to_csv("unified.csv", index=False)