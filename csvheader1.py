import pandas as pd
df = pd.read_csv('data.csv')
df.head()#it prints the first n rows in the dataframe [default n=5]
print(df)
df['Lineprice'] = df['Quantity'] * df['UnitPrice']
df.head()
print(df)
df_customers = df.groupby('CustomerID').agg(
   orders=('InvoiceNo','nunique'),
   skus=('StockCode','nunique'),
   quantity=('Quantity','sum'),
   revenue=('Lineprice','sum'),
).reset_index()

df_customers.head()
print(df_customers)
