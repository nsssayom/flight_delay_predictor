import pandas as pd 
import plotly.express as px
import plotly.graph_objects as go

dataframe = pd.read_csv("dataset/dataset.csv")

field_x = 'Pressure'
field_y = 'WEATHER_DELAY'
title = field_x + " vs " + field_y

#figure = px.scatter(data_frame= dataframe, x = field_x, y = field_y, title= title)
figure = px.scatter(data_frame= dataframe, x = field_x, y = field_y, title= title)
figure.write_image("plots/" + title + ".png")
figure.show()