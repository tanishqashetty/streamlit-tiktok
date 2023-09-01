import streamlit as st
import pandas as pd
from subprocess import call
import plotly.express as px


df=pd.read_csv("tiktokdata.csv")

hashtag= st.text_input('Search for a hashtag here', value="")


if st.button('Get Data'):
    st.write(hashtag)
