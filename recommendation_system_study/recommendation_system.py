"""#1 recommendation system using 내용기반추천, and linear_regression as a hypothesis function, thereby using mse as a J-function"""
#1내용기반 추천-data끼리의 상호작용은 없음
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

"""#3 유클리드 거리를 기준으로 유사한 이웃들 뽑아내고, 이웃을 기준으로 빈 데이터를 평균으로 채운 다음, 추천하기"""

import pandas as pd
import numpy as np
from math import sqrt

RATING_DATA_PATH = 'C:/Users/공성식/Desktop/WORKSTATION/Python Workplace/codeit/intermediate_machine_learning/5fb0e111933f7147701779cf_3681/3681/data/ratings.csv'  # 받아올 평점 데이터 경로 정의

np.set_printoptions(precision=2)  # 소수점 둘째 자리까지만 출력

def distance(user_1, user_2):
    """유클리드 거리를 계산해주는 함수"""
    return sqrt(np.sum((user_1 - user_2)**2))
    
    
def filter_users_without_movie(rating_data, movie_id):
    """movie_id 번째 영화를 평가하지 않은 유저들은 미리 제외해주는 함수"""
    return rating_data[~np.isnan(rating_data[:,movie_id])]
    
    
def fill_nan_with_user_mean(rating_data):
    """평점 데이터의 빈값들을 각 유저 평균 값으로 체워주는 함수"""
    filled_data = np.copy(rating_data)  # 평점 데이터를 훼손하지 않기 위해 복사
    row_mean = np.nanmean(filled_data, axis=0)  # 유저 평균 평점 계산-이때 nanmean 을 사용!
    
    inds = np.where(np.isnan(filled_data))  # 비어 있는 인덱스들을 구한다-np.where 이라는 메소드 사용! 이 정보로 새롭게 인덱싱 할 수 있다! 아래처럼:
    filled_data[inds] = np.take(row_mean, inds[1])  #빈 인덱스를 유저 평점으로 채운다
    
    return filled_data
    
    
def get_k_neighbors(user_id, rating_data, k):
    """user_id에 해당하는 유저의 이웃들을 찾아주는 함수"""
    distance_data = np.copy(rating_data)  # 평점 데이터를 훼손하지 않기 위해 복사
    # 마지막에 거리 데이터를 담을 열 추가한다
    distance_data = np.append(distance_data, np.zeros((distance_data.shape[0], 1)), axis=1)
    
    for i in range(len(rating_data)):
        if i == user_id:
            distance_data[i][-1] = np.inf
        else:
            distance_data[i][-1] = distance(rating_data[user_id], rating_data[i])

    
    # 데이터를 거리 열을 기준으로 정렬한다
    distance_data = distance_data[np.argsort(distance_data[:, -1])]
    
    # 가장 가까운 k개의 행만 리턴한다 + 마지막(거리) 열은 제외한다
    return distance_data[:k, :-1]
    

# 실행 코드     
rating_data = pd.read_csv(RATING_DATA_PATH, index_col='user_id').values  # 평점 데이터를 불러온다
filtered_data = filter_users_without_movie(rating_data, 3)  # 3 번째 영화를 보지 않은 유저를 데이터에서 미리 제외시킨다
filled_data = fill_nan_with_user_mean(filtered_data)  # 빈값들이 채워진 새로운 행렬을 만든다
user_0_neighbors = get_k_neighbors(0, filled_data, 5)  # 유저 0과 비슷한 5개의 유저 데이터를 찾는다
print(user_0_neighbors)