"""#1 recommendation system using 내용기반추천, and linear_regression as a hypothesis function, thereby using mse as a J-function"""
#내용기반 추천-data끼리의 상호작용은 없음
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

"""#2 협업 필터링을 적용한 recommendation system"""
#2-1 data간 유사도 계산방법1 : Euclid Distance
import numpy as np
from math import sqrt

def euclid_distance(user1, user2):
    return sqrt(np.sum((user2-user1)*(user2-user1)))

user1 = np.array([[1,2,3],[2,2,2],[5,6,4]])
user2= np.array([[1,2,2],[1,1,1],[0,2,3]])

print(euclid_distance(user1, user2))

#2-2 data간 유사도 계산방법2 : cos 유사도