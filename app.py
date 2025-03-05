import streamlit as st
import pandas as pd
import plotly_express as px

car_data = pd.read_csv('vehicles_us.csv')

st.header('Cuadro de mandos de anuncios de venta de coches')

build_histogram = st.checkbox('Construir histograma')
build_scatter = st.checkbox('Construir diagrama de dispersión')

if build_histogram:
    st.write('Construyendo un histograma para la columna odómetro')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

if build_scatter:
    st.write('Construyendo un diagrama de dispersión para año vs precio')
    fig = px.scatter(car_data, x="year", y="price")
    st.plotly_chart(fig, use_container_width=True)
