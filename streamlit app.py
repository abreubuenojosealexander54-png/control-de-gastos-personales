import streamlit as st

st.title("💰 Control de Gastos")

# Ingreso
ingreso = st.number_input("Ingrese sus ingresos:", min_value=0.0)

# Lista de gastos en memoria
if "gastos" not in st.session_state:
    st.session_state.gastos = []

# Agregar gasto
st.subheader("Agregar gasto")

categoria = st.text_input("Categoría")
monto = st.number_input("Monto", min_value=0.0)

if st.button("Agregar"):
    gasto = {"categoria": categoria, "monto": monto}
    st.session_state.gastos.append(gasto)

# Mostrar gastos
st.subheader("📋 Lista de gastos")
for g in st.session_state.gastos:
    st.write(f"{g['categoria']} : {g['monto']}")

# Total
total = sum(g["monto"] for g in st.session_state.gastos)
st.write("### Total gastado:", total)

# Comparación
if total > ingreso:
    st.error("⚠️ Gastas más de lo que ganas")
elif total == ingreso:
    st.warning("😐 Estás justo")
else:
    st.success("✅ Vas bien")
