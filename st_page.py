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
with open('index.html') as source1:
    design1 = source1.read()
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
long_lat = pd.read_excel('locaties.xlsx')
measurements  = pd.read_csv('measurements_2.csv')


# Nav bar 
selected = option_menu(
    menu_title=None,  
    options=["Data","Map", "Confidence interval"],  
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
    #sidebar
    _id = st.sidebar.slider('test', 1 , 231, 10)

#Page two
if selected == "Map":
    components.html(design1)
    input1 = st.text_input('Voer het ID in van uw middenspanningsruimte')
    if input1 == "":
        input1 = '1af6b926-ad76-5af7-91a1-aac1f3fa6e31'
    
    col1, col2, col3 = st.columns([4,8,4])
    with col1:
        st.write('')
    with col2:
        fig = plt.figure(figsize=(10, 4))
        sns.lineplot(x = 'Dag van de Week', y = input1, data = measurements).set(title='Verbruik [KWH] per dag van de week')
        plt.ylabel('Verbruik [KWH]')
        st.pyplot(fig)
        fig = plt.figure(figsize=(10, 4))
        sns.lineplot(x = 'Dag van de Maand', y = input1, data = measurements).set(title='Verbruik [KWH] per dag van de maand')
        plt.ylabel('Verbruik [KWH]')
        st.pyplot(fig)
        fig = plt.figure(figsize=(10, 4))
        sns.lineplot(x = 'Uur', y = input1, data = measurements).set(title='Verbruik [KWH] per uur')
        plt.ylabel('Verbruik [KWH]')
        st.pyplot(fig)
    with col3:
        st.write('')


#    arhnem = [51.954898, 5.849199]
#    m= folium.Map(location=arhnem, zoom_start=12)
#
#    for i in range(0,len(long_lat)):
#        html  = components.html="""
#       <iframe src=\"""" + long_lat['html_file'][i] + """\" width="850" height="400"  frameborder="0">    
#        """
#        popup = folium.Popup(folium.Html(html, script=True))
#        folium.Marker([long_lat['latitude'].iloc[i],long_lat['longitude'].iloc[i]],
#                    popup=popup,icon=folium.Icon( icon='flash', prefix='fa')).add_to(m)
#    m.to_streamlit()

#Page two
if selected == "Confidence interval":
    components.html(design1, height=800)
    DinandLocaties = pd.read_excel('locaties.xlsx')

    DinandLocaties['colour']= (DinandLocaties['html_file'].str.len() == 6)
    DinandLocaties['colour'] = DinandLocaties['colour'].replace(True,'red')
    DinandLocaties['colour'] = DinandLocaties['colour'].replace(False,'green')
    arhnem = [51.954898, 5.849199]
    m= folium.Map(location=arhnem, zoom_start=12)
    for a,b in DinandLocaties.iterrows():
        tekst= """
        <iframe src=\"""" + b['html_file'] + """\" width="850" height="400"  frameborder="0">    
        """

        popup = folium.Popup(folium.Html(tekst, script=True))
        folium.Marker([b['longitude'],b['latitude']],popup=popup,icon=folium.Icon(icon='flash', prefix='fa',color=b['colour'])).add_to(m)
    #st_data =  st_folium(m, width = 1500)