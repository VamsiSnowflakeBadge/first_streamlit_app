import streamlit
streamlit.title('🥣 My Parents New Healthy Life Style')
streamlit.header('🥗 Breakfast Menu')
streamlit.text('🐔 🍞Idly & Puri with curries and chutney')
streamlit.text('🥗  Spinach and Beetroot')
streamlit.text('Yoga and walk every day for 45 mins')
streamlit.text('🥑Avacado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
streamlit.dataframe(my_fruit_list)


import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit') 

fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocodo','Strawberries'])
fruits_to_show = my_fruit_list.Loc[fruits_selected] 
streamlit.dataframe(fruits_to_show)





