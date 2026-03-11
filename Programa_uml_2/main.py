from clases import *

us1 = Persona(1, "Mario Hugo", "mario.hugo@example.com")
us2 = Persona(2, "Lucía Fernández", "lucia.fernandez@example.com")
us3 = Persona(3, "Carlos Ramírez", "carlos.ramirez@example.com")
us4 = Persona(4, "Ana Torres", "ana.torres@example.com")
us5 = Persona(5, "Jorge Castillo", "jorge.castillo@example.com")
us6 = Persona(6, "Mariana López", "mariana.lopez@example.com")
us7 = Persona(7, "Ricardo Sánchez", "ricardo.sanchez@example.com")
us8 = Persona(8, "Sofía Martínez", "sofia.martinez@example.com")
us9 = Persona(9, "Andrés Gutiérrez", "andres.gutierrez@example.com")
us10 = Persona(10, "Valeria Domínguez", "valeria.dominguez@example.com")

Usuarios=[
    us1, us2, us3, us4, us5,
    us6, us7, us8, us9, us10
]

emp1 = Empleado("Ana López", "ana.lopez@empresa.com", 1, "Gerente")
emp2 = Empleado("Carlos Pérez", "carlos.perez@empresa.com", 2, "Analista")
emp3 = Empleado("María Torres", "maria.torres@empresa.com", 3, "Desarrollador")
emp4 = Empleado("José Ramírez", "jose.ramirez@empresa.com", 4, "Diseñador")
emp5 = Empleado("Lucía Gómez", "lucia.gomez@empresa.com", 5, "Tester")
emp6 = Empleado("Miguel Sánchez", "miguel.sanchez@empresa.com", 6, "Soporte")
emp7 = Empleado("Laura Díaz", "laura.diaz@empresa.com", 7, "Recursos Humanos")
emp8 = Empleado("Pedro Herrera", "pedro.herrera@empresa.com", 8, "Contador")
emp9 = Empleado("Sofía Morales", "sofia.morales@empresa.com", 9, "Marketing")
emp10 = Empleado("Andrés Castillo", "andres.castillo@empresa.com", 10, "Ventas")

Empleados = [
    emp1, emp2, emp3, emp4, emp5,
    emp6, emp7, emp8, emp9, emp10
]


prod1 = Producto_base(1, "Sandwich de jamón y queso", 45, 10)
prod2 = Producto_base(2, "Panini de pollo", 50, 8)
prod3 = Producto_base(3, "Wrap vegetariano", 42, 12)
prod4 = Producto_base(4, "Bagel con salmón", 55, 15)
prod5 = Producto_base(5, "Croissant relleno de queso", 28, 15)
prod6 = Producto_base(6, "Tostada de aguacate", 35,23)
prod7 = Producto_base(7, "Quiche de espinaca", 48, 9)
prod8 = Producto_base(8, "Empanada de carne", 30, 19)
prod9 = Producto_base(9, "Pizza individual margarita", 60, 13)
prod10 = Producto_base(10, "Baguette con jamón serrano", 52,21)
prod11 = Producto_base(11, "Ensalada César", 40,7)
prod12 = Producto_base(12, "Wrap de pollo", 44, 10)
prod13 = Producto_base(13, "Sandwich vegetariano", 38, 18)
prod14 = Producto_base(14, "Torta mexicana", 46, 19)

Platillos=[
    prod1, prod2, prod3, prod4, prod5,
    prod6, prod7, prod8, prod9, prod10
]

beb1 = Bebida(1, "Latte vainilla", 38, 42, "grande", "caliente")
beb2 = Bebida(2, "Capuchino moka", 40, 23, "mediano", "caliente")
beb3 = Bebida(3, "Té chai latte", 36, 31, "grande", "caliente")
beb4 = Bebida(4, "Frappé de caramelo", 42, 13, "grande", "frío")
beb5 = Bebida(5, "Smoothie de frutos rojos", 45, 13, "mediano", "frío")

Bebi=[
    beb1, beb2, beb3, beb4, beb5
]

mod1=Modificadores("Leche de almendra")
mod2=Modificadores("Sin azúcar")
mod3=Modificadores("Con hielos")
mod4=Modificadores("Chocolate liquido")
mod5=Modificadores("Crema batida")

Modif=[
    mod1, mod2, mod3, mod4, mod5,
]

post1 = Postre(20, "Brownie de chocolate", 28, 12, False, False)
post2 = Postre(21, "Galleta de avena", 20, 23, True, False)
post3 = Postre(22, "Cheesecake", 35, 13, False, False)
post4 = Postre(23, "Muffin de plátano", 25, 13, True, True)
post5 = Postre(24, "Tarta de manzana", 30, 34, False, True)
post6 = Postre(25, "Cupcake de vainilla", 22, 43, False, False)

postr=[
    post1, post2, post3, post4, post5
]


