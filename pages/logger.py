import streamlit as st
from streamlit_autorefresh import st_autorefresh
from gsheetsdb import connect
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime
from streamlit_webrtc import webrtc_streamer, WebRtcMode, RTCConfiguration

from .computervision.motiontracker import VideoProcessor


def app(self):
    st.header("Security Camera Gateway")

    # Set up RTC config for https protocol
    RTC_CONFIGURATION = RTCConfiguration(
        {"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]}
    )

    # Authorize the API
    scope = [
        'https://www.googleapis.com/auth/drive',
        'https://www.googleapis.com/auth/drive.file'
    ]
    file_name = 'client_key.json'
    creds = ServiceAccountCredentials.from_json_keyfile_name(file_name, scope)
    client = gspread.authorize(creds)

    # Fetch the sheet
    try:
        sheet = client.open('parkcorps-master').sheet1
    except:
        pass
    name = st.selectbox('Parking Spot Selection',
                        self.parking_spaces_master['name'])

    st.write('You selected: ', name)

    webrtc_ctx = webrtc_streamer(
        key="motion-tracker",
        mode=WebRtcMode.SENDRECV,
        rtc_configuration=RTC_CONFIGURATION,
        video_processor_factory=VideoProcessor,
        media_stream_constraints={"video": True, "audio": False},
        async_processing=True,
    )


def UpdateAvailability(sheet, name, value):
    UpdateValue(sheet, name, "available", value)
    timestamp = datetime.now().strftime("%m/%d/%Y %I:%M:%S")
    UpdateValue(sheet, name, "timestamp", timestamp)


def UpdateValue(sheet, name, column_name, value):
    cell = sheet.find(str(name), in_column=2)
    row = cell.row
    cell = sheet.find(str(column_name), in_row=1)
    col = cell.col
    sheet.update_cell(row, col, str(value))


def GetValue(self, name, value):
    string = self.parking_spaces_master.loc[self.parking_spaces_master['name']
                                            == name, value].to_string()

    string_array = string.split(' ')

    new_array = []
    for i in string_array[1:]:
        if i != '':
            new_array.append(i)

    return str(" ".join(new_array))
