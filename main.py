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
        try:
            codigo=input("Ingrese el Codigo del Producto: ")
            if codigo in self.productos:
                print("Este Codigo ya exste en el Sistema, intente uno nuevo")
                return
