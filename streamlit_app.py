import streamlit as st
import pandas as pd
import numpy as np

st.title("My Parents New Healthy Diner")

st.header('Breakfast Menu')
st.text(' 🥣 Omega 3 & Blueberry Oatmeal')
st.text(' 🥗 Kale, Spinach & Rocket Smoothie')
st.text(' 🐔 Hard-Boiled Free-Range Egg')
st.text(' 🥑🍞 Avacado Toast')
        
st.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

df =  pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
st.dataframe(df)
