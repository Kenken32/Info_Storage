import streamlit as st


conversion_factors = {
  'distance':{'mm':1,
              'cm':0.1,
              'dcm':0.01,
              'm':0.001,
              'dm':0.0001,
              'hm':0.00001,
              'km':0.000001},
  'weight':{"gr":1/0.001,
            "Kg":1,
            "7-Year-Old kid" : 1/22,
            "Ton":1/1000,
            "Adult person":1/70,
            "A teenager":1/40,
            "Cat":1/4.5,
            "Mouse":1/0.030,
            "Dog":1/27,
            "Cow":1/635,
            "Elephant":1/5443,
            "Giraffe":1/1927,
            "Emperor Penguin":1/40,
            "Maui's Dolphin":1/45,
            "Blue whale":1/150000,
            "Brontosaurus":1/30600,
            "T-rex":1/8845},
  'time':{"hour" : 1,
         "minute" : 60,
         "second" : 60*60,
          "day" : 1/24,
          "week" : 1/24*7,
          "month" : 1/24*7*4,
          "year" : 1/24*7*4*12,
          "decade" : 1/24*7*4*12*10,
          "century" : 1/24*7*4*12*10*10,
          "cat year" : 1/(24*365*5)},
    "calories" : {"fries" : 319,
                  "donut" : 319/190,
                  "burger" : 319/290,
                  "ice cream" : 319/207,
                  "apple" : 319/52.1,
                  "banana" : 319/88.1,
                  "cabbage" : 319/24.6,
                  "coke" : 319/139}}

col1,col2,col3,col4,col5 = st.columns(5)
#category selection
with col1:
  st.write("Category")
  category_list = list(conversion_factors.keys())
  category = st.radio("Select Category",options=category_list)

with col2:
  base_factor = st.write("Input")
  input_number = st.number_input("Enter Number")

with col3:
  base_unit_list = list(conversion_factors[category].keys())
  base_unit = st.radio("From:",options=base_unit_list)
  base_cf = conversion_factors[category][base_unit]

with col4:
  target_unit_list = list(conversion_factors[category].keys())
  target_unit = st.radio("To:",options=target_unit_list)
  target_cf = conversion_factors[category][target_unit]

with col5:
  st.write("output")
  output_value = input_number / base_cf * target_cf
  st.write(f'The {category} of {input_number} {base_unit} equals to {output_value:.2f} {target_unit}')
