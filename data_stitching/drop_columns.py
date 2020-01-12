import pandas as pd

df = pd.read_csv("unified/flight.csv", dtype='unicode')
# columns = ['REPORT_TYPE', 'SOURCE', 'AWND', 'BackupDirection', 'BackupDistance', 'BackupDistanceUnit', 'BackupElements', 'BackupElevation', 
#             'BackupElevationUnit', 'BackupEquipment', 'BackupLatitude', 'BackupLongitude', 'BackupName', 'CDSD', 'CLDD', 'DSNW', 
#             'DailyAverageDewPointTemperature', 'DailyAverageDryBulbTemperature', 'DailyAverageRelativeHumidity', 'DailyAverageSeaLevelPressure', 
#             'DailyAverageStationPressure', 'DailyAverageWetBulbTemperature', 'DailyAverageWindSpeed', 'DailyCoolingDegreeDays', 
#             'DailyDepartureFromNormalAverageTemperature', 'DailyHeatingDegreeDays', 'DailyMaximumDryBulbTemperature', 'DailyMinimumDryBulbTemperature', 
#             'DailyPeakWindDirection', 'DailyPeakWindSpeed', 'DailyPrecipitation', 'DailySnowDepth', 'DailySnowfall', 'DailySustainedWindDirection', 
#             'DailySustainedWindSpeed', 'DailyWeather', 'HDSD', 'HTDD', 'HeavyFog', 'HourlyAltimeterSetting', 
#             'MonthlyAverageRH', 'MonthlyDaysWithGT001Precip', 'MonthlyDaysWithGT010Precip', 'MonthlyDaysWithGT32Temp', 'MonthlyDaysWithGT90Temp', 
#             'MonthlyDaysWithLT0Temp', 'MonthlyDaysWithLT32Temp', 'MonthlyDepartureFromNormalAverageTemperature', 'MonthlyDepartureFromNormalCoolingDegreeDays', 
#             'MonthlyDepartureFromNormalHeatingDegreeDays', 'MonthlyDepartureFromNormalMaximumTemperature', 'MonthlyDepartureFromNormalMinimumTemperature', 
#             'MonthlyDepartureFromNormalPrecipitation', 'MonthlyDewpointTemperature', 'MonthlyGreatestPrecip', 'MonthlyGreatestPrecipDate', 'MonthlyGreatestSnowDepth', 
#             'MonthlyGreatestSnowDepthDate', 'MonthlyGreatestSnowfall', 'MonthlyGreatestSnowfallDate', 'MonthlyMaxSeaLevelPressureValue', 'MonthlyMaxSeaLevelPressureValueDate', 
#             'MonthlyMaxSeaLevelPressureValueTime', 'MonthlyMaximumTemperature', 'MonthlyMeanTemperature', 'MonthlyMinSeaLevelPressureValue', 
#             'MonthlyMinSeaLevelPressureValueDate', 'MonthlyMinSeaLevelPressureValueTime', 'MonthlyMinimumTemperature', 'MonthlySeaLevelPressure', 
#             'MonthlyStationPressure', 'MonthlyTotalLiquidPrecipitation', 'MonthlyTotalSnowfall', 'MonthlyWetBulb', 'NormalsCoolingDegreeDay', 
#             'NormalsHeatingDegreeDay', 'REM', 'REPORT_TYPE.1', 'SOURCE.1', 'ShortDurationEndDate005', 'ShortDurationEndDate010', 'ShortDurationEndDate015', 
#             'ShortDurationEndDate020', 'ShortDurationEndDate030', 'ShortDurationEndDate045', 'ShortDurationEndDate060', 'ShortDurationEndDate080', 
#             'ShortDurationEndDate100', 'ShortDurationEndDate120', 'ShortDurationEndDate150', 'ShortDurationEndDate180', 'ShortDurationPrecipitationValue005', 
#             'ShortDurationPrecipitationValue010', 'ShortDurationPrecipitationValue015', 'ShortDurationPrecipitationValue020', 'ShortDurationPrecipitationValue030', 
#             'ShortDurationPrecipitationValue045', 'ShortDurationPrecipitationValue060', 'ShortDurationPrecipitationValue080', 'ShortDurationPrecipitationValue100', 
#             'ShortDurationPrecipitationValue120', 'ShortDurationPrecipitationValue150', 'ShortDurationPrecipitationValue180', 'Sunrise', 'Sunset', 'TStorms', 
#             'WindEquipmentChangeDate', 'HourlyPrecipitation',	'HourlyPresentWeatherType',	'HourlyPressureChange',	'HourlyPressureTendency', 'HourlyWindGustSpeed']

columns = ['ORIGIN']
df.drop(columns, inplace=True, axis=1)

df.to_csv("flight_dropped.csv", index=False)
