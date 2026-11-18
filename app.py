import pandas as pd
import streamlit as st

st.title("Una semana en la heladería")
st.write("Explora siete días de ventas ficticias. Cada fila representa un día.")
datos = pd.read_csv("helados.csv")
datos["total"] = datos["vainilla"] + datos["chocolate"]
st.dataframe(datos, hide_index=True)
st.caption("Temperatura en °C. Las ventas se miden en helados.")

# El control devuelve el nombre de una columna de la tabla.
sabor = st.selectbox("Elige el sabor para las gráficas 1, 3 y 5", ["vainilla", "chocolate"])

st.subheader("1 · ¿Cuántos helados de ese sabor se vendieron cada día?")
horizontal = st.checkbox("Ver barras horizontales")
st.bar_chart(datos, x="dia", y=sabor, horizontal=horizontal)
st.caption("Cada barra representa un día. Busca la más larga.")

st.subheader("2 · ¿Cómo cambiaron las ventas de ambos sabores?")
st.line_chart(datos, x="dia", y=["vainilla", "chocolate"])
st.caption("Sigue cada línea de izquierda a derecha. Su color indica el sabor.")

st.subheader("3 · ¿Qué pasó con las ventas en los días más cálidos?")
st.scatter_chart(datos, x="temperatura", y=sabor)
st.caption("Cada punto es un día. Más a la derecha significa más calor y más arriba, más ventas.")

st.subheader("4 · ¿Cuántos helados se vendieron en total cada día?")
st.area_chart(datos, x="dia", y="total")
st.caption("La altura del área indica la suma de ambos sabores en ese día.")

st.subheader("5 · ¿Cuántos helados llevábamos vendidos al cierre de cada día?")
datos["acumulado"] = datos[sabor].cumsum()
st.line_chart(datos, x="dia", y="acumulado")
st.caption(f"El último punto suma todas las ventas de {sabor} de la semana.")