def menu_principal():
    print("\nBienvenido al servicio personalizado de: \n                 My Caffee\n")
    
    print("1. Iniciar sesión")
    print("2. Registrarse")

    cliente_actual = opciones()

    if cliente_actual is not None:
        if isinstance(cliente_actual, Empleado):
            menu_empleado(cliente_actual)
        else:
            print("1. Hacer un pedido")
            print("2. Ver historial de pedidos")
            opciones_cliente(cliente_actual)

            if cliente_actual is not None:
                if not isinstance(cliente_actual, Cliente):
                    cliente_actual = Cliente(cliente_actual.id_persona, cliente_actual.nombre, cliente_actual.email)
                cliente_actual.Pedido1(Platillos)
                opcion_bebida = input("¿Desea agregar bebidas a su orden? (si/no): ")
                if opcion_bebida.lower() == "si":
                    Mostrar_bebidas()
                    cliente_actual.Pedido_bebidas(Bebi, Modif)

                opcion_postre = input("¿Desea agregar postres a su orden? (si/no): ")
                if opcion_postre.lower() == "si":
                    for x in postr:
                        print(f"{x.id_producto}. {x.nombre} - ${x.precio_base}")
                    cliente_actual.Pedido_postres(postr)
                print("\nResumen completo de tu pedido:")
                cliente_actual.Mostrar_Historial()

    return menu_principal()

def menu_empleado(cliente_actual):
    print(f"\nBienvenido {cliente_actual.nombre}, Rol: {cliente_actual.rol}\n")

    print("1. Ver lista de productos")
    print("2. Ver lista de clientes")
    print("3. Registrar nuevo producto")
    print("4. Ver inventario")
    print("5. Procesar pedido de cleinte")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        print("\nPLATILLOS\n")
        Mostrar_menu()
        print("\nBEBIDAS\n")
        Mostrar_bebidas()
        print("\nPOSTRES\n")
        Mostrar_postres()

    elif opcion == "2":
        for u in Usuarios:
            print(f"{u.id_persona} - {u.nombre} ({u.email})")

    elif opcion == "3":
        print("1. Un platillo")
        print("2. Una bebida")
        print("3. Un postre")
        opc=input("Que tipo de producto desea agregar?")
        if opc == "1":
            nombre = input("Nombre del nuevo platillo: ")
            precio = int(input("Precio: "))
            unidades = int(input("Unidades: "))
            nuevo = Producto_base(len(Platillos)+1, nombre, precio, unidades)
            Platillos.append(nuevo)
            print("Producto registrado correctamente.")
        elif opc == "2":
            nombre = input("Nombre de la nueva bebida: ")
            precio = int(input("Precio: "))
            tamaño = input("Tamaño (chico/mediano/grande): ")
            temperatura = input("Temperatura (frío/caliente): ")
            nuevo = Bebida(len(Bebi)+1, nombre, precio, tamaño, temperatura)
            Bebi.append(nuevo)
            print("Bebida registrada correctamente.")
        elif opc == "3":
            nombre = input("Nombre del nuevo postre: ")
            precio = int(input("Precio: "))
            es_vegano = input("¿Es vegano? (si/no): ").lower() == "si"
            sin_gluten = input("¿Es sin gluten? (si/no): ").lower() == "si"
            nuevo = Postre(len(postr)+1, nombre, precio, es_vegano, sin_gluten)
            postr.append(nuevo)
            print("Postre registrado correctamente.")

    elif opcion == "4":
        inventario.mostrar_inventario()

    elif opcion == "5":
        print("\nProcesando pedido de prueba...")
        pedido_demo = Pedido(999, [(Platillos[0], 2), (Bebi[0], 1)])
        inventario.procesar_pedido(pedido_demo)
        pedido_demo.mostrar_resumen()
        inventario.mostrar_inventario()



def opciones():
    opcion = input("Seleccione opción: ")
    try: 
        if opcion == "1":
            return iniciar_secion()

        elif opcion =="2":
            return registrarse()
    except ValueError:
        print("Opcion invalida")
        return menu_principal
    
def opciones_cliente(cliente_actual):
    opcion1=input("Seleccione una opcion")

    if opcion1 =="1":
        print("\n|||MENU|||\n")
        print("\n||PLATILLOS PRINCIPALES|||")
        Mostrar_menu()
    elif opcion1=="2":
        cliente_actual.Mostrar_Historial()


def iniciar_secion():
    print("\n Por favor ingrese su nombre de usuario")

    nombre=input("Nombre:")

    for e in Empleados:
        if e.nombre == nombre:
            print(f"Bienvenido {e.id_empleado}-{e.nombre} (Empleado).")
            return e

    for u in Usuarios:
        if u.nombre == nombre:
            print(f"Bienvenido {u.id_persona}-{u.nombre}.")

            if not isinstance(u,Cliente):
                u=Cliente(u.id_persona, u.nombre, u.email)
            return u
    print("No encontrado.")
    return None

def registrarse():
    print ("\nPor favor ingrese los datos que se le piden a continuacion:\n")

    nombre = input("Ingrese su Nombre: ")
    email = input("Email: ")
    nuevo = Persona(len(Usuarios)+1, nombre, email)
    Usuarios.append(nuevo)
    print("Usuario registrado correctamente.")
    return nuevo and menu_principal()

def Mostrar_menu():
    for x in Platillos:
        print (f"{x.id_producto}. {x.nombre}-${x.precio_base}, ")

def Mostrar_bebidas():
    for x in Bebi:
        print (f"{x.id_producto}. {x.nombre}-${x.precio_base} de tamaño: {x.tamaño} y temperatura: {x.temperatura}")

def Mostrar_postres():
    for x in postr:
        print (f"{x.id_producto}. {x.nombre}-${x.precio_base} es vegano: {x.es_vegano} y libre de gluten: {x.sin_gluten}")

    

menu_principal()