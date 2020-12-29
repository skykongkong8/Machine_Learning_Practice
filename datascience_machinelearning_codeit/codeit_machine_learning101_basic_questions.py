"""#1 Diabetes dataset"""
#Using Multiple Linear Regression
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

import pandas as pd  

# 당뇨병 데이터 갖고 오기
diabetes_dataset = datasets.load_diabetes()

# 입력 변수를 사용하기 편하게 pandas dataframe으로 변환
X = pd.DataFrame(diabetes_dataset.data, columns=diabetes_dataset.feature_names)

# 목표 변수를 사용하기 편하게 pandas dataframe으로 변환
y = pd.DataFrame(diabetes_dataset.target, columns=['diabetes'])

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=5)
model = LinearRegression()
model.fit(X_train, y_train)
print(model.coef_, model.intercept_)
# 평균 제곱 오차의 루트를 통해서 테스트 데이터에서의 모델 성능 판단
y_test_predict=model.predict(X_test)
mse = mean_squared_error(y_test, y_test_predict)

mse ** 0.5

"""#2 Diabetes dataset2"""
#Using Polynomial Regression

from sklearn import datasets
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

import pandas as pd  

diabetes_dataset = datasets.load_diabetes()


diabetes_dataset = datasets.load_diabetes()  # 데이터 셋 갖고오기

polynomial_transformer = PolynomialFeatures(2)
polynomial_data = polynomial_transformer.fit_transform(diabetes_dataset.data)
polynomial_feature_names = polynomial_transformer.get_feature_names(diabetes_dataset.feature_names)
X=pd.DataFrame(polynomial_data,columns=polynomial_feature_names)
# 목표 변수
y = pd.DataFrame(diabetes_dataset.target, columns=['diabetes'])

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2, random_state=5)
model=LinearRegression()
model.fit(X_train, y_train)

y_test_predict=model.predict(X_test)

mse = mean_squared_error(y_test, y_test_predict)
print(mse ** 0.5)

"""#3 Wine data"""
#Using Logistic Regression
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

import pandas as pd  

wine_data = datasets.load_wine()
""" 데이터 셋을 살펴보는 코드
print(wine_data.DESCR)
"""

# 입력 변수를 사용하기 편하게 pandas dataframe으로 변환
X = pd.DataFrame(wine_data.data, columns=wine_data.feature_names)

# 목표 변수를 사용하기 편하게 pandas dataframe으로 변환
y = pd.DataFrame(wine_data.target, columns=['Y/N'])
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=5)
y_train=y_train.values.ravel()
model=LogisticRegression(solver='saga', max_iter=7500)
model.fit(X_train, y_train)
y_test_predict=model.predict(X_test)
score = model.score(X_test, y_test)
# 테스트 코드
print(y_test_predict, score)