import pandas as pd
df = pd.read_csv("dataset/dataset.csv", dtype='unicode')

df["Pressure"] = df["Pressure"].str.replace("s", "")
df.to_csv("new_dataset.csv", index=False)