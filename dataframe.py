import pandas as pd 
#df=pd.DataFrame()
#print(df)
#using the dic data
data = {'country':['India','Brazil','Africa'],

'Captial':['New delhi', 'Brasilia', 'Congo'],

'population': [1234567654,23456876,2345676]}
df = pd.DataFrame(data,columns=['country', 'Captial', 'population'])
print(df)