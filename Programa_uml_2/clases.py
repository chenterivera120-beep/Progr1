class Persona():
    Usuarios=[]
    def __init__(self, id_persona, nombre, email):
        self.id_persona=id_persona
        self.nombre=nombre
        self.email=email

    def login(self):
        print(f"{self.nombre} ha iniciado sesión.")

    def actualizarDatos(self, nombre, email):
        self.nombre=nombre
        self.email=email

class Cliente(Persona):
    def __init__(self, id_cliente, nombre, email, puntos_fidelidad=0):
        super().__init__(id_cliente, nombre, email) 
        self.puntos_fidelidad = puntos_fidelidad
        self.historial_platillos = [] 
        self.historial_bebidas = []
        self.historial_postres = []

    def Pedido1(self, platillos):
        orden = [] 

        print("Seleccione sus platillos escribiendo sus números separados por comas (ejemplo: 1,2,3):")
        entrada = input("Orden principal: ")
        numeros = entrada.split(",")

        for num in numeros:
            try:
                pedido = int(num)
                if 1 <= pedido <= len(platillos):
                    platillo = platillos[pedido - 1]
                    cantidad = int(input(f"¿Cuantas unidades de {platillo.nombre} desea ordenar? "))
                    orden.append((platillo, cantidad))
                    print(f"Has agregado {cantidad} x {platillo.nombre} - ${platillo.precio_base * cantidad}")
                else:
                    print(f"Número {pedido} inválido, fuera de rango.")
            except ValueError:
                print(f"'{num}' no es un número válido.")
        self.historial_platillos.append(orden)

    def Pedido_bebidas(self, bebidas, modificadores):
        orden2 = []
        print("Seleccione sus bebidas escribiendo sus números separados por comas (ejemplo: 1,2,3):")
        entrada = input("Orden bebidas: ")
        numeros = entrada.split(",")

        for num in numeros:
            try:
                pedido = int(num)
                if 1 <= pedido <= len(bebidas):
                    bebida = bebidas[pedido - 1]
                    cantidad = int(input(f"¿Cuántas unidades de {bebida.nombre} desea ordenar? "))
                    mods_aplicados = []

                    opcion_mod = input(f"¿Desea agregar modificadores a {bebida.nombre}? (si/no): ")
                    if opcion_mod.lower() == "si":
                        print("\n--- Lista de modificadores disponibles ---")
                        for i, m in enumerate(modificadores, start=1):
                            print(f"{i}. {m.modificador}")
                        entrada_mods = input("Seleccione modificadores separados por comas: ")
                        numeros_mods = entrada_mods.split(",")
                        for nm in numeros_mods:
                            try:
                                idx = int(nm)
                                if 1 <= idx <= len(modificadores):
                                    mods_aplicados.append(modificadores[idx-1].modificador)
                            except ValueError:
                                print(f"'{nm}' no es válido.")

                    orden2.append((bebida, cantidad, mods_aplicados))
                    print(f"Has agregado {cantidad} x {bebida.nombre} con modificadores: {mods_aplicados}")
                else:
                    print(f"Número {pedido} inválido, fuera de rango.")
            except ValueError:
                print(f"'{num}' no es un número válido.")

        self.historial_bebidas.append(orden2)

    def Pedido_postres(self, postres):
        orden3 = []
        print("Seleccione sus postres escribiendo sus números separados por comas (ejemplo: 1,2,3):")
        entrada = input("Orden postres: ")
        numeros = entrada.split(",")

        for num in numeros:
            try:
                pedido = int(num)
                if 1 <= pedido <= len(postres):
                    postre = postres[pedido - 1]
                    cantidad = int(input(f"¿Cuántas unidades de {postre.nombre} desea ordenar? "))
                    orden3.append((postre, cantidad))
                    print(f"Has agregado {cantidad} x {postre.nombre} - ${postre.precio_base * cantidad}")
                else:
                    print(f"Número {pedido} inválido, fuera de rango.")
            except ValueError:
                print(f"'{num}' no es un número válido.")

        self.historial_postres.append(orden3)

    def Mostrar_Historial(self):
        print("\nHistorial de pedidos")

        total_platillos = sum(p.precio_base * c for pedido in self.historial_platillos for p, c in pedido)
        total_bebidas = sum(p.precio_base * c for pedido in self.historial_bebidas for p, c, mods in pedido)
        total_postres = sum(p.precio_base * c for pedido in self.historial_postres for p, c in pedido)

        print("\nPlatillos:")
        for pedido in self.historial_platillos:
            for p, c in pedido:
                print(f"{c} x {p.nombre} - ${p.precio_base * c}")
        print(f"Subtotal platillos: ${total_platillos}")

        print("\nBebidas:")
        for pedido in self.historial_bebidas:
            for p, c, mods in pedido:
                mods_txt = ", ".join(mods) if mods else "Ninguno"
                print(f"{c} x {p.nombre} - ${p.precio_base * c} | Modificadores: {mods_txt}")
        print(f"Subtotal bebidas: ${total_bebidas}")

        print("\nPostres:")
        for pedido in self.historial_postres:
            for p, c in pedido:
                print(f"{c} x {p.nombre} - ${p.precio_base * c}")
        print(f"Subtotal postres: ${total_postres}")

        total_general = total_platillos + total_bebidas + total_postres
        print(f"\nTOTAL GENERAL: ${total_general}")



