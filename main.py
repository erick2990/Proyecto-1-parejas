class Producto:
    def __init__(self,codigoProducto,nombre,categoria,precio,stock):
        self.codigoProducto=codigoProducto
        self.nombre=nombre
        self.categoria=categoria
        self.precio=precio
        self.stock=stock
    def Mostrar(self):
        return f"Codigo: {self.codigoProducto} - Nombre: {self.nombre} - Categoria: {self.categoria} - Precio: {self.precio} - Stok: {self.stock}"
class RegistroProductos:
    def __init__(self):
        self.productos={}
    def agregar(self):
        while True:
            codigo=input("Ingrese El Codigo del Producto:   ")
            if codigo in self.productos:
                print("Este Codigo Ya existe, Intentelo de nuevo...")
            elif codigo=="":
                print("El codigo no puede estar vacio, Intentelo de nuevo")
            else:
                break
        nombre=input("Ingrese el Nombre del Producto:       ")
        categoria=input("Ingrese La Categoria del Producto: ")
        precio=float(input("Ingrese el Precio del Producto: "))
        stock=int(input("Ingrese la cantidad en Stock:      "))
        self.productos[codigo]=Producto(codigo,nombre,categoria,precio,stock)
        print("El producto se Agrego Correctamente")

registro=RegistroProductos()
while True:
    print("1. Agregar")
    try:
        opcion=int(input("seleccione una opcion"))
        match opcion:
            case 1:
                registro.agregar()
            case 2:
                print("Salir")
                break
            case _:
                print("Incorrecto")
    except ValueError:
        print("Ingrese un numero entero: ")

