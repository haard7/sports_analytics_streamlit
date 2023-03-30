import streamlit as st
import pandas as pd
import numpy as np
import plotly.figure_factory as ff
import matplotlib.pyplot as plt
import base64
import matplotlib.dates as mdates
import seaborn as sns



@st.cache_data
def load_data_2(nrows):
    NBA_Data =  pd.read_csv("NBA_Games2.csv")
    return NBA_Data


# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading data...')
# Load 10,000 rows of data into the dataframe.

# shot = load_data(100)
NBA_Data = load_data_2(100)
# Notify the reader that the data was successfully loaded.
data_load_state.text("Done! (using st.cache_data)")



st.write("### correlation analysis", unsafe_allow_html=True)

res2 = st.selectbox('Select the team nickname', NBA_Data['NICKNAME'].unique())
Pistons_Games=NBA_Data[(NBA_Data.NICKNAME == res2)&(NBA_Data.SEASON_ID==22017)& (NBA_Data.GAME_DATE>='2017-10-17')]

st.set_option('deprecation.showPyplotGlobalUse', False)
# Create a regression plot
sns.regplot(x='AST', y='FGM', data=Pistons_Games, marker='.')

# Set x and y axis labels and title
plt.xlabel('Assists')
plt.ylabel('Field Goals Made')
plt.title("Relationship between the Numbers of Assists and Field Goals Made", fontsize=15)

# Show plot in Streamlit app
st.pyplot()