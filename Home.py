import streamlit as st
from source.pages.header import *
from config import *
from utils.functions import *

st.set_page_config(
        page_title="CLIMADE AFRICA DASHBOARD",
        layout="wide",
        initial_sidebar_state="expanded",
        page_icon="img/cropped-ceri_branco-01-150x150.png"
    )

st.markdown(css_changes, unsafe_allow_html=True)
remote_css('https://fonts.googleapis.com/icon?family=Material+Icons')

st.write("#  Welcome to CLIMADE AFRICA DASHBOARD!")

st.sidebar.success("Select an arbovirus above.")