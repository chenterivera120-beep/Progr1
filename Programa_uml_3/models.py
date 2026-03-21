class Material():
    def __init__(self, id_Material, año_Publicacion, disponible):
        self.id_Material=id_Material
        self.año_Publicacion=año_Publicacion
        self.disponible=disponible

class Libro(Material):
    def __init__(self, id_Material, año_Publicacion, disponible, autor, isbn, genero):
        super().__init__(id_Material, año_Publicacion, disponible)
        self.autor=autor
        self.isbn=isbn
        self.genero=genero

        

class Revista(Material):
    def __init__(self, id_Material, año_Publicacion, disponible, edicion, periocidad):
        super().__init__(id_Material, año_Publicacion, disponible)
        self.edicion=edicion
        self.periocidad=periocidad

class Material_Digital(Material):
    def __init__(self, id_Material, año_Publicacion, disponible, tipo_Archivo, url_Descarga, tamaño_MB):
        super().__init__(id_Material, año_Publicacion, disponible)
        self.tipo_Archivo=tipo_Archivo
        self.url_Descarga=url_Descarga
        self.tamaño_MB=tamaño_MB


class Persona():
    def __init__(self, id_persona, nombre, numero, funcion):
        self.id_persona=id_persona
        self.nombre=nombre
        self.numero=numero
        self.funcion=funcion

class Usuario(Persona):
    def __init__(self, id_persona, nombre, numero, funcion, limite_Prestamos):
        super().__init__(id_persona, nombre, numero, funcion)
        self.limite_Prestamos=limite_Prestamos

class Bibliotecario(Persona):
    def __init__(self, id_persona, nombre, numero, funcion):
        super().__init__(id_persona, nombre, numero, funcion)


    def gestionarPrestamo(self, Usuarios, Pedidos):
        print("\nElija un usuario para acceder a sus pedidos:\n")
        for x in Usuarios:
            if x.funcion == "Usuario":
                print(f"{x.id_persona} - {x.nombre}")

        us_id = int(input("\nIngrese el ID del usuario: "))
        usuario = None
        for u in Usuarios:
            if u.id_persona == us_id:
                usuario = u
                break

        if not usuario:
            print("Usuario no encontrado.")
            return

        pedidos_usuario = Pedidos.get(us_id, [])
        if not pedidos_usuario:
            print("Este usuario no tiene pedidos registrados.")
            return

        print(f"\nPedidos de {usuario.nombre}:")
        for material in pedidos_usuario:
            print(f"ID {material.id_Material} - {type(material).__name__}")

            decision = input("¿Aceptar (A) o Denegar (D) este pedido?: ").upper()
            if decision == "A":
                if material.disponible:
                    material.disponible = False
                    print(f"Pedido aceptado: Material {material.id_Material} prestado.")
                else:
                    print(f"Material {material.id_Material} no disponible.")
            elif decision == "D":
                print(f"Pedido denegado: Material {material.id_Material} no será prestado.")



    def transferir_material(self, Sucursales, catalogos):    
        print("\n1. libros")
        print("2. Revistas")
        print("3. Material DIgital")

        for x in Sucursales:
            print(f"{x.id_Sucursal} - {x.nombre}")

        origen = int(input("\nSucursal origen (ID): "))
        destino = int(input("Sucursal destino (ID): "))

        material_id = int(input("Ingrese el ID del material a transferir: "))

        origen_catalogo = catalogos[origen]
        destino_catalogo = catalogos[destino]

        material = None
        for m in origen_catalogo:
            if m.id_Material == material_id:
                material = m
                break

        if material:
            origen_catalogo.remove(material)
            destino_catalogo.append(material)
            print(f"\nMaterial {material_id} transferido de {Sucursales[origen-1].nombre} "
                f"a {Sucursales[destino-1].nombre}.")
        else:
            print("\nEl material no se encontró en la sucursal origen.")





class Sucursal():
    def __init__(self, id_Sucursal, nombre_Sucursal):
        self.id_Sucursal=id_Sucursal
        self.nombre=nombre_Sucursal

        self.catalogo_Local=[]


class Prestamo():
    def __init__(self, id_Prestamo, fecha_Inicio, fecha_Devolucion, usuario, material):
        self.id_Prestamo = id_Prestamo
        self.fecha_Inicio = fecha_Inicio
        self.fecha_Devolucion = fecha_Devolucion
        self.usuario = usuario
        self.material = material

class Penalizacion():
    def __init__(self, monto=0, motivo="", pagada=False, usuario=None, material=None):
        self.monto = monto
        self.motivo = motivo
        self.pagada = pagada
        self.usuario = usuario
        self.material = material

    def calcular_multa(self, usuario, material, dias_retraso, tarifa_por_dia=10):
        self.usuario = usuario
        self.material = material
        self.monto = dias_retraso * tarifa_por_dia
        self.motivo = f"Retraso de {dias_retraso} días en la devolución"
        self.pagada = False

        print(f"\n📌 Multa generada:")
        print(f"Usuario: {usuario.nombre}")
        print(f"Material ID: {material.id_Material} ({type(material).__name__})")
        print(f"Días de retraso: {dias_retraso}")
        print(f"Monto a pagar: ${self.monto}")

class Catalogo:
    def __init__(self, catalogos):
        self.catalogos = catalogos

    def buscar_por_autor(self, autor):
        resultados = []
        for sucursal_id, materiales in self.catalogos.items():
            for m in materiales:

                if isinstance(m, Libro) and m.autor.lower() == autor.lower():
                    resultados.append((sucursal_id, m))
        return resultados

    def buscar_general(self, termino):
        resultados = []
        for sucursal_id, materiales in self.catalogos.items():
            for m in materiales:

                if (str(m.id_Material) == str(termino) or
                    (isinstance(m, Libro) and termino.lower() in m.autor.lower()) or
                    (isinstance(m, Libro) and termino.lower() in m.genero.lower()) or
                    (isinstance(m, Revista) and termino.lower() in m.edicion.lower()) or
                    (isinstance(m, Material_Digital) and termino.lower() in m.tipo_Archivo.lower())):
                    resultados.append((sucursal_id, m))
        return resultados