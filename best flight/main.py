import pandas as pd
from queue import PriorityQueue

df = pd.read_csv('Flight_Data.csv')
input = 'Imam Khomeini International Airport - Raleigh Durham International Airport'.split(' - ')
source = input[0]
destination = input[1]

locations = df.loc[df['SourceAirport'] == source]

print(locations.iat[2,13])


def dijkstra(source, destination):
    frontier = PriorityQueue()
    for index in locations.index:
        frontier.put(df.loc[index])
    while not frontier.empty:
        node = frontier.get
        # check is goal or not
        children = df.loc[df['SourceAirport'] == source]
        for index in children.index:
            frontier.put(df.loc[index])
        
    return 'path not found'