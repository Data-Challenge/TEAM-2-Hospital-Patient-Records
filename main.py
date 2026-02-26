import pandas as pd

pd.options.display.max_rows = 999

df = pd.read_csv("hospital.csv")

print(df)