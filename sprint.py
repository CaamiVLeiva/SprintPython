import random
import string

#Elaborar un programa que recorra una lista con los nombres de 10 de sus futuros usuarios de tu
#aplicación (pueden ser personas, pacientes, organizaciones sociales o instituciones públicas).
usuarios = ["John Doe", "Alice Smith", "Michael Johnson", "Emily Brown", "Daniel Wilson",        
            "Olivia Davis", "David Martinez", "Sophia Taylor", "Matthew Anderson", "Emma Thomas"]

cuentas = {}

#● Mediante una función, a todos los usuarios se les creará una cuenta automáticamente.
def crear_cuenta(usuario):
    caracteres = string.ascii_lowercase + string.ascii_uppercase + string.digits
    #● Asigne una contraseña para cada cuenta. La contraseña debe ser creada con random y debe
    #cumplir con los siguientes criterios: mayúsculas, minúsculas y números.
    password = ''.join(random.choice(caracteres) for _ in range(8))
    telefono = input(f"Ingrese el número telefónico para {usuario}: ")
    #● El programa no terminará de preguntar por los números hasta que todas las organizaciones
    #tengan un número de contacto asignado.
    while len(telefono) != 8 or not telefono.isdigit():
        #● El programa debe verificar que el número telefónico tenga 8 dígitos numéricos.
        print("El número telefónico debe tener 8 dígitos numéricos.")
        #● Por cada cuenta debe pedir un número telefónico para contactarse.
        telefono = input(f"Ingrese el número telefónico para {usuario}: ")
        print("------------------------")
    return (password, telefono)

for usuario in usuarios:
    cuenta = crear_cuenta(usuario)
    cuentas[usuario] = cuenta

# Imprimir las cuentas creadas
for usuario, cuenta in cuentas.items():
    print(f"Nombre usuario: {usuario}")
    print(f"Contraseña: {cuenta[0]}")
    print(f"Número telefónico: {cuenta[1]}")
    print("***************************")