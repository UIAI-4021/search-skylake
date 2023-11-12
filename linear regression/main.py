import numpy as np
import pandas as pd 
from sklearn.model_selection import train_test_split


train = pd.read_csv('Flight_Price_Dataset_Q2.csv')

class_map = {
    'Economy': 1,
    'Business': 2
}
train['class'] = train['class'].map(class_map)

departure_time_map = {
    'Night': 5,
    'Evening': 4,
    'Afternoon': 3,
    'Morning': 2,
    'Early_Morning': 1
}
train['departure_time'] = train['departure_time'].map(departure_time_map)

arrival_time_map = {
    'Night': 5,
    'Evening': 4,
    'Afternoon': 3,
    'Morning': 2,
    'Early_Morning': 1
}
train['arrival_time'] = train['arrival_time'].map(arrival_time_map)


stops_map = {
    'zero' : 1,
    'one' : 2,
    'two_or_more' : 3
}
train['stops'] = train['stops'].map(stops_map)
train.info()

X_train, X_test, y_train, y_test = train_test_split(train[['departure_time', 'stops', 'arrival_time', 'class', 'duration', 'days_left']], train['price'], random_state=42, shuffle=True) # x , y , percent of test size, random state, shuffle


w = []
for i in range(6):
    w.append(np.random.randn(1))
b = np.random.randn(1)

yp = []

for i in X_train.iterrows():
    yp[i] = w[0] * X_train[1]['departure_time'] + w[1] * X_train[1]['stops'] + w[2] * X_train[1]['arrival_time'] + w[3] * X_train[1]['class'] + w[4] * X_train[1]['duration'] + w[5] * X_train[1]['days_left'] + b
