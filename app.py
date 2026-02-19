import pandas as pd
import plotly.express as px
import streamlit as st

# leer datos
car_data = pd.read_csv('vehicles_us.csv')

# encabezado
st.header('Dashboard de anuncios de venta de autos')

# -------- HISTOGRAMA --------
hist_button = st.button('Crear histograma')

if hist_button:
    st.write('Creando un histograma del odómetro')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

# -------- SCATTER --------
scatter_button = st.button('Crear gráfico de dispersión')

if scatter_button:
    st.write('Relación entre kilometraje y precio')
    fig2 = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig2, use_container_width=True)

    



