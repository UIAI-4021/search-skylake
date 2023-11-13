from math import sqrt
import time
import numpy as np
import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import r2_score


train = pd.read_csv('linear regression/Flight_Price_Dataset_Q2.csv')
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

start_time = time.time()
w = []
np.random.seed(2)
for i in range(6):
    w.append(np.random.randn(1))
b = np.random.randn(1)
lr = 0.000966
for repeat_counte in range(5000):
    yp = w[0] * X_train['departure_time'] + w[1] * X_train['stops'] + w[2] * X_train['arrival_time'] + w[3] * X_train['class'] + w[4] * X_train['duration'] + w[5] * X_train['days_left'] + b
    error = (y_train - yp)
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

yp_test = w[0] * X_test['departure_time'] + w[1] * X_test['stops'] + w[2] * X_test['arrival_time'] + w[3] * X_test['class'] + w[4] * X_test['duration'] + w[5] * X_test['days_left'] + b

f = open("linear regression/4-UIAI4021-PR1-Q2.txt", "w")
f.write('PRICE = ' + str(w[0][0]) + ' * departure_time + ' + str(w[1][0]) + ' * stops + ' + str(w[2][0]) + ' * arrival_time + ' + str(w[3][0]) + ' * class + ' + str(w[4][0]) + ' * duration + ' + str(w[5][0]) + ' * days_left + ' + str(b[0]))
f.write('\nTraining Time: ' + str((time.time() - start_time)) + ' s')
f.write('\n\nLogs:')
f.write('\nMSE: ' + str(mean_squared_error(y_test, yp_test)))
f.write('\nRMSE: ' + str(sqrt(mean_squared_error(y_test, yp_test))))
f.write('\nMAE: ' + str(mean_absolute_error(y_test, yp_test)))
f.write('\nR2: ' + str(r2_score(y_test, yp_test)))