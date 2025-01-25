import pandas as pd

data = pd.read_excel('./pages/source.xlsx')

criteria1 = data['category'] == 'non food'
criteria2 = data['store_name'] == 'Indomaret'
criteria3 = data['price'] > 12000
criteria4 = (data['price'] >= 12000) & (data['price'] <= 40000)
criteria5 = (criteria1) & (criteria2) & (criteria3)

print(data[criteria5].sort_values('price',ascending=True))
