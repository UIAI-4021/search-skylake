import pandas as pd
from queue import PriorityQueue

def dijkstra(source, destination):
    reached = []
    frontier = PriorityQueue()
    locations = df.loc[df['SourceAirport'] == source]
    for row in locations.iterrows():
        frontier.put((row[1]['Distance'], row[0]))
    while not frontier.empty():
        pop = frontier.get()
        distance = pop[0]
        node = pop[1]
        if df.loc[node, 'DestinationAirport'] == destination:
            return True
        reached.append(node)
        children = df.loc[df['SourceAirport'] == df.loc[node, 'DestinationAirport']]
        for children_row in children.iterrows():
            if children_row[0] not in reached:
                frontier.put((children_row[1]['Distance'] + distance, children_row[0]))


df = pd.read_csv('Flight_Data.csv')
#input = 'General Edward Lawrence Logan International Airport - John F Kennedy International Airport'.split(' - ')
input = 'Imam Khomeini International Airport - Raleigh Durham International Airport'.split(' - ')
source = input[0]
destination = input[1]
print(dijkstra(source,destination))

