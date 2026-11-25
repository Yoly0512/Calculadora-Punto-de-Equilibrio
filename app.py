import streamlit as st

st.title("🧮 Calculadora de Punto de Equilibrio")
st.write("Calcula cuantas unidades debes vender para no ganar ni perder.")

costos_fijos = st.number_input("Costos Fijos ($)", value=1000000.0, step=1000.0)
precio = st.number_input("Precio de Venta ($)", value=50000.0, step=1000.0)
costo_variable = st.number_input("Costo Variable por unidad ($)", value=30000.0, step=1000.0)

if st.button("Calcular"):
    margen = precio - costo_variable
    if margen <= 0:
        st.error("El precio debe ser mayor que el costo variable.")
    else:
        pe_unidades = costos_fijos / margen
        pe_pesos = pe_unidades * precio
        st.success(f"Punto de Equilibrio en Unidades: {pe_unidades:.0f} unidades")
        st.success(f"Punto de Equilibrio en Pesos: ${pe_pesos:,.0f}")
        st.info(f"Margen por unidad: ${margen:,.0f}")
