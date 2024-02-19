print("Bienvenido a la calculadora de propinas")

total = float(input("Ingrese el total de la cuenta a pagar? $"))
porcentaje = int(
    input("¿Qué porcentaje de propina te gustaría dar? 10, 12, 0 15? "))
personas = int(input("Ingresar cantidad de personas a pagar: "))

propina_con_porcentaje = porcentaje / 100
total_porcentaje_cantidad = total * propina_con_porcentaje
total_factura = total + total_porcentaje_cantidad
total_por_persona = total_factura / personas
final_cuenta = round(total_por_persona, 2)
final_cuenta = "{:.2f}.format(total_por_persona)"
print(f"Deben pagar cada personas un total: {final_cuenta}")
