import requests 
import streamlit as st
# import pandas as pd
# import numpy as np


st.title('Aplicación de IRIS en Acámica con FastAPI')

lon_petalo = st.text_input("Seleccione la lonitud del petalo", 0)
lon_hoja = st.text_input("Seleccione la lonitud de la hoja", 0)
ancho_petalo = st.text_input("Seleccione el ancho del pétalo", 0)
ancho_hoja = st.text_input("Seleccione el ancho de la hoja", 0)


new_measurement = {
    'sepal_length': lon_hoja,
    'sepal_width': ancho_hoja,
    'petal_length': lon_petalo,
    'petal_width': ancho_petalo
}


response = requests.post('http://127.0.0.1:8000/predict', json=new_measurement)

respuesta = str(response.content)

st.text("El tipo de flor predicha es: " + respuesta)




