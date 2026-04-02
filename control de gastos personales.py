# Vas a crear un programa que:
# Registre gastos
# Muestre el total gastado
# Diga si te pasaste de tu presupuesto

ingreso = float(input("Ingrese sus ingresos: "))

gastos = []
continuar = "si"

while continuar == "si":
    categoria = input("Ingrese la categoría (comida, transporte, etc): ")
    monto = float(input("Ingrese el gasto: "))
    
    gasto = {"categoria": categoria, "monto": monto}
    gastos.append(gasto)
    
    continuar = input("¿Desea agregar otro gasto? (si/no): ").lower()

# Mostrar gastos
print("\n📋 Lista de gastos:")
for g in gastos:
    print(g["categoria"], ":", g["monto"])

# Calcular total
total = sum(g["monto"] for g in gastos)
print("\nTotal gastado:", total)

# Comparación
if total > ingreso:
    print("⚠️ Gastas más de lo que ganas")
elif total == ingreso:
    print("😐 Estás justo")
else:
    print("✅ Vas bien")

