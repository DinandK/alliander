#Import packages
import streamlit as st
import matplotlib.pyplot as plt
from streamlit_folium import st_folium
import folium
import pandas as pd
import seaborn as sns
import streamlit.components.v1 as components
from streamlit_option_menu import option_menu
from PIL import Image


#loading plots
with open('24uuranalyse.html') as source2:
    design2 = source2.read()
with open('averages1to247.html') as source3:
    design3 = source3.read()
with open('averages1to52.html') as source4:
    design4 = source4.read()            


#Style
st.set_page_config(
    page_title="Presentatie Alliander",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state = 'collapsed',
)

#Title
st.markdown("<h1 style='text-align: center; color: grey;'>⚡Dashboard Alliander⚡</h1>", unsafe_allow_html=True)

#Create header
st.markdown("<h4 style='text-align: center; color: grey;'>Opdracht uitgevoerd door: Dinand Kruger, Thijs van den Berg en Thomas van Meerveld</h4>", unsafe_allow_html=True)

#import datasets
measurements  = pd.read_csv('measurements_2.csv')
names = pd.read_csv('names.csv')


# Nav bar 
selected = option_menu(
    menu_title=None,  
    options=["Data","Map"],  
    icons=["activity", "globe","bezier"],   
    default_index=0,  
    orientation="horizontal",
)

#Page one
if selected == "Data":
    col1, col2, col3 = st.columns([1,6,1])

    with col1:
        st.write("")

    with col2:
        components.html(design2, height=500)
        components.html(design3, height=500)
        components.html(design4, height=500)

    with col3:
        st.write("")

#Page two
if selected == "Map":
    components.iframe("https://lemon-smoke-0c2fad103.2.azurestaticapps.net/",height= 800)
    
    col1, col2, col3 = st.columns([4,8,4])
    with col1:
        st.write('')
    with col2:
        fig = plt.figure(figsize=(10, 4))
        input1 = st.selectbox('Selecteer het ID in van uw middenspanningsruimte', names.names)
        if input1 == "":
            input1 = '1af6b926-ad76-5af7-91a1-aac1f3fa6e31'
        sns.lineplot(x = 'Uur', y = input1, data = measurements, color="purple").set(title='Verbruik [KWH] per uur')
        plt.ylabel('Verbruik [KWH]')
        st.pyplot(fig)
        fig, ax = plt.subplots(figsize=(10, 4))
        sns.lineplot(x = 'Dag van de Week', y = input1, data = measurements, color="purple").set(title='Verbruik [KWH] per dag van de week')
        plt.ylabel('Verbruik [KWH]')
        plt.xticks([0,1,2,3,4,5,6])
        ax.set_xticklabels(['Maa','Din','Woe','Don','Vri','Zat','Zon'])
        st.pyplot(fig)
        fig = plt.figure(figsize=(10, 4))
        sns.lineplot(x = 'Dag van de Maand', y = input1, data = measurements, color="purple").set(title='Verbruik [KWH] per dag van de maand')
        plt.ylabel('Verbruik [KWH]')
        st.pyplot(fig)
    with col3:
        st.write('')


