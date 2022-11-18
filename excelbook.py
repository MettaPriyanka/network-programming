import pandas as pd
#data = pd.read_csv(r'C:\pythoncode\Gaints.csv')

data = pd.read_excel(r'C:\pythoncode\companies.xlsx')
df = pd.DataFrame(data,columns=['CEO'])
print(df)