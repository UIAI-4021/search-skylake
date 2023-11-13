import numpy as np
import pandas as pd 
from sklearn.model_selection import train_test_split


train = pd.read_csv('Flight_Price_Dataset_Q2.csv')
train['price'] = train['price'].astype(float)

class_map = {
    'Economy': 1,
    'Business': 2
}
train['class'] = train['class'].map(class_map)

departure_time_map = {
    'Late_Night' : 1,
    'Night': 2,
    'Evening': 3,
    'Afternoon': 4,
    'Morning': 5,
    'Early_Morning': 6
}
train['departure_time'] = train['departure_time'].map(departure_time_map)

arrival_time_map = {
    'Late_Night' : 1,
    'Night': 2,
    'Evening': 3,
    'Afternoon': 4,
    'Morning': 5,
    'Early_Morning': 6
}
train['arrival_time'] = train['arrival_time'].map(arrival_time_map)


stops_map = {
    'zero' : 1,
    'one' : 2,
    'two_or_more' : 3
}
train['stops'] = train['stops'].map(stops_map)

X_train, X_test, y_train, y_test = train_test_split(train[['departure_time', 'stops', 'arrival_time', 'class', 'duration', 'days_left']], train['price'], test_size=0.2, random_state=42, shuffle=True) # x , y , percent of test size, random state, shuffle


w = []
np.random.seed(2)
for i in range(6):
    w.append(np.random.randn(1))
b = np.random.randn(1)
lr = 0.000966
for repeat_counte in range(5000):
    yp = w[0] * X_train['departure_time'] + w[1] * X_train['stops'] + w[2] * X_train['arrival_time'] + w[3] * X_train['class'] + w[4] * X_train['duration'] + w[5] * X_train['days_left'] + b
    error = (y_train - yp)
    loss = (error ** 2).mean()
    b_grad = -2 * error.mean()
    w_grad = [0] * (6)
    w_grad[0] = -2 * (X_train['departure_time'] * error).mean()
    w_grad[1] = -2 * (X_train['stops'] * error).mean()
    w_grad[2] = -2 * (X_train['arrival_time'] * error).mean()
    w_grad[3] = -2 * (X_train['class'] * error).mean()
    w_grad[4] = -2 * (X_train['duration'] * error).mean()
    w_grad[5] = -2 * (X_train['days_left'] * error).mean()
    b = b - lr * b_grad
    for i in range(6):
        w[i] = w[i] - lr * w_grad[i]
