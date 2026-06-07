import pandas as pd

df = pd.read_csv("../data/ecommerce_raw.csv")

df.drop_duplicates(inplace=True)

df.to_csv(
    "../data/ecommerce_clean.csv",
    index=False
)

print("Cleaning Completed")