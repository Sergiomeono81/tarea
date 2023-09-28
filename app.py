# app.py

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Defininiendo el comportamiento de la Perinola
def lanzar_perinola():
    return np.random.choice(['Resultado del juego', 'Pon 1', 'Pon 2', 'Toma 1', 'Toma 2', 'Toma todo', 'Todos ponen'])

# ... [Todas tus otras funciones se quedan igual]

# Interfaz Streamlit
def main():
    st.title("Simulación de Perinola con Montecarlo")
    
    N = st.slider('Número de jugadores (N):', 2, 10, 4)
    M = st.slider('Número de juegos (M):', 1, 500, 10)
    dinero_inicial = st.slider('Dinero inicial:', 1, 100, 10)

    if st.button('Simular'):
        plot_results(N, M, dinero_inicial)

if __name__ == "__main__":
    main()
