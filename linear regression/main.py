import numpy as np
import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error


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

X_train, X_test, y_train, y_test = train_test_split(train[['departure_time', 'stops', 'arrival_time', 'class', 'duration', 'days_left']], train['price'], test_size=0.999, random_state=42, shuffle=True) # x , y , percent of test size, random state, shuffle

print(X_train)
w = []
for i in range(6):
    w.append(np.random.randn(1))
b = np.random.randn(1)

yp = pd.DataFrame(np.random.randn(1, 1), columns=['price'])

for i in X_train.iterrows():
    yp.loc[i[0]] = yp.loc[0]
    yp.loc[i[0]]['price'] = w[0] * i[1]['departure_time'] + w[1] * i[1]['stops'] + w[2] * i[1]['arrival_time'] + w[3] * i[1]['class'] + w[4] * i[1]['duration'] + w[5] * i[1]['days_left'] + b
    print(yp.loc[i[0]])
MAE_error = mean_absolute_error(y_train, yp)
print(MAE_error)