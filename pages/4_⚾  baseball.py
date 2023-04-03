import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

st.subheader('Baseball  ground analysis')
# st.markdown(hide_menu,unsafe_allow_html=True)
# st.sidebar.success("Select the page")
@st.cache_data
def load_data(nrows):
    data = pd.read_csv("MLBAM18.csv")
    return data

# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading data...')
# Load 10,000 rows of data into the dataframe.

# shot = load_data(100)
data = load_data(100)
# Notify the reader that the data was successfully loaded.
data_load_state.text("Done! (using st.cache_data)")

# shot = load_data(100)

# Notify the reader that the data was successfully loaded.


# Limiting the set of variables

MLBmap = data[['gameId','home_team','away_team','stadium','inning', 'batterId', 'batterName',\
                  'pitcherId', 'pitcherName','event','timestamp','stand', 'throws','x','y','our.x','our.y']]



if st.checkbox('Show raw data', key='checkbox1'):
    st.subheader('Raw data')
    st.write(MLBmap)


# Analysis below

single_checked = st.checkbox('Single', key='single')
double_checked = st.checkbox('Double', key = 'double')
triple_checked  = st.checkbox('Triple', key = 'triple')
home_run_checked  = st.checkbox('Home Run', key = 'home run')
all_combined = st.checkbox('combined All' , key = 'all')

if single_checked:
    # Create scatter plot\
    Single = MLBmap[MLBmap.event == 'Single']
    fig, ax = plt.subplots(figsize=(3, 2))
    ax.scatter(Single['our.x'], Single['our.y'], s=.005, c='darkorange', marker='.')
    ax.set_xlabel('our.x')
    ax.set_ylabel('our.y')
    ax.set_title('Scatter Plot of Singles')
    st.pyplot(fig)
# Display plot in Streamlit app
if double_checked:
    Double = MLBmap[MLBmap.event == 'Double']
    fig, ax = plt.subplots(figsize=(3, 2))
    ax.scatter(Double['our.x'], Double['our.y'], s=.02, c='darkblue', marker='.')
    ax.set_xlabel('our.x')
    ax.set_ylabel('our.y')
    ax.set_title('Scatter Plot of Doubles')
    st.pyplot(fig)

if triple_checked:
    Triple = MLBmap[MLBmap.event == 'Triple']
    fig, ax = plt.subplots(figsize=(3, 2))
    ax.scatter(Triple['our.x'], Triple['our.y'], s=.02, c='g', marker='.')
    ax.set_xlabel('our.x')
    ax.set_ylabel('our.y')
    ax.set_title('Scatter Plot of Doubles')
    st.pyplot(fig)

if home_run_checked:
    Homer = MLBmap[MLBmap.event == 'Home Run']
    fig, ax = plt.subplots(figsize=(3, 2))
    ax.scatter(Homer['our.x'], Homer['our.y'], s=.02, c='m', marker='.')
    ax.set_xlabel('our.x')
    ax.set_ylabel('our.y')
    ax.set_title('Scatter Plot of Doubles')
    st.pyplot(fig)

if all_combined:
    Single = MLBmap[MLBmap.event == 'Single']
    Double = MLBmap[MLBmap.event == 'Double']
    Triple = MLBmap[MLBmap.event == 'Triple']
    Homer = MLBmap[MLBmap.event == 'Home Run']
    fig, axs = plt.subplots(1, 4, figsize=(15, 3))

    #Create scatter plot for each type of hit
    axs[0].scatter(Single['our.x'], Single['our.y'], s=0.01, c='darkorange', marker='.')
    axs[0].set_ylim((0, 500))
    axs[0].set_title('Singles')
    axs[1].scatter(Double['our.x'], Double['our.y'], s=0.1, c='dodgerblue', marker='.')
    axs[1].set_ylim((0, 500))
    axs[1].set_title('Doubles')
    axs[2].scatter(Triple['our.x'], Triple['our.y'], s=1, c='g', marker='.')
    axs[2].set_ylim((0, 500))
    axs[2].set_title('Triples')
    axs[3].scatter(Homer['our.x'], Homer['our.y'], s=0.5, c='m', marker='.')
    axs[3].set_ylim((0, 500))
    axs[3].set_title('Home Runs')
    # Display plot in Streamlit app
    st.pyplot(fig)








