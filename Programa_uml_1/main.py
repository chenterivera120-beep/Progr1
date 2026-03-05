from clases import *
from datetime import datetime, date


us1 = Usuario(1, "Jorje Paz Ortuño", "Jos1021@gmail.com", "52 233 201 4192")
us2 = Usuario(2, "Ana López", "ana@gmail.com", "5512345678")
us3 = Usuario(3, "Carlos Méndez", "carlos@gmail.com", "5523456789")
us4 = Usuario(4, "María Torres", "maria@gmail.com", "5534567890")
us5 = Usuario(5, "Luis Ramírez", "luis@gmail.com", "5545678901")
us6 = Usuario(6, "Sofía Herrera", "sofia@gmail.com", "5556789012")
us7 = Usuario(7, "Diego Cruz", "diego@gmail.com", "5567890123")
us8 = Usuario(8, "Valeria Sánchez", "valeria@gmail.com", "5578901234")
us9 = Usuario(9, "Fernando Díaz", "fernando@gmail.com", "5589012345")
us10 = Usuario(10, "Camila Reyes", "camila@gmail.com", "5590123456")

usuarios = [
    us1, us2, us3, us4, us5,
    us6, us7, us8, us9, us10
]

emp1 = Empleado(101, "Pedro Admin", "admin@gmail.com", "5511111111", "EMP1", Rol.ADMIN, "9:00-18:00")
emp2 = Empleado(102, "Laura Taquilla", "laura@gmail.com", "5522222222", "EMP2", Rol.TAQUILLERO, "9:00-18:00")
emp3 = Empleado(103, "Miguel Limpieza", "miguel@gmail.com", "5533333333", "EMP3", Rol.LIMPIEZA, "9:00-18:00")
emp4 = Empleado(104, "Sandra Taquilla", "sandra@gmail.com", "5544444444", "EMP4", Rol.TAQUILLERO, "9:00-18:00")
emp5 = Empleado(105, "Roberto Limpieza", "roberto@gmail.com", "5555555555", "EMP5", Rol.LIMPIEZA, "9:00-18:00")
emp6 = Empleado(106, "Andrea Taquilla", "andrea@gmail.com", "5566666666", "EMP6", Rol.TAQUILLERO, "9:00-18:00")
emp7 = Empleado(107, "Daniel Limpieza", "daniel@gmail.com", "5577777777", "EMP7", Rol.LIMPIEZA, "9:00-18:00")
emp8 = Empleado(108, "Lucía Taquilla", "lucia@gmail.com", "5588888888", "EMP8", Rol.TAQUILLERO, "9:00-18:00")
emp9 = Empleado(109, "Javier Limpieza", "javier@gmail.com", "5599999999", "EMP9", Rol.LIMPIEZA, "9:00-18:00")
emp10 = Empleado(110, "Monica Taquilla", "monica@gmail.com", "5500000000", "EMP10", Rol.TAQUILLERO, "9:00-18:00")

empleados = [
    emp1, emp2, emp3, emp4, emp5,
    emp6, emp7, emp8, emp9, emp10
]

zona = ZonaComida(1, "Dulcería Principal", "Entrada")

p1 = Producto(1, "Palomitas Chicas", 50, "Palomitas")
p2 = Producto(2, "Palomitas Grandes", 80, "Palomitas")
p3 = Producto(3, "Nachos", 65, "Snacks")
p4 = Producto(4, "Hot Dog", 45, "Snacks")
p5 = Producto(5, "Refresco Chico", 30, "Bebidas")
p6 = Producto(6, "Refresco Grande", 45, "Bebidas")
p7 = Producto(7, "Chocolate", 25, "Dulces")
p8 = Producto(8, "Gomitas", 20, "Dulces")
p9 = Producto(9, "Combo Pareja", 150, "Combos")
p10 = Producto(10, "Combo Familiar", 250, "Combos")

productos = [p1,p2,p3,p4,p5,p6,p7,p8,p9,p10]

for prod in productos:
    zona.agregarProducto(prod, 20)

