import pandas as pd
import streamlit as st

data = pd.read_excel('./pages/source.xlsx')
unique_category = data['category'].unique()
unique_storename = data['store_name'].unique()

selected_category = st.multiselect("Select category",options=unique_category)

criteria1 = data['category'].isin(selected_category)

criteria2 = data['store_name'] == 'Indomaret'
criteria3 = data['price'] > 12000
criteria4 = (data['price'] >= 12000) & (data['price'] <= 40000)
criteria5 = (criteria1) & (criteria2) & (criteria3)

data = data[criteria1]

print(data[criteria5].sort_values('price',ascending=True))
st.dataframe(data)
