
producto = input("Introduce el nombre del producto: ")
precio = float(input("Introduce el precio unitario del producto: "))
unidades = int(input("Introduce el número de unidades: "))

total = precio * unidades

print(f"{producto}: precio unitario {precio:09.2f}, unidades {unidades:03d}, coste total {total:011.2f}")

#f quiere decir que es el principio de una cadena

# :09 es el número total de caracteres
# .2f es el numero de digitos decimales

