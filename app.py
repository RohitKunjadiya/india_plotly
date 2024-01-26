import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st

df = pd.read_csv('india.csv')

state = list(df['State'].unique())
state.insert(0,'overall india')

st.set_page_config(layout='wide')

st.sidebar.title('Census Data Visualization-2011')

selected_state = st.sidebar.selectbox('State of India',state)
primary = st.sidebar.selectbox('Select primary parameter',df.columns[5:])
secondary = st.sidebar.selectbox('Select secondary parameter',df.columns[5:])

plot = st.sidebar.button('Plot Graph')

if plot:
    st.text('Size represent primary parameter')
    st.text('Color represent secondary parameter')
    if selected_state == 'overall india':
        #plot for india
        fig = px.scatter_mapbox(df, lat='Latitude', lon='Longitude', mapbox_style='carto-positron',
        size=primary,color=secondary,size_max=35, zoom=3.5,width=1200,height=700)

        st.plotly_chart(fig,use_container_width=True)
    else:
        #plot for selected state
        state_df = df[df['State'] == selected_state]
        fig = px.scatter_mapbox(state_df, lat='Latitude', lon='Longitude',size=primary,color=secondary,mapbox_style='carto-positron',
                                size_max=35, zoom=6,width=1200,height=700)

        st.plotly_chart(fig,use_container_width=True)