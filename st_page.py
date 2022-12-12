#Import packages
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import seaborn as sns
import numpy as np
import streamlit.components.v1 as components
from streamlit_option_menu import option_menu
import leafmap.foliumap as leafmap
from statsmodels.formula.api import ols

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
st.markdown("<h4 style='text-align: center; color: grey;'>Opdracht uitgevoerd door gemaakt door: Dinand Kruger, Thijs van den Berg en Thomas van Meerveld</h4>", unsafe_allow_html=True)

#Import datasets



# Nav bar 
selected = option_menu(
    menu_title=None,  
    options=["pagina 1","pagina 2", "pagina 3", "pagina 4"],  
    icons=["globe", "bar-chart","map", "bezier"],   
    default_index=0,  
    orientation="horizontal",
)

#Page one
if selected == "pagina 1":
    components.html(
    """
        <div style="text-align: center">
            <a href="https://fast.com" target="_blank" class="button">test🔗</a>
            
            </div>
    """
    """
        <div style="text-align: center">
            
            <a href="https://fast.com" target="_blank" class="button">test🔗</a>
            </div>
    """
    , height= 72)

    #sidebar
    _id = st.sidebar.slider('test', 1 , 231, 10)

#Page two
if selected == "pagina 2":  
    st.write('')

#Page three
if selected == "pagina 3":
    st.write('')

#Page four
if selected == "pagina 4":
    st.write('')