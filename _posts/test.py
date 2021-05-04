import pandas as pd
from sklearn.datasets import fetch_20newsgroups

newsdata = fetch_20newsgroups(subset='train')

print(newsdata.keys())
print(newsdata.data[:5])
print(newsdata.target[:5])
print(newsdata.target_names)

data = pd.DataFrame(data=newsdata.data, columns=['email'])
data['target'] = pd.Series(newsdata.target) # 데이터프레임에 'target'열 추가
print(data[:5])