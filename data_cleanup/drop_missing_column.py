import pandas as pd
import numpy as np
import sys

df = pd.read_csv("dataset/dataset.csv")
print(df.isna().sum())

df = df.dropna(axis=0)

print("__After Cleanup__")
print(df.isna().sum())
df.to_csv("dataset_no_missing.csv", index=False)
