import pandas as pd

df = pd.read_csv('data/occupations.csv')
occu=df.groupby('occupation')
no=occu['age'].count()
sigma=occu['age'].sum()
occulist=list(df["occupation"].unique())
# 코드를 작성하세요.
avgage=sigma/no
avgage.sort_values()
occu