import streamlit
streamlit.title('🥣 My Parents New Healthy Life Style')
streamlit.header('🥗 Breakfast Menu')
streamlit.text('🐔 🍞Idly & Puri with curries and chutney')
streamlit.text('🥗  Spinach and Beetroot')
streamlit.text('Yoga and walk every day for 45 mins')
streamlit.text('🥑Avacado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)


import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)


