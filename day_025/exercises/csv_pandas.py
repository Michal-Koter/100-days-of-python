import pandas as pd

df = pd.read_csv("data/weather_data.csv")
# print(df["temp"])

data_dict = df.to_dict()
print(data_dict)

temp_list = df["temp"].to_list()
print(temp_list)

print(df["temp"].mean())
print(df["temp"].max())

print(df[df.day == "Monday"])
print(df[df.temp == df.temp.max()])

data_dict = {
    "student": ["Amy", "James", "Angela"],
    "score": [76, 56, 65]
}

data = pd.DataFrame(data_dict)
print(data)
data.to_csv("data/new_data.csv")