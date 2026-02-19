import pandas as pd
import streamlit as st

# Cargar los datos
df = pd.read_csv('vehicles_us.csv')

# Título de la aplicación
st.title('Análisis de Vehículos')

# Mostrar los primeros datos
st.write('Primeros registros del dataset:')
st.dataframe(df.head())