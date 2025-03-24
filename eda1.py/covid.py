import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv("C:/Users/kumar/Downloads/country_wise_latest.csv")
print(df.head())
# df['ObservationDate'] = pd.to_datetime(df['ObservationDate'])
# df.dropna(subset=['Confirmed', 'Deaths', 'Recovered'], inplace=True)

df.rename(columns={'New cases': 'ObservationDate'}, inplace=True)
df['ObservationDate'] = pd.to_datetime(df['ObservationDate'])
df.dropna(subset=['Confirmed', 'Deaths', 'Recovered'], inplace=True)
total_confirmed = df['Confirmed'].sum()
total_deaths = df['Deaths'].sum()
total_recovered = df['Recovered'].sum()
print(f"Total confirmed cases: {total_confirmed}")