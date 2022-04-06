from os import system

system('clear')
# 101 What is Pandas

# 102 Pandas Installation and Sample file
import pandas as pd

data = pd.read_csv("countries_population.csv")

print(data.head(5)) #first 5 rows

print(data.tail(5)) #last 5 rows

system('clear')

# 103 Dataframe Creation methods

