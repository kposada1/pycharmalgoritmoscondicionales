'''En un almacén se hace un 20% de descuento a los clientes cuya compra supere los $1000
¿ Cual será la cantidad que pagara una persona por su compra?'''

compra = int(input("Ingrese el valor de su compra: "))

if compra > 1000:
    desc = compra * 0.20
else:
    desc = 0

totpag = compra - desc
print(f"El total a pagar es: {totpag}")