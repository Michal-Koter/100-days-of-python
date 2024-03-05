import pandas as pd

# extract Fur Color and Count of each from CSV

df = pd.read_csv("data/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

colors = df["Primary Fur Color"].value_counts()

colors.to_csv("data/squirrel_count.csv")

print(colors)
