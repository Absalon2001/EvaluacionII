#funcion para validar nombre del trabajador
nombre_trabajador = input("Por favor ingrese su nombre del trabajador: \n")
while len(nombre_trabajador.strip()) == 0 or len(nombre_trabajador) > 10:
    print("Nombre inválido\n")
    nombre_trabajador = input("Por favor ingrese su nombre del trabajador: \n")

sueldo_base = float(input("Ingrese el sueldo base del trabajador: "))
while sueldo_base <= 0:
    print("Error: Ingrese un sueldo válido\n")
    sueldo_base = float(input("Ingrese el sueldo base del trabajador: "))

horas_extras_del_mes = float(input("Ingrese las horas extras trabajadas durante el mes: "))
while horas_extras_del_mes < 0:
    print("Error: Ingrese horas válidas\n")
    horas_extras_del_mes = float(input("Ingrese las horas extras trabajadas durante el mes: "))
#Calculo de pagos
pago_horas_EXTRAS = sueldo_base / 160 * 1.50 * horas_extras_del_mes
total_ingresos_mensual = pago_horas_EXTRAS + sueldo_base
seguridad_social_descuentos = total_ingresos_mensual * 0.07 + total_ingresos_mensual * 0.1
sueldo_neto_pagar = total_ingresos_mensual - seguridad_social_descuentos
#Imprimir liquidacion
print("\n--- Liquidación ---")
print(f"Nombre del trabajador: {nombre_trabajador}\nSueldo base: ${sueldo_base:,.2f}\nPago por cada hora extra: ${pago_horas_EXTRAS:,.2f}\nTotal ingresos mensuales: ${total_ingresos_mensual:,.2f}\nDescuentos por seguridad social: ${seguridad_social_descuentos:,.2f}\nSueldo neto a pagar: ${sueldo_neto_pagar:,.2f}")
#Generar archivo de liquidacion
nombre_archivo = f"liquidacion_{nombre_trabajador}.txt"
with open(nombre_archivo, "w") as documento:
    documento.write(f"DATOS DE LIQUIDACIÓN DE {nombre_trabajador}\n\n")
    documento.write(f"Nombre del trabajador: {nombre_trabajador}\nSueldo base: ${sueldo_base:,.2f}\nPago por cada hora extra: ${pago_horas_EXTRAS:,.2f}\nTotal ingresos mensuales: ${total_ingresos_mensual:,.2f}\nDescuentos por seguridad social: ${seguridad_social_descuentos:,.2f}\nSueldo neto a pagar: ${sueldo_neto_pagar:,.2f}\n")

print(f"\nArchivo de liquidación generado: {nombre_archivo}")