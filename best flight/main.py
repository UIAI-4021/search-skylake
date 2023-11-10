import pandas as pd
from geopy.distance import great_circle as GRC
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




def heuristic(source , destination):
    temp = df.loc[df['SourceAirport'] == source]
    source_lat =temp.iloc[0]['SourceAirport_Latitude']
    source_lon =temp.iloc[0]['SourceAirport_Longitude']

    temp = df.loc[df['DestinationAirport'] == destination]
    destination_lat =temp.iloc[0]['DestinationAirport_Latitude']
    destination_lon =temp.iloc[0]['DestinationAirport_Longitude']
    resault =  GRC([source_lat , source_lon],[destination_lat , destination_lon]).km
    return resault



def a_star(source , destination):
    reached = []
    reached.append(source)
    path = {}
    frontier = PriorityQueue()
    locations = df.loc[df['SourceAirport'] == source]
    for row in locations.iterrows():
        reached.append(row[1]['DestinationAirport'])
        f = heuristic(row[1]['SourceAirport'] , destination) + row[1]['Distance']
        frontier.put((f, row[0]))
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
                f = heuristic(children_row[1]['SourceAirport'] , destination) + distance
                frontier.put((f, children_row[0]))
                path.update({children_row[0]: path[node].copy()+ [children_row[0]]})



df = pd.read_csv('Flight_Data.csv')
input = 'Imam Khomeini International Airport - Raleigh Durham International Airport'.split(' - ')
#input = 'General Edward Lawrence Logan International Airport - John F Kennedy International Airport'.split(' - ')
source = input[0]
destination = input[1]
finded_path = a_star(source,destination)
print(finded_path)


distance_sum=0

for i in finded_path:

    distance_sum += df.loc[i, 'Distance']

print('\nTotal Distance: : ' + str(distance_sum) + ' km')