class Empleado(Persona):
    def __init__(self, nombre, email, id_empleado, rol):
        super().__init__(id_empleado, nombre, email) 
        self.id_empleado=id_empleado
        self.rol=rol



class Producto_base():
    def __init__(self, id_producto, nombre, precio_base, unidades):
        self.id_producto=id_producto
        self.nombre=nombre
        self.precio_base=precio_base
        self.unidades=unidades

class Bebida(Producto_base):
    def __init__(self, id_producto, nombre, precio_base, unidades, tamaño, temperatura):
        super().__init__(id_producto, nombre, precio_base, unidades)
        self.tamaño= tamaño
        self.temperatura=temperatura


class Modificadores(Producto_base):
    def __init__(self, modificador):
        self.modificador=modificador


class Postre(Producto_base):
    def __init__(self, id_producto, nombre, precio_base, unidades, es_vegano, sin_gluten):
        super().__init__(id_producto, nombre, precio_base, unidades)
        self.es_vegano=es_vegano
        self.sin_gluten=sin_gluten


class Pedido():
    def __init__(self, id_pedido, productos):
        self.id_pedido = id_pedido
        self.productos = productos
        self.estado = "Pendiente"
        self.total = self.calcular_total()

    def calcular_total(self):
        return sum(prod.precio_base * cant for prod, cant in self.productos)

    def mostrar_resumen(self):
        print(f"\nPedido-{self.id_pedido}")
        for prod, cant in self.productos:
            print(f"{cant} x {prod.nombre} - ${prod.precio_base * cant}")
        print(f"Estado: {self.estado}")
        print(f"Total: ${self.total}")



class Inventario():
    def __init__(self):
        self.existencias = {}

    def agregar_producto(self, producto, unidades):
        self.existencias[producto.id_producto] = unidades

    def procesar_pedido(self, pedido):
        for prod, cant in pedido.productos:
            if prod.id_producto not in self.existencias:
                pedido.estado = "Rechazado (producto no existe)"
                return False
            if self.existencias[prod.id_producto] < cant:
                pedido.estado = "Rechazado (sin stock suficiente)"
                return False

        for prod, cant in pedido.productos:
            self.existencias[prod.id_producto] -= cant

        pedido.estado = "Aceptado"
        return True

    def mostrar_inventario(self):
        print("\nInventario actual")
        for id_prod, unidades in self.existencias.items():
            print(f"Producto {id_prod}: {unidades} unidades")

        
