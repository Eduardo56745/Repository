import streamlit as st
import pandas as pd
import plotly.express as px

car_data = pd.read_csv('vehicles_us.csv')

st.header('Analisis de datos de venta de choches')
# Crear un botón para el histograma
hist_button = st.button('Construir un histograma')
# Crear un botón para el diagrama de dispersión
scatter_button = st.button('Construir un diagrama de dispersión')

if hist_button:
    # mostrar el mensaje
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    fig = px.histogram(car_data, x='odometer')  # crear un histograma

    st.plotly_chart(fig, use_container_width=True)  # gráfico interactivo

if scatter_button:
    st.write('Creación de un grafico de dispersión para el conjunto de datos de anuncios de venta de coches')

    fig = px.scatter(car_data, x='odometer', y='price')

    st.plotly_chart(fig, use_container_width=True)
