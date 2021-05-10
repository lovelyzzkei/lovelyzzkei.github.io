import pandas as pd
import numpy as np

# 데이터프레임에 다운받은 파일 저장
df = pd.read_csv('ArticlesApril2018.csv')

# 데이터 개수, 열 개수, 열 이름 등 기본적인 정보들 파악
# 앞의 데이터 몇 개만 확인해서 데이터가 어떤 특징을 가지고 있는지 확인
print(df.head())
print("열 정보: ", df.columns)
print("열 개수: ", len(df.columns))
print("데이터의 개수: ", len(df))

# 필요한 headline 열만 따로 추출
headline = []
headline.extend(df['headline'].values)

print(headline[:10])

print(df['headline'].isnull().any())
headline = [title for title in headline if title != 'Unknown']
print(len(headline))

from string import punctuation

def repreprocessing(s):
    s = s.encode("utf8").decode("ascii", 'ignore')

    return ''.join(c for c in s if c not in punctuation).lower()

text = [repreprocessing(x) for x in headline]
print(text[:5])