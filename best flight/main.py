import collections
import pandas as pd
from queue import PriorityQueue

def dijkstra(source, destination):
    reached = []
    reached.append(source)
    path = {}
    frontier = PriorityQueue()
    locations = df.loc[df['SourceAirport'] == source]
    for row in locations.iterrows():
        reached.append(row[1]['DestinationAirport'])
        frontier.put((row[1]['Distance'], row[0]))
        path.update({row[0]: [row[0]]})
    while not frontier.empty():
        pop = frontier.get()
        distance = pop[0]
        node = pop[1]
        if df.loc[node, 'DestinationAirport'] == destination:
            return path[node]
        reached.append(df.loc[node, 'DestinationAirport'])
        children = df.loc[df['SourceAirport'] == df.loc[node, 'DestinationAirport']]
        for children_row in children.iterrows():
            if children_row[1]['DestinationAirport'] not in reached:
                frontier.put((children_row[1]['Distance'] + distance, children_row[0]))
                path.update({children_row[0]: path[node].copy()+ [children_row[0]]})

df = pd.read_csv('Flight_Data.csv')
input = 'Imam Khomeini International Airport - Raleigh Durham International Airport'.split(' - ')
#input = 'General Edward Lawrence Logan International Airport - John F Kennedy International Airport'.split(' - ')
source = input[0]
destination = input[1]
finded_path = dijkstra(source,destination)
print(finded_path)
for index in finded_path:
    print(df.loc[index])

