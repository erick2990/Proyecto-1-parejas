class Producto:
    #metodo constructor para la instancia de los objetos recibe
    def __init__(self,cod_producto,nombre,categoria,precio,stock):
        self.Cod_producto=cod_producto
        self.nombre=nombre
        self.categoria=categoria
        self.precio=precio
        self.stock=stock
    #metodo para presentar los datos del objeto
    def mostrar_producto(self):
        print(f'Codigo: {self.Cod_producto} Nombre: {self.nombre} Categoria: {self.categoria} Precio: {self.precio} Stok: {self.stock}')

class Ordenador:


    def quick_sort(self, lista):
        if len(lista) <= 1:
            return lista

        pivote = lista[0]
        inicial = [x for x in lista[1:] if x < pivote]
        medio = [x for x in lista if x == pivote]
        final = [x for x in lista[1:] if x > pivote]

        return self.quick_sort(inicial) + medio + self.quick_sort(final)


#En esta clase se maneja toda la gestion de la tienda desde compras, control y existencias
class Inventario:
    def __init__(self):
        self.productos={}


    def ingreso_producto(self):
        while True:
            try:
                cantidad_productos = int(input('¿Cuantos productos desea ingresar al inventario?:     '))
                for i in range(cantidad_productos):
                    print(f'\t\t\t\tIngreso datos de {i+1} producto: ')
                    while True:
                        codigo = input("Ingrese el codigo del Producto:     ")
                        if codigo in self.productos:
                            print("Este Codigo Ya existe, Intentelo de nuevo...        ")
                        elif codigo == "":
                            print("El codigo no puede estar vacio, Intentelo de nuevo... ")
                        else:
                            break
                    while True:
                        nombre = input("Ingrese el Nombre del Producto:       ")
                        if nombre in self.productos:  # Validacion por nombre check
                            print("Este Nombre en especifico ya existe, ingrese otro:")
                        elif nombre == "":
                            print("Este Campo no puede quedar vacio, Ingrese el nombre")
                        else:
                            break
                    while True:
                        categoria = input("Ingrese La Categoria del Producto:     ")
                        if categoria == "":
                            print("Este campo no puede quedar vacio, Ingrese la categoria")
                        else:
                            break
                    while True:
                        try:
                            precio = float(input("Ingrese el Precio en Quetzales del Producto:     Q."))
                            if precio == "":
                                print("Este campo no Puede quedar vacio, Ingrese el precio")

                            elif precio < 0:
                                print("El precio debe ser mayor a Q0 este no puede ser negativo ni igual a 0")
                            else:
                                break
                        except ValueError:
                            print("Solo se permiten cantidades")
                    while True:
                        try:
                            stock = int(input("Ingrese la cantidad en Stock:      "))
                            if stock < 0:
                                print("Error, la cantidad en stock, no puede ser negativa")
                            else:
                                break
                        except ValueError:
                            print("Solo se permiten enteros")

                    # Luego de tener todos los datos corroborados se pasan hacia un objeto que se guardara en el diccionario
                    producto_tmp = Producto(codigo, nombre.lower(), categoria.lower(), precio, stock)
                    self.productos[codigo] = {
                        "Articulo": producto_tmp
                    }
                    print(f'El producto con codigo {codigo} se Agrego Correctamente')
                    print('\n')
                break #Termina el break principal porque este bloque se ejecuto bien
            except Exception as e:
                print(f'Por favor ingrese datos validos, ocurrio {e}')


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

fin_menu = True
registro=Inventario()
while fin_menu:
    try:
        print('\t\t\t\t****Bienvenido usuario****')
        print('1.Ingreso de mercaderia\n2.Listado de productos \n3.Buscar producto')
        print('4.Actualizar o eliminar producto\n5.Salir')
        opcion=int(input("Digite la opción a ingresar: "))
        match opcion:
            case 1:
                registro.ingreso_producto()
            case 2:
                registro.mostrar()
            case 3:
                registro.eliminar()
            case 4:
                pass
            case 5:
                while True:
                    conf = input('¿Esta seguro que desea salir? S/N    ')
                    if conf.upper() == "S":
                        print('Adios')
                        fin_menu = False
                        break
                    elif conf.upper() == "N":
                        break
                    else:
                        print(f'La opcion {conf} no existe vuelve a intentarlo con S para si o N para no')

            case _:
                print("Esta opción no existe por favor vuelva a intentarlo con una opcion valida")
    except Exception as e:
        print(f'Ocurrio un error {e}, por favor verifique nuevamente')
