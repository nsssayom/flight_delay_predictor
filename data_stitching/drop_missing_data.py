import pandas as pd
import numpy as np

flight_data = pd.read_csv("unified/unified.csv", dtype='unicode')
print(flight_data.isna().sum())

flight_data = flight_data[np.isfinite(flight_data['HourlyDewPointTemperature'])]

print(flight_data.isna().sum())
flight_data.to_csv("dataset_no_missing.csv", index=False)
