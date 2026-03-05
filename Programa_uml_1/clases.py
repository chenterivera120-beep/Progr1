from abc import ABC, abstractmethod
from enum import Enum
from datetime import datetime, date

class Rol(Enum):
    TAQUILLERO = "Taquillero"
    ADMIN = "Administrador"
    LIMPIEZA = "Limpieza"

class TipoSala(Enum):
    DOS_D = "2D"
    TRES_D = "3D"
    IMAX = "IMAX"

class EstadoReserva(Enum):
    PENDIENTE = "Pendiente"
    PAGADA = "Pagada"
    CANCELADA = "Cancelada"


class Persona(ABC):
    def __init__(self, idPersona, nombre, email, telefono):
        self.idPersona = idPersona
        self.nombre = nombre
        self.email = email
        self.telefono = telefono
        self.logueado = False

    def login(self):
        self.logueado = True
        print(f"{self.nombre} ha iniciado sesión.")

    def logout(self):
        self.logueado = False
        print(f"{self.nombre} ha cerrado sesión.")

    def actualizarDatos(self, email, telefono):
        self.email = email
        self.telefono = telefono


class Usuario(Persona):
    def __init__(self, idPersona, nombre, email, telefono):
        super().__init__(idPersona, nombre, email, telefono)
        self.puntosFidelidad = 0
        self.historialReservas = []

    def crearReserva(self, reserva):
        self.historialReservas.append(reserva)

    def consultarPromociones(self, promociones):
        for p in promociones:
            print(f"{p.codigo} - {p.descripcion}")

    def cancelarReserva(self, reserva):
        reserva.estado = EstadoReserva.CANCELADA


class Empleado(Persona):
    def __init__(self, idPersona, nombre, email, telefono, idEmpleado, rol, horario):
        super().__init__(idPersona, nombre, email, telefono)
        self.idEmpleado = idEmpleado
        self.rol = rol
        self.horario = horario

    def marcarEntrada(self):
        print(f"{self.nombre} marcó entrada.")

    def gestionarFunciones(self):
        if self.rol == Rol.ADMIN:
            print("Puede gestionar funciones.")
        else:
            print("No tiene permisos.")



class Reserva:
    def __init__(self, idReserva, usuario, funcion, asientos):
        self.idReserva = idReserva
        self.usuario = usuario
        self.funcion = funcion
        self.asientos = asientos
        self.estado = EstadoReserva.PENDIENTE
        self.montoTotal = len(asientos) * funcion.precioBase

    def confirmarPago(self):

        for asiento in self.asientos:
            if asiento in self.funcion.sala.asientosOcupados:
                print(f"El asiento {asiento} ya está ocupado.")
                return False

        for asiento in self.asientos:
            self.funcion.sala.asientosOcupados.append(asiento)

        self.estado = EstadoReserva.PAGADA

        self.usuario.historialReservas.append(self)

        return True

    def aplicarPromocion(self, promo):
        if promo.esValida():
            self.montoTotal = promo.aplicarDescuento(self.montoTotal)

    def generarTicket(self):
        return f"Reserva {self.idReserva} - Total: ${self.montoTotal}"
    
class Funcion:
    def __init__(self, idFuncion, pelicula, sala, horarioInicio, precioBase):
        self.idFuncion = idFuncion
        self.pelicula = pelicula
        self.sala = sala
        self.horarioInicio = horarioInicio
        self.precioBase = precioBase

    def calcularAsientosLibres(self):
        return self.sala.asientosDisponibles()

    def obtenerDetallesFuncion(self):
        return f"{self.pelicula.titulo} - {self.horarioInicio}"

class Pelicula:
    def __init__(self, titulo, duracion, clasificacion, genero):
        self.titulo = titulo
        self.duracion = duracion
        self.clasificacion = clasificacion
        self.genero = genero

    def obtenerSinopsis(self):
        return f"{self.titulo} - {self.genero}"

    def esAptaParaTodoPublico(self):
        return self.clasificacion == "AA"


class Promocion:
    def __init__(self, codigo, descripcion, porcentajeDescuento, fechaExpiracion):
        self.codigo = codigo
        self.descripcion = descripcion
        self.porcentajeDescuento = porcentajeDescuento
        self.fechaExpiracion = fechaExpiracion

    def esValida(self):
        return date.today() <= self.fechaExpiracion

    def aplicarDescuento(self, monto):
        return monto - (monto * self.porcentajeDescuento / 100)

class Espacio:
    def __init__(self, idEspacio, nombre, ubicacion):
        self.idEspacio = idEspacio
        self.nombre = nombre
        self.ubicacion = ubicacion

    def verificarDisponibilidad(self):
        print("Verificando disponibilidad...")

    def limpiarEspacio(self):
        print(f"{self.nombre} está siendo limpiado.")

class Sala(Espacio):
    def __init__(self, idEspacio, nombre, ubicacion, tipo, capacidadTotal, esVip):
        super().__init__(idEspacio, nombre, ubicacion)
        self.tipo = tipo
        self.capacidadTotal = capacidadTotal
        self.esVip = esVip
        self.asientosOcupados = []

    def ajustarAforo(self, nuevoAforo):
        self.capacidadTotal = nuevoAforo

    def obtenerTipoSala(self):
        return self.tipo

    def asientosDisponibles(self):
        return self.capacidadTotal - len(self.asientosOcupados)
    
class ZonaComida(Espacio):
    def __init__(self, idEspacio, nombre, ubicacion):
        super().__init__(idEspacio, nombre, ubicacion)
        self.listaProductos = []
        self.stockActual = {}

    def agregarProducto(self, producto, cantidad):
        self.listaProductos.append(producto)
        self.stockActual[producto.idProducto] = cantidad

    def venderProducto(self, idProducto, cantidad):
        if self.stockActual.get(idProducto, 0) >= cantidad:
            self.stockActual[idProducto] -= cantidad
            return True
        else:
            return False
        
class Producto:
    def __init__(self, idProducto, nombre, precio, categoria):
        self.idProducto = idProducto
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria