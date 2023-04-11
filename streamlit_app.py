import streamlit
streamlit.title('🥣 My Parents New Healthy Life Style')
streamlit.header('🥗 Breakfast Menu')
streamlit.text('🐔 🍞Idly & Puri with curries and chutney')
streamlit.text('🥗  Spinach and Beetroot')
streamlit.text('Yoga and walk every day for 45 mins')
streamlit.text('🥑Avacado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')


import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

streamlit.dataframe(my_fruit_list)








