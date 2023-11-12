import numpy as np
import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
from sklearn.linear_model import LinearRegression



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

X_train, X_test, y_train, y_test = train_test_split(train[['departure_time', 'stops', 'arrival_time', 'class', 'duration', 'days_left']], train['price'], test_size=0.999, random_state=42, shuffle=False) # x , y , percent of test size, random state, shuffle


w = []
for i in range(6):
    w.append(np.random.randn(1))
b = np.random.randn(1)

for repeat_counte in range(100):
    yp = pd.DataFrame(columns = ['price'])

    for i in X_train.iterrows():
        yp.loc[i[0], 'price'] = w[0] * i[1]['departure_time'] + w[1] * i[1]['stops'] + w[2] * i[1]['arrival_time'] + w[3] * i[1]['class'] + w[4] * i[1]['duration'] + w[5] * i[1]['days_left'] + b
    MAE_error = round(mean_absolute_error(y_train, yp), 10)

    b_grad = -2 * MAE_error
    w_grad = [0] * (6)

    for i in range (6):
        for j in X_train.iterrows():
            w_grad[i] += (j[1][i] * (yp.loc[j[0], 'price'] - y_train.loc[j[0]]))
        w_grad[i] = w_grad[i] * (-2) / len(X_train.index)


    lr = 0.1
    b = np.round(b - lr * b_grad, 10 )
    for i in range(6):
        w[i] = np.round(w[i] - lr * w_grad[i], 10)



print(b)
print(w)