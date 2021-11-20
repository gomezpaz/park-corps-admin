import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk


def app(self):
    st.header("Map")

    location_coords = GetCoordinates(self.parking_spaces_master)

    df = pd.DataFrame(
        location_coords,
        columns=['lat', 'lon', 'available', 'not_available', 'id', 'name', 'rules'])

    deck = pdk.Deck(
        map_style='mapbox://styles/mapbox/light-v9',
        initial_view_state=pdk.ViewState(
            latitude=40.24498472860159,
            longitude=-111.65600451105257,
            zoom=20,
            pitch=50,
        ),
        layers=[
            pdk.Layer(
                'ScatterplotLayer',
                data=df,
                get_position='[lon, lat]',
                get_fill_color=[0, 255, 0, 140],
                get_radius='available',
                pickable=True,
            ),
            pdk.Layer(
                'ScatterplotLayer',
                data=df,
                get_position='[lon, lat]',
                get_fill_color=[255, 0, 0, 140],
                get_radius='not_available',
                pickable=True,
            ),
            pdk.Layer(
                type='TextLayer',
                id='text-layer',
                data=df,
                pickable=True,
                get_position='[lon, lat]',
                billboard=False,
                get_size=18,
                get_angle=0,
                # get_text_anchor='"middle"',
                # get_alignment_baseline='"center"'
            ),
        ],
        tooltip={"html": "{name}<br/>ID: {id}<br/>Notes: <br/>{rules}"}
    )

    st.pydeck_chart(deck)


def GetCoordinates(parking_spaces):
    location_coords = []
    for index, row in parking_spaces.iterrows():
        location_coord = []
        location_coord.append(float(row['latitude'])+0.00002)
        location_coord.append(float(row['longitude'])+0.00005)
        location_coord.append(int(row['available']))
        location_coord.append(int(not int(row['available'])))
        location_coord.append(int(row['id']))
        location_coord.append(str(row['name']))
        location_coord.append(str(row['rules']))
        location_coords.append(location_coord)

    return location_coords
