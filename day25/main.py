# Create a new csv file which generates the count of squirrels by their colour
import pandas as pd

df_raw = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv",encoding='utf-8')
df_count = df_raw.groupby(["Primary Fur Color"])["Unique Squirrel ID"].count()
print(df_count)

df_count.to_csv("squirrel_count.csv")