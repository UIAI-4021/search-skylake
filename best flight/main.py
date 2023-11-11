import time
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
        f = heuristic(row[1]['DestinationAirport'] , destination) + row[1]['Distance']
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
                f = heuristic(children_row[1]['DestinationAirport'] , destination) + distance + children_row[1]['Distance']
                frontier.put((f, children_row[0]))
                path.update({children_row[0]: path[node].copy()+ [children_row[0]]})



def write_result(algorithm, time, data):
    f = open("skylake-UIAI4021-PR1-Q1(" + algorithm + ").txt", "w")
    f.write(algorithm + ' Algorithm')
    f.write("\nExecution Time:" + str(time))
    f.write('\n.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-')
    index = 1
    distance_sum=0
    price_sum=0
    time_sum=0
    for i in data:
        f.write('\nFlight #' + str(index) + '(' + df.loc[i, 'Airline'] + ')')
        f.write('\nFrom: ' + df.loc[i, 'SourceAirport'] + ' - ' + df.loc[i, 'SourceAirport_Country'] + ', ' + df.loc[i, 'SourceAirport_City'])  
        f.write('\nFrom: ' + df.loc[i, 'DestinationAirport'] + ' - ' + df.loc[i, 'DestinationAirport_Country'] + ', ' + df.loc[i, 'DestinationAirport_City'])
        f.write('\nDistance: ' + str(df.loc[i, 'Distance']) + 'km')
        f.write('\nTime: ' + str(df.loc[i, 'FlyTime']) + ' h')
        f.write('\nPrice: ' + str(df.loc[i, 'Price']) + ' $')
        f.write('\n----------------------------')
        index += 1
        distance_sum += df.loc[i, 'Distance']
        time_sum += df.loc[i, 'FlyTime']
        price_sum += df.loc[i, 'Price']
    f.write('\nTotal Price: ' + str(price_sum) + ' $')
    f.write('\nTotal Distance: ' + str(distance_sum) + ' km')
    f.write('\nTotal Time: ' + str(time_sum) + ' h')


df = pd.read_csv('Flight_Data.csv')
input = input().split(' - ')
source = input[0]
destination = input[1]
start_time = time.time()
finded_path = a_star(source,destination)
write_result('a*', (time.time() - start_time), finded_path)
start_time = time.time()
finded_path = dijkstra(source,destination)
write_result('dijkstra', (time.time() - start_time), finded_path)
