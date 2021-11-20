from os import write
import streamlit as st
from streamlit_webrtc import webrtc_streamer, WebRtcMode, RTCConfiguration
import streamlit.components.v1 as components
import hydralit as hy
# from computervision.motiontracker import VideoProcessor
import pandas as pd
import numpy as np

from pages.multipage import MultiPage
from pages import database, map, logger

# Create an instance of the app
app = MultiPage()

# Title of the main page
st.title("Park Corps")

app.add_page("Raw Database", database.app)
# app.add_page("Map", map.app)
app.add_page("Logger", logger.app)

try:
    app.run()
except:
    pass
