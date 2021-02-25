from sklearn.tree import DecisionTreeClassifier
import pandas as pd
import numpy as np

grape_variety = {
    'cab' : 1,
    'chardonnay' : 2,
    'pino noir' : 3,
    'pino grigio' : 4,
    'shiraz' : 5,
    'syrah' : 5,
    'malbec' : 6,
    'carmenere' : 7,
    'merlot' : 8,
    'tempranillo' : 9,
    'else' : 0
}


#데이터 불러오기
data = pd.read_csv('C:/Users/공성식/Desktop/WORKSTATION/Workstation_data/skykongkong_wine_data.csv')

#Feature Engineering

#1 grape variety를 수치화할 수 있는 숫자로 바꾸기
for variety in grape_variety.keys():
    data.loc[data.loc[:,'grape variety'] == variety, 'grape variety'] = grape_variety[variety]

#2 정답 부분 - evaluation을 제거하기 (추후에 진행할 것이므로 여기서는 생략하였음)
# try:
#     data.drop('evaluation', axis = 1, inplace = True)
# except:
#     pass
    
#3 비비노 점수 변화 스케일이 너무 작으므로 더 키운다.
VIVINO_PORTION = float(input('비비노 점수를 얼마나 반영할 것인지 정해주세요 : '))
data.loc[:, 'vivino'] = data.loc[:, 'vivino']*VIVINO_PORTION

# 결정트리로 학습
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

#DataFrame일때, model 생성

X = data.drop(['evaluation'], axis =1)
y = data['evaluation']
y = y.astype({'evaluation' : 'int'})

tree = DecisionTreeClassifier()
tree.fit(X,y)

def check_your_wine(model, grape_variety,data):
    while True:    
        Grape_Variety = input('포도 품종을 입력하세요 : ')
        if Grape_Variety in grape_variety:
            break
        else:
            print(f'품종 이름을 잘못 입력하셨습니다! 다시 입력해주세요. 입력값 : {Grape_Variety}')

    Color = int(input('색깔 정보를 입력하시오 [레드와인 : 0, 화이트와인 : 1] : '))
    Oak = int(input('오크향이 있습니까? [예 : 1, 아니오: 0] : '))
    Vivino = float(input('비비노 평점을 입력하세요 : '))
    RedFruit = int(input('붉은 과일 향이 있습니까? [예 : 1, 아니오 : 0] : '))
    BlackFruit = int(input('검은 과일 향이 있습니까? [예 : 1, 아니오 : 0] : '))
    Earthy = int(input('흙, 버섯, 가죽 향이 있습니까? [예 : 1, 아니오 : 0] : '))
    Spicy = int(input('스파이시한 특성이 있습니까? [예 : 1, 아니오 : 0] : '))
    Citrus = int(input('시트러스 향이 있습니까? [예 : 1, 아니오 : 0] : '))
    TreeFruit = int(input('나무열매 향이 있습니까? [예 : 1, 아니오 : 0] : '))
    TropicalFruit = int(input('열대과일 향이 있습니까? [예 : 1, 아니오 : 0] : '))
    
    X = data.drop(['evaluation'], axis =1)
    df_t = pd.DataFrame([grape_variety[Grape_Variety], Color, Oak, Vivino, RedFruit,\
                                         BlackFruit, Earthy, Spicy, Citrus, TreeFruit, TropicalFruit], X.columns)


    df=df_t.transpose()

    prediction = model.predict(df)

    if prediction >=4.0:
        print(f'당신이 정말 좋아하는 스타일의 와인입니다! 예상 평점 : {prediction}')
    elif 4.0>prediction >= 3.7:
        print(f'당신의 취향에 맞는 와인입니다. 예상 평점 : {prediction}')
    elif 3.7> prediction > 3.4:
        print(f'당신의 취향과는 맞지 않을 수도 있겠군요. 하지만 때때로 마실만 할겁니다. 예상 평점 : {prediction}')
    elif 3.4>=prediction>3.0:
        print(f'당신이 별로 좋아하지 않을 와인 같습니다. 예상 평점 : {prediction}')
    else:
        print(f'당신이 전혀 좋아하지 않는 스타일의 와인입니다. 예상 평점 : {prediction}')
    wanna_record = int(input('방금 예측한 와인의 평점을 매기시겠습니까? : [예 : 1, 아니오 : 0] : '))
    if wanna_record ==1:
        with open('C:/Users/공성식/Desktop/WORKSTATION/Workstation_data/skykongkong_wine_data.csv','a') as f:
            your_score = float(input('당신의 평가를 적어주세요. 학습한 뒤 더 나은 기능을 제공합니다! : '))
            f.write(f'\n{Grape_Variety},{Color},{Oak},{Vivino},{RedFruit},{BlackFruit},{Earthy},{Spicy},{Citrus},{TreeFruit},{TropicalFruit},{your_score}')
    else:
        print('감사합니다.')

if __name__ == '__main__':
    check_your_wine(tree, grape_variety,data)
