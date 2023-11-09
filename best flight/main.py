import pandas as pd
from queue import PriorityQueue

def dijkstra(source, destination):
    reached = []
    frontier = PriorityQueue()
    locations = df.loc[df['SourceAirport'] == source]
    for index in locations.index:
        frontier.put((df['Distance'].loc[index], df.loc[index]))
    while not frontier.empty():
        node = frontier.get()[1]
        if node['DestinationAirport'] == destination:
            return True
        reached.append(node)
        children = df.loc[df['SourceAirport'] == source]
        for children_index in children.index:
            if children.loc[children_index] not in reached and children['DestinationAirport'].loc[children_index] != node['DestinationAirport'].loc[index]:
                frontier.put((df['Distance'].loc[children_index]+node['DestinationAirport'].loc[index],df.loc[children_index]))

df = pd.read_csv('Flight_Data.csv')
input = 'Hamad International Airport - Imam Khomeini International Airport'.split(' - ')
source = input[0]
destination = input[1]
print(dijkstra(source,destination))

