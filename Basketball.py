import streamlit as st
import pandas as pd
import numpy as np
import plotly.figure_factory as ff
import matplotlib.pyplot as plt
import base64
import matplotlib.dates as mdates
import seaborn as sns
import lxml

hide_menu = """ 
<style>
    #MainMenu{
    visibility: hidden;
    }

    footer{
        visibility: visible;
    }
    footer:after{
        content: 'Copyright @ 2023: Haard, Khanjan and Femil';
        display: block;
        position: relative;
        color: tomato;
    }
</style>
"""

st.set_page_config(
    page_title="L_1_Sports_Analytics",
    page_icon="🥇",
)


st.subheader('Basketball player and ground analysis')
st.markdown(hide_menu,unsafe_allow_html=True)
st.sidebar.success("Select the page")
@st.cache_data
def load_data(nrows):
    shot = pd.read_csv("NBA Shotlog_16_17.csv")
    return shot

@st.cache_data
def load_data_2(nrows):
    NBA_Data =  pd.read_csv("NBA_Games2.csv")
    return NBA_Data

# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading data...')
# Load 10,000 rows of data into the dataframe.

shot = load_data(100)
NBA_Data = load_data_2(100)
# Notify the reader that the data was successfully loaded.
data_load_state.text("Done! (using st.cache_data)")

if st.checkbox('Show raw data', key='checkbox1'):
    st.subheader('Raw data')
    st.write(shot)


# Heatmap of whole data
x = shot['location_x']
y = shot['location_y']

fig, ax = plt.subplots()
ax.scatter(x, y, s=0.005, c='r', marker='.')
ax.set_xlabel('location_x')
ax.set_ylabel('location_y')

st.pyplot(fig)


#missed/shots of any searched player - Heatmaps 

shot['halfcourt_x'] =np.where(shot['location_x'] < 933/2, 933 - shot['location_x'],shot['location_x'])
shot['halfcourt_y'] =np.where(shot['location_x'] < 933/2, 500 - shot['location_y'],shot['location_y'])


st.write("### Individual player Shots analysis", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    res = st.selectbox('Select the player name', shot['shoot_player'].unique())
    # LeBron = shot[shot['shoot_player']=='LeBron James']
    result = shot[shot['shoot_player'] == res]
    # Create scatter plot


    
    hxL = result['halfcourt_x']
    hyL = result['halfcourt_y']
    colors = np.where(result['current_shot_outcome']=='SCORED','r',np.where(result['current_shot_outcome']=='MISSED','b','g'))
    fig, ax = plt.subplots(figsize=(70/8,40/6))
    # standard size: (figsize=(94/12,50/6)) 
    ax.scatter(hxL,hyL, s=10, c= colors, marker= '.')
    ax.grid(True)
    ax.set_title(res, fontsize = 15)
    # Display plot in Streamlit app
    st.pyplot(fig)

    # hxL = LeBron['halfcourt_x']
    # hyL = LeBron['halfcourt_y']
    # colors = np.where(LeBron['current_shot_outcome']=='SCORED','r',np.where(LeBron['current_shot_outcome']=='MISSED','b','g'))
    # fig, ax = plt.subplots(figsize=(70/8,40/6))
    # # standard size: (figsize=(94/12,50/6)) 
    # ax.scatter(hxL,hyL, s=10, c= colors, marker= '.')
    # ax.grid(True)
    # ax.set_title("LeBron James", fontsize = 15)
    # # Display plot in Streamlit app
    # st.pyplot(fig)

with col2:
    # st.markdown("&nbsp;", unsafe_allow_html=True)
    
    # st.markdown("<div style='margin-left: 50px;'>", unsafe_allow_html=True)
    st.markdown("<br><br><br><br>", unsafe_allow_html=True)
    st.markdown(":red[Red]: scored, :blue[Blue]: missed")

    
    player = shot[shot['shoot_player'] == res]

    Missed = player[player.current_shot_outcome == 'MISSED'].shape[0]
    Scored = player[player.current_shot_outcome == 'SCORED'].shape[0]
    Blocked =player[player.current_shot_outcome == 'BLOCKED'].shape[0]
    total = Missed+Scored+Blocked

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<div style='padding-left: 20px;'>", unsafe_allow_html=True)
    st.write(f'**Total shots:** {total}')
    st.write(f'**Missed: shots:** {Missed}')
    st.write(f'**Scored shots:** {Scored}')
    st.write(f'**Blocked shots:** {Blocked}')

    st.markdown("</div>", unsafe_allow_html=True)


# Time-series analysis on different data
st.write("### Time-series analysis", unsafe_allow_html=True)


if st.checkbox('Show raw data 2', key='checkbox2'):
    st.subheader('Raw data')
    st.write(NBA_Data)


res2 = st.selectbox('Select the team nickname', NBA_Data['NICKNAME'].unique())
Pistons_Games=NBA_Data[(NBA_Data.NICKNAME == res2)&(NBA_Data.SEASON_ID==22017)& (NBA_Data.GAME_DATE>='2017-10-17')]

# Convert the GAME_DATE column to datetime format
Pistons_Games['GAME_DATE'] = pd.to_datetime(Pistons_Games['GAME_DATE'])

# Set the index to GAME_DATE
Pistons_Games.set_index('GAME_DATE', inplace=True)

# Create a new figure and axis
fig, ax = plt.subplots()

# Plot data
ax.plot(Pistons_Games['PTS'])

# Format the x-axis ticks to show one tick per month
ax.xaxis.set_major_locator(mdates.MonthLocator(interval=1))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))

# Set x and y axis labels
ax.set_xlabel('Date')
ax.set_ylabel('Points')

# Show plot in Streamlit app
st.pyplot(fig)

# Save the plot
fig.savefig('PISTONS_PTS_TIME.png')

# st.line_chart(Pistons_Games[['GAME_DATE', 'PTS']].set_index('GAME_DATE'))

# # Save the plot
# fig = plt.gcf()
# fig.savefig('PISTONS_PTS_TIME.png')
# # display(Pistons_Games)



# st.write("### correlation analysis", unsafe_allow_html=True)

# st.set_option('deprecation.showPyplotGlobalUse', False)
# # Create a regression plot
# sns.regplot(x='AST', y='FGM', data=NBA_Data, marker='.')

# # Set x and y axis labels and title
# plt.xlabel('Assists')
# plt.ylabel('Field Goals Made')
# plt.title("Relationship between the Numbers of Assists and Field Goals Made", fontsize=15)

# # Show plot in Streamlit app
# st.pyplot()