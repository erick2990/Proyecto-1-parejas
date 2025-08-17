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

    #Este metodo sirve para ordenar datos desde un diccionario ya que recibe el diccionario hecho lista y su llave
    def quick_sort(self, lista, clave):
        if len(lista) <= 1:
            return lista
        pivote = lista[0]
        valor_pivote = pivote[clave]
        inicial = [x for x in lista[1:] if x[clave] < valor_pivote]
        medio = [x for x in lista if x[clave] == valor_pivote]
        final = [x for x in lista[1:] if x[clave] >= valor_pivote]
        return self.quick_sort(inicial, clave) + medio + self.quick_sort(final, clave)


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
        else:
            ordenado = Ordenador()
            #Se necesira listar los datos de los objetos para saber a que poder acceder
            #Articulo se refiere al objeto que asi se llama el campo pero de el se regresan los atributos
            productos_lista = [
                {
                    "codigo": codigo,
                    "nombre": datos["Articulo"].nombre,
                    "precio": datos["Articulo"].precio,
                    "stock": datos["Articulo"].stock,
                    "copia": datos["Articulo"] #Este es una copia original para que despues se pueda acceder a todos los metodos del mismo
                }
                for codigo, datos in self.productos.items()
            ]
            while True:
                try:
                    print('\n¿Como desea visualizar los datos? \n1.Ordenado por nombre\n2.Ordenado por precio\n3.Ordenado por stock')
                    op = int(input('Digite la opcion que desea visualizar:  '))
                    match op:
                        case 1:
                           ordenados_u = ordenado.quick_sort(productos_lista, "nombre")
                        case 2:
                           ordenados_u = ordenado.quick_sort(productos_lista, "precio")
                        case 3:
                            ordenados_u = ordenado.quick_sort(productos_lista, "stock")
                        case _:
                            print('La opcion no existe por favor volver a intentarlo')

                    print('Productos ordenados')
                    for tmp in ordenados_u:
                        tmp["copia"].mostrar_producto()
                    break    #Termina el while para ordenar los productos

                except Exception as e:
                    print(f'Por favor volver a intentar, ocurrio {e}')



    def eliminar(self):
        if not  self.productos:
            print("No hay Productos aun")
            return

        else:
            productoEliminar = input("Ingrese el Codigodel producto a eliminar: ")
            if productoEliminar in self.productos:
                while True:
                    confir = input(f'¿Esta seguro que desea eliminar este producto {productoEliminar}? S/N   ')
                    if confir.upper() == "S":
                        del self.productos[productoEliminar]
                        print("Producto eliminado")
                        break
                    elif confir.upper() == "N":
                        print('Eliminacion cancelada')
                        break
                    else:
                        print(f'La opcion {conf} no existe vuelve a intentarlo con S para si o N para no')
            else:
                print("Producto No encontrado")



    def actualiza(self):
        codigoActualizar=input("Ingrese l codigo a Actualizar")
        if codigoActualizar in self.productos:
            Producto = self.productos[codigoActualizar]["Articulo"]
            print("Si esta el Producto")

            nuevoNombre=input("Ingrese el Nuevo Nombre: ")
            nuevaCategoria=input("Ingrese la Nueva Categoria")
            nuevoPrecio=int(input("Ingrese el nuevo Precio"))
            nuevoStock=int(input("Ingrese el nuevo stock"))
            if nuevoNombre:
                Producto.nombre=nuevoNombre
            if nuevaCategoria:
                Producto.categoria=nuevaCategoria
            if nuevoPrecio:
                Producto.precio=nuevoPrecio
            if nuevoStock:
                Producto.stock=nuevoStock
        else:
            print("Producto No encontrado jaja")
class Usuario:
    def __init(self,nombreUsuario,contrasenia):
        self.nombreUsuario=nombreUsuario
        self.contrasenia=contrasenia


fin_menu = True
registro=Inventario()
while fin_menu:
    try:
        print('\t\t\t\t****Bienvenido usuario****')
        print('1.Ingreso de mercaderia\n2.Listado de productos \n3.Buscar producto')
        print('4.Actualizar \n5.eEliminar\n6.salir')
        opcion=int(input("Digite la opción a ingresar: "))
        match opcion:
            case 1:
                registro.ingreso_producto()
            case 2:
                registro.mostrar()
            case 3:
                registro.eliminar()
            case 4:
                registro.eliminar()
            case 5:
                registro.actualiza()
            case 6:
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