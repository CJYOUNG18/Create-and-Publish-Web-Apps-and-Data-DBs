import streamlit as st
import pandas


data = {
    'Series_1':[1, 3, 4, 5, 7],
    'Series_2':[10, 30, 40, 100, 250]
}

df = pandas.DataFrame(data)
st.title('Our First Streamlit App')
st.subheader('Introducing Streamlit and Automate with Python')
st.write("""This is our first Web App.
Enjoy it!
""")
st.write(df)