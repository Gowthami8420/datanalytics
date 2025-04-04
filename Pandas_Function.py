import pandas as pd
s=pd.Series([10,20,30,40],index=['a','b','c','d'])
print(s)

data={
    'name':['Alice','Bob','Charlie'],
    'age':[20,30,22],
    'city':['kphb','sr nagar','lbnagar']
}
df=pd.DataFrame(data)
print(df)
c=df.to_csv('data.csv')
print(df.head())
print(df.tail())
print(df.info())
print(df.shape)
print(df.describe())
print(df.columns)
print(df['age'])
print(df[['name','city']])
print(df[df['age']>28])
print(df.iloc[1])
print(df.loc[1])
df['age']+=1
print(df['age'])
df['country']='usa'
print(df)

df.rename(columns={'age':'years'},inplace=True)
print(df)
df.drop('city',axis=1)
print(df)