sala1 = Sala(1, "Sala 1", "Planta Baja", TipoSala.DOS_D, 50, False)
sala2 = Sala(2, "Sala 2", "Planta Alta", TipoSala.IMAX, 30, True)
sala3 = Sala(3, "Sala 3", "Planta Baja", TipoSala.TRES_D, 40, False)
sala4 = Sala(4, "Sala 4", "Planta Alta", TipoSala.DOS_D, 35, False)
sala5 = Sala(5, "Sala 5", "Planta Baja", TipoSala.IMAX, 25, True)
sala6 = Sala(6, "Sala 6", "Planta Alta", TipoSala.TRES_D, 45, False)
sala7 = Sala(7, "Sala 7", "Planta Baja", TipoSala.DOS_D, 60, False)
sala8 = Sala(8, "Sala 8", "Planta Alta", TipoSala.IMAX, 20, True)
sala9 = Sala(9, "Sala 9", "Planta Baja", TipoSala.TRES_D, 30, False)
sala10 = Sala(10, "Sala 10", "Planta Alta", TipoSala.DOS_D, 55, False)

salas = [sala1,sala2,sala3,sala4,sala5,sala6,sala7,sala8,sala9,sala10]


pel1 = Pelicula("Avengers", 120, "B", "Acción")
pel2 = Pelicula("Toy Story", 90, "AA", "Animación")
pel3 = Pelicula("La Monja", 110, "C", "Terror")
pel4 = Pelicula("Rápidos y Furiosos", 130, "B", "Acción")
pel5 = Pelicula("Frozen", 100, "AA", "Animación")
pel6 = Pelicula("Joker", 122, "C", "Drama")
pel7 = Pelicula("Spider-Man", 115, "B", "Superhéroes")
pel8 = Pelicula("El Conjuro", 112, "C", "Terror")
pel9 = Pelicula("Coco", 105, "AA", "Animación")
pel10 = Pelicula("Batman", 140, "B", "Acción")

peliculas = [pel1,pel2,pel3,pel4,pel5,pel6,pel7,pel8,pel9,pel10]


func1 = Funcion(1, pel1, sala1, datetime.now(), 80)
func2 = Funcion(2, pel2, sala2, datetime.now(), 70)
func3 = Funcion(3, pel3, sala3, datetime.now(), 75)
func4 = Funcion(4, pel4, sala4, datetime.now(), 85)
func5 = Funcion(5, pel5, sala5, datetime.now(), 90)
func6 = Funcion(6, pel6, sala6, datetime.now(), 95)
func7 = Funcion(7, pel7, sala7, datetime.now(), 80)
func8 = Funcion(8, pel8, sala8, datetime.now(), 100)
func9 = Funcion(9, pel9, sala9, datetime.now(), 70)
func10 = Funcion(10, pel10, sala10, datetime.now(), 85)

funciones = [
    func1,func2,func3,func4,func5,
    func6,func7,func8,func9,func10
]


promo1 = Promocion("DESC10", "10% descuento general", 10, date(2026, 12, 31))
promo2 = Promocion("DESC20", "20% descuento estudiantes", 20, date(2026, 12, 31))
promo3 = Promocion("FAM15", "15% descuento familiar", 15, date(2026, 12, 31))
promo4 = Promocion("VIP25", "25% descuento VIP", 25, date(2026, 12, 31))
promo5 = Promocion("MATINEE", "30% función matutina", 30, date(2026, 12, 31))
promo6 = Promocion("TERROR5", "5% películas de terror", 5, date(2026, 12, 31))
promo7 = Promocion("COMBO10", "10% combo dulcería", 10, date(2026, 12, 31))
promo8 = Promocion("CINEPLUS", "18% membresía especial", 18, date(2026, 12, 31))
promo9 = Promocion("VIERNES20", "20% viernes especial", 20, date(2026, 12, 31))
promo10 = Promocion("NAVIDAD35", "35% promoción navideña", 35, date(2026, 12, 31))

promociones = [
    promo1,promo2,promo3,promo4,promo5,
    promo6,promo7,promo8,promo9,promo10
]



def registrar_usuario():
    nombre = input("Ingrese su Nombre: ")
    email = input("Email: ")
    telefono = input("Teléfono: ")
    nuevo = Usuario(len(usuarios)+1, nombre, email, telefono)
    usuarios.append(nuevo)
    print("Usuario registrado correctamente.")
    return nuevo


def iniciar_sesion():
    email = input("Email: ")
    for u in usuarios:
        if u.email == email:
            print(f"Bienvenido {u.nombre}.")
            return u
    for e in empleados:
        if e.email == email:
            print("Bienvenido empleado.")
            return e
    print("No encontrado.")
    return None


def menu_usuario(usuario):

    print("\n|||FUNCIONES DISPONIBLES|||")
    for f in funciones:
        print(f"{f.idFuncion}. {f.pelicula.titulo} - Sala: {f.sala.nombre} - ${f.precioBase}")

    opcion = int(input("Seleccione función: "))
    funcion = next(f for f in funciones if f.idFuncion == opcion)

    print(f"\nAsientos disponibles: {funcion.calcularAsientosLibres()}")
    print(f"Asientos ocupados: {funcion.sala.asientosOcupados}")

    while True:
        asientos = input("Ingrese asientos separados por coma (A1,A2): ")
        lista_asientos = [a.strip().upper() for a in asientos.split(",")]

        ocupados = funcion.sala.asientosOcupados

        repetidos = [a for a in lista_asientos if a in ocupados]

        duplicados = [a for a in lista_asientos if lista_asientos.count(a) > 1]

        if repetidos:
            print(f"Estos asientos ya están ocupados: {repetidos}")
            print("Por favor elija otros.")
        elif duplicados:
            print(f"No puede repetir asientos: {set(duplicados)}")
        else:
            break

    reserva = Reserva(len(usuario.historialReservas)+1, usuario, funcion, lista_asientos)

    print("\n||| DULCERÍA |||")
    for prod in zona.listaProductos:
        print(f"{prod.idProducto}. {prod.nombre} | Categoría: {prod.categoria} | Precio: ${prod.precio}")

    eleccion = input("Seleccione productos separados por coma (0 si no desea): ")

    if eleccion != "0":
        seleccionados = eleccion.split(",")

        for item in seleccionados:
            idProd = int(item)
            cantidad = int(input(f"Cantidad para producto {idProd}: "))

            if zona.venderProducto(idProd, cantidad):
                producto = next(p for p in zona.listaProductos if p.idProducto == idProd)
                reserva.montoTotal += producto.precio * cantidad
                print("Producto agregado.")
            else:
                print("Stock insuficiente.")

    codigo = input("¿Tiene código promocional? (si/no): ")

    if codigo.lower() == "si":
        cod = input("Ingrese código: ").upper()

        for p in promociones:
            if p.codigo == cod and p.esValida():
                reserva.aplicarPromocion(p)
                print("Descuento aplicado.")
                break
        else:
            print("Código inválido o expirado.")

    if reserva.confirmarPago():
        print("\nReserva confirmada correctamente.")
        print(reserva.generarTicket())
    else:
        print("\nNo se pudo completar la reserva.")


def menu_empleado(empleado):
    print(f"\nBienvenido {empleado.nombre}")
    print("1. Ver funciones")
    if empleado.rol == Rol.ADMIN:
        print("2. Agregar función")

    opcion = input("Seleccione opción: ")

    if opcion == "1":
        for f in funciones:
            print(f.obtenerDetallesFuncion())

    elif opcion == "2" and empleado.rol == Rol.ADMIN:
        titulo = input("Título película: ")
        duracion = int(input("Duración: "))
        clasificacion = input("Clasificación: ")
        genero = input("Género: ")
        nueva_peli = Pelicula(titulo, duracion, clasificacion, genero)

        nueva_funcion = Funcion(
            len(funciones)+1,
            nueva_peli,
            sala1,
            datetime.now(),
            80
        )

        funciones.append(nueva_funcion)
        print("Función agregada.")



while True:
    print("\nSISTEMA CINE")
    print("1. Iniciar sesión")
    print("2. Registrarse")
    print("3. Salir")

    opcion = input("Seleccione opción: ")

    if opcion == "1":
        persona = iniciar_sesion()
        if isinstance(persona, Usuario):
            menu_usuario(persona)
        elif isinstance(persona, Empleado):
            menu_empleado(persona)

    elif opcion == "2":
        usuario = registrar_usuario()
        menu_usuario(usuario)

    elif opcion == "3":
        print("Gracias por usar el sistema.")
        break