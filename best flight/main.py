import pandas as pd

df = pd.read_csv('Flight_Data.csv')
input = 'Imam Khomeini International Airport - Raleigh Durham International Airport'.split(' - ')
source = input[0]
destination = input[1]

locations = df.loc[df['SourceAirport'] == source]

print(locations)