import streamlit as st


conversion_factors = {
  'distance':{'mm':1,
              'cm':0.1,
              'dcm':0.01,
              'm':0.001,
              'dm':0.0001,
              'hm':0.00001,
              'km':0.000001},
  'weight':{"mg": 1,
           "g": 0.01,
           "kg": 0.000001},
  'time':{"hour" : 1,
         "minute" : 60,
         "second" : 60*60,
          "day" : 1/24,
          "week" : 1/24*7,
          "month" : 1/24*7*4,
          "year" : 1/24*7*4*12,
          "decade" : 1/24*7*4*12*10,
          "century" : 1/24*7*4*12*10*10}}

col1,col2,col3,col4,col5 = st.columns(5)
#category selection
with col1:
  st.write("Category")
  category_list = list(conversion_factors.keys())
  category = st.radio("Select Category",options=category_list)

with col2:
  st.write("Input")
  st.text_input("Enter Text")

with col3:
  base_unit_list = list(conversion_factors[category].keys())
  base_unit = st.radio("From:",options=base_unit_list)

with col4:
  target_unit_list = list(conversion_factors[category].keys())
  target_unit = st.radio("To:",options=target_unit_list)

with col5:
  st.write("output")
