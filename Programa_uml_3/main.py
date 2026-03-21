from models import *

lib1 = Libro(1, 1998, True, "Gabriel García Márquez", "9780307389732", "Novela")
lib2 = Libro(2, 2005, False, "Isabel Allende", "9780061120254", "Drama")
lib3 = Libro(3, 2010, True, "Mario Vargas Llosa", "9788420471839", "Política")
lib4 = Libro(4, 1995, True, "Gabriel García Márquez", "9788437604947", "Ensayo")
lib5 = Libro(5, 2020, False, "Isabel Allende", "9786073161234", "Crónica")
lib6 = Libro(6, 2018, True, "Juan Rulfo", "9788437604948", "Cuento")
lib7 = Libro(7, 2001, True, "Gabriel García Márquez", "9789681604224", "Poesía")
lib8 = Libro(8, 2015, False, "Laura Esquivel", "9780385420174", "Romance")
lib9 = Libro(9, 2022, True, "Valeria Luiselli", "9780525559262", "Narrativa")
lib10 = Libro(10, 1990, True, "Gabriel García Márquez", "9789681604225", "Ensayo")

libros=[
    lib1, lib2, lib3, lib4, lib5, 
    lib6, lib7, lib8, lib9, lib10
]

rev1 = Revista(11, 2021, True, "Edición Especial", "Mensual")
rev2 = Revista(12, 2019, False, "Vol. 34", "Semanal")
rev3 = Revista(13, 2020, True, "Núm. 12", "Trimestral")
rev4 = Revista(14, 2018, True, "Vol. 20", "Bimestral")
rev5 = Revista(15, 2022, False, "Edición Anual", "Anual")
rev6 = Revista(16, 2017, True, "Núm. 45", "Mensual")
rev7 = Revista(17, 2015, True, "Vol. 10", "Semanal")
rev8 = Revista(18, 2023, False, "Edición Especial", "Trimestral")
rev9 = Revista(19, 2016, True, "Núm. 30", "Mensual")
rev10 = Revista(20, 2024, True, "Vol. 50", "Semanal")

revistas=[
    rev1, rev2, rev3, rev4, rev5, 
    rev6, rev7, rev8, rev9, rev10
]

rev_d1 = Material_Digital(21, 2020, True, "PDF", "http://ejemplo.com/rev1", 15.2)
rev_d2 = Material_Digital(22, 2019, False, "EPUB", "http://ejemplo.com/rev2", 8.5)
rev_d3 = Material_Digital(23, 2021, True, "MOBI", "http://ejemplo.com/rev3", 12.0)
rev_d4 = Material_Digital(24, 2018, True, "PDF", "http://ejemplo.com/rev4", 20.3)
rev_d5 = Material_Digital(25, 2022, False, "EPUB", "http://ejemplo.com/rev5", 9.7)
rev_d6 = Material_Digital(26, 2017, True, "PDF", "http://ejemplo.com/rev6", 14.1)
rev_d7 = Material_Digital(27, 2015, True, "EPUB", "http://ejemplo.com/rev7", 7.9)
rev_d8 = Material_Digital(28, 2023, False, "MOBI", "http://ejemplo.com/rev8", 11.5)
rev_d9 = Material_Digital(29, 2016, True, "PDF", "http://ejemplo.com/rev9", 18.4)
rev_d10 = Material_Digital(30, 2024, True, "EPUB", "http://ejemplo.com/rev10", 10.2)

revistas_d=[
    rev_d1, rev_d2, rev_d3, rev_d4, rev_d5, 
    rev_d6, rev_d7, rev_d8, rev_d9, rev_d10
]

sucur1 = Sucursal(1, "Biblioteca Central Puebla")
sucur2 = Sucursal(2, "Biblioteca Regional Cholula")
sucur3 = Sucursal(3, "Biblioteca Universitaria BUAP")
sucur4 = Sucursal(4, "Biblioteca Municipal Atlixco")
sucur5 = Sucursal(5, "Biblioteca Comunitaria Tehuacán")
sucur6 = Sucursal(6, "Biblioteca Infantil San Pedro")
sucur7 = Sucursal(7, "Biblioteca Digital Angelópolis")
sucur8 = Sucursal(8, "Biblioteca Histórica Zacatlán")
sucur9 = Sucursal(9, "Biblioteca Pública Huauchinango")
sucur10 = Sucursal(10, "Biblioteca Metropolitana Puebla")

Sucursales = [
    sucur1, sucur2, sucur3, sucur4, sucur5,
    sucur6, sucur7, sucur8, sucur9, sucur10
]


catalogo_sucur1 = [lib1, lib2, rev1, rev_d1, rev_d2]
catalogo_sucur2 = [lib3, lib4, rev2, rev3, rev_d3]
catalogo_sucur3 = [lib5, lib6, rev4, rev_d4, rev_d5]
catalogo_sucur4 = [lib7, rev5, rev6, rev_d6, rev_d7]
catalogo_sucur5 = [lib8, lib9, rev7, rev_d8, rev_d9]
catalogo_sucur6 = [lib10, rev8, rev9, rev_d10]
catalogo_sucur7 = [lib1, lib3, rev2, rev_d1, rev_d4]
catalogo_sucur8 = [lib4, lib6, rev3, rev5, rev_d2]
catalogo_sucur9 = [lib7, lib9, rev6, rev8, rev_d7]
catalogo_sucur10 = [lib2, lib5, lib10, rev10, rev_d9]

catalogos = {
    1: catalogo_sucur1,
    2: catalogo_sucur2,
    3: catalogo_sucur3,
    4: catalogo_sucur4,
    5: catalogo_sucur5,
    6: catalogo_sucur6,
    7: catalogo_sucur7,
    8: catalogo_sucur8,
    9: catalogo_sucur9,
    10: catalogo_sucur10
}

