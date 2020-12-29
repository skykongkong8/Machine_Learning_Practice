from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error

movie_data_path = 'C:/Users/공성식\Documents/git_practice/machine_learning_study/recommendation_system_study/movie_rating.csv'

movie_rating_df = pd.read_csv(movie_data_path)
features = ['romance','action', 'comedy','heart-warming']
X = movie_rating_df[features]
Y = movie_rating_df[['rating']]

X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size = 0.2, random_state=5)

model = LinearRegression()
model.fit(X_train, Y_train)

y_test_predict=model.predict(X_test)
print(y_test_predict)
mse = mean_squared_error(Y_test, y_test_predict)
print(mse ** 0.5)