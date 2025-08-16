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
            codigo=input("Ingrese El Codigo del Producto:                  ")
            if codigo in self.productos:
                print("Este Codigo Ya existe, Intentelo de nuevo...        ")
            elif codigo=="":
                print("El codigo no puede estar vacio, Intentelo de nuevo  ")
            else:
                break
        while True:
            nombre=input("Ingrese el Nombre del Producto:               ")
            if nombre in self.productos:
                print("Este Nombre en especifico ya existe, ingrese otro:")
            elif nombre=="":
                print("Este Campo no puede quedar vacio, Ingrese el Dato")
            else:
                break
        while True:
            categoria=input("Ingrese La Categoria del Producto:         ")
            if categoria=="":
                print("Este campo no puede quedar vacio, Ingrese el Dato")
            else:
                break
        while True:
            try:
                precio = float(input("Ingrese el Precio del Producto:   "))
                if precio=="":
                    print("Este campo no Puede quedar vacio, Ingrese el Dato")

                elif precio<0:
                    print("El precio debe ser mayor a 0")
                else:
                    break
            except ValueError:
                print("Solo se permiten cantidades")
        while True:
            try:
              stock=int(input("Ingrese la cantidad en Stock:             "))
              if stock=="":
                  print("El stock no puede quedar,vacio Ingrese datos")
              elif stock<0:
                  print("Error, el cantidad en stock, no puede ser menor a 0")
              else:
                  break
            except ValueError:
                print("Solo se permiten enteros")

        self.productos[codigo]=Producto(codigo,nombre,categoria,precio,stock)
        print("El producto se Agrego Correctamente")

    def mostrar(self):
        if not self.productos:
            print("No hay Productos Aun")
            return
        print("Listado")
        for i, Producto in enumerate(self.productos.values(), start=1):
            print(f"{i}. {Producto.Mostrar()}")

    def eliminar(self):
        if not  self.productos:
            print("No hay Productos aun")
            return
        productoEliminar=input("Ingrese el Codigodel producto a eliminar: ")
        if productoEliminar in self.productos:
            del self.productos[productoEliminar]
            print("Producto eliminado")
        else:
            print("Estudiante No encontrado")

fin_Menu = True
registro=RegistroProductos()
while fin_Menu:

    try:
        print("1. Agregar")
        opcion=int(input("seleccione una opcion"))
        match opcion:
            case 1:
                registro.agregar()
            case 2:
                registro.mostrar()
            case 3:
                registro.eliminar()
            case 4:
                 while True:
                    conf = input('¿Esta seguro que desea salir? S/N')
                    if conf.upper() == "S":
                      print('Adios')
                      fin_menu = False
                      break
                    elif conf.upper() == "N":
                       break
                    else:
                       print(f'La opcion {conf} no existe vuelve a intentarlo con S para si o N para no')
            case 5:
                print("Salir")
                break
            case _:
                print("Incorrecto")
    except ValueError:
        print("Ingrese un numero entero: ")