Us1  = Usuario(1, "Mauricio López", "mauricio.lopez@mail.com", "Usuario", 5)
Us2  = Usuario(2, "Ana Torres", "ana.torres@mail.com", "Usuario", 5)
Us3  = Usuario(3, "Jorge Ramírez", "jorge.ramirez@mail.com", "Usuario", 5)
Us4  = Usuario(4, "Lucía Hernández", "lucia.hernandez@mail.com", "Usuario", 5)
Us5  = Usuario(5, "Carlos Méndez", "carlos.mendez@mail.com", "Usuario", 5)
Us6  = Usuario(6, "Sofía Aguilar", "sofia.aguilar@mail.com", "Usuario", 5)
Us7  = Usuario(7, "Fernando Díaz", "fernando.diaz@mail.com", "Usuario", 5)
Us8  = Usuario(8, "Patricia Gómez", "patricia.gomez@mail.com", "Usuario", 5)
Us9  = Bibliotecario(9, "Ricardo Sánchez", "ricardo.sanchez@mail.com", "Bibliotecario")
Us10 = Bibliotecario(10, "María Fernández", "maria.fernandez@mail.com", "Bibliotecario")

Usuarios=[
    Us1, Us2, Us3, Us4, Us5, 
    Us6, Us7, Us8, Us9, Us10
]


Prestamo_Us1  = [lib1, lib2, rev1, rev_d1]
Prestamo_Us2  = [lib3, rev2, rev_d3]
Prestamo_Us3  = [lib5, rev4, rev_d5]
Prestamo_Us4  = [lib7, rev5, rev_d6]
Prestamo_Us5  = [lib8, rev7, rev_d9]
Prestamo_Us6  = [lib10, rev8, rev_d10]
Prestamo_Us7  = [lib3, rev2, rev_d4]
Prestamo_Us8  = [lib6, rev5, rev_d2]
Prestamo_Us9  = [lib9, rev6, rev8]
Prestamo_Us10 = [lib2, lib10, rev10, rev_d9]

Pedidos={
    1: Prestamo_Us1,
    2: Prestamo_Us2,
    3: Prestamo_Us3,
    4: Prestamo_Us4,
    5: Prestamo_Us5,
    6: Prestamo_Us6,
    7: Prestamo_Us7,
    8: Prestamo_Us8,
    9: Prestamo_Us9,
    10: Prestamo_Us10
}





def menu_principal():
    print("\n|||Bienvenido a la sistema de asistencia virtual de su biblioteca|||\n")

    print("Seleccione una opcion:\n")

    print("1. Iniciar secion")
    print("2. Registrar nuevo usuario")

    ops=input("\nQue desea hacer: ")

    opciones(ops)

    

def opciones(ops):
    if ops == "1":
        iniciar_secion()
    if ops == "2":
        registrarse()

def iniciar_secion():
    print("Por favor ingrese su nombre de usuario\n")
    var=input("Nombre de usuario:")

    for x in Usuarios:
        if x.nombre == var:
            if x.funcion == "Bibliotecario":
                print(f"\nBienvenido {x.nombre} al menu del empleado\n")
                menu_empleado(x, Sucursales, catalogos)
            else:
                print(f"\nBienvenido {x.nombre} al menu de usuario")


def registrarse():
    print("\nComplete los tadotos que se le piden a continuacion\n")

    nombre=input("Nombre: ")
    numero=input("Número de telefono: ")

    nuevo=Usuario(len(Usuarios)+1, nombre, numero, "Usuario")
    Usuarios.append(nuevo)
    print("Usuario registrado correctamente.")
    return nuevo and menu_principal()

def menu_empleado(x, Sucursales, catalogos):
    print("\n1. Gestionar Prestamos")
    print("2. Transferir Material")
    print("3. Calcular Multa")
    print("4. Busqueda por autor")
    print("5. Búsqueda general por sucursal")

    op=input("¿Qué decea hacer?: ")

    catalogo_general = Catalogo(catalogos)
    
    if op == "1":
        x.gestionarPrestamo(Usuarios, Pedidos)
    elif op == "2":
        x.transferir_material(Sucursales, catalogos)
    elif op == "3":
        us_id = int(input("Ingrese el ID del usuario: "))
        material_id = int(input("Ingrese el ID del material: "))
        dias_retraso = int(input("Ingrese los días de retraso: "))

        usuario = None
        material = None

        for u in Usuarios:
            if u.id_persona == us_id:
                usuario = u
                break

        for lista in catalogos.values():
            for m in lista:
                if m.id_Material == material_id:
                    material = m
                    break

        if usuario and material:
            penalizacion = Penalizacion()
            penalizacion.calcular_multa(usuario, material, dias_retraso)
        else:
            print("Usuario o material no encontrado.")

    elif op == "4":
        autor = input("Ingrese el nombre del autor: ")
        resultados = catalogo_general.buscar_por_autor(autor)
        if resultados:
            for sucursal_id, material in resultados:
                print(f"Sucursal {sucursal_id}: {material.id_Material} - {type(material).__name__}")
        else:
            print("No se encontraron libros de ese autor.")

    elif op == "5":
        termino = input("Ingrese término de búsqueda (ID, autor, género, etc.): ")
        resultados = catalogo_general.buscar_general(termino)
        if resultados:
            for sucursal_id, material in resultados:
                print(f"Sucursal {sucursal_id}: {material.id_Material} - {type(material).__name__}")
        else:
            print("No se encontraron coincidencias.")

    

menu_principal()