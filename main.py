from cloudinit.sources.DataSourceAzure import find_busdev_from_disk
from wx.core import ADJUST_MINSIZE


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

class Buscador:


    def busqueda_secuencial(self, lista, objetivo):
        for i in range(len(lista)):  # Recorrer la lista
            if lista[i] == objetivo:  # Comparar elemento actual con el objetivo
                return i  # Retornar índice si lo encuentra

        return -1


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
                    print('\n')

                    print('Productos ordenados')
                    for tmp in ordenados_u:
                        tmp["copia"].mostrar_producto()
                    break    #Termina el while para ordenar los productos

                except Exception as e:
                    print(f'Por favor volver a intentar, ocurrio {e}')


    #metodo para eliminar articulos y a la vez validar y confirmar que el articulo que se borra es el correcto
    def eliminar(self):
        if not  self.productos:
            print("No hay Productos aun")
            return

        else:
            producto_eliminar = input("Ingrese el Codigodel producto a eliminar: ")
            if producto_eliminar in self.productos:
                while True:
                    confir = input(f'¿Esta seguro que desea eliminar este producto {producto_eliminar}? S/N   ')
                    if confir.upper() == "S":
                        del self.productos[producto_eliminar]
                        print("Producto eliminado")
                        break
                    elif confir.upper() == "N":
                        print('Eliminacion cancelada')
                        break
                    else:
                        print(f'La opcion {conf} no existe vuelve a intentarlo con S para si o N para no')
            else:
                print("Producto No encontrado")

    #Metodo para actualizar precio o stock de un articulo según su codigo
    def actualiza(self):
        codigo_actualizar=input("Ingrese el codigo a Actualizar")
        if codigo_actualizar in self.productos:
            fin_update = True #Esta variable sirve para detener o cancelar la actualizacion del producto
            while fin_update:
                confi_u = input(f'¿Esta seguro que desea Actualizar el Producto Con el Codigo {codigo_actualizar}? S/N   ')
                if confi_u.upper() == "S":
                    producto_a = self.productos[codigo_actualizar]["Articulo"] #toma el valor del producto que coincide con ese codigo
                    print("Si esta el Producto")
                    while True:
                        try:
                            nuevo_precio = float(input("Ingrese el Nuevo Precio en Quetzales del Producto:     Q."))
                            if nuevo_precio == "":
                                print("Este campo no Puede quedar vacio, Ingrese el precio")

                            elif nuevo_precio < 0:
                                print("El precio debe ser mayor a Q0 este no puede ser negativo ni igual a 0")
                            elif nuevo_precio>0:
                                producto_a.precio=nuevo_precio
                                break
                        except ValueError:
                            print("Solo se permiten datos en Quetzales")

                    while True:
                        try:
                            nuevo_stock = int(input("Ingrese cuantas unidades se tienen actualmente en stock:   "))
                            if nuevo_stock < 0:
                                print("Error, la cantidad en stock, no puede ser negativa")
                            elif nuevo_stock:
                                producto_a.stock=nuevo_stock
                                print("Se actualizaron datos...")
                                break
                        except ValueError:
                            print("No es permitido ingresar cantidades negativas")

                elif confi_u.upper() == "N":
                    print('Proceso de actualización cancelado')
                    fin_update = False #Se cancela el metodo de actualizacion
                else:
                    print(f'La opcion {conf} no existe vuelve a intentarlo con S para si o N para no')

        else:
            print("Producto No encontrado ")

#Dinamica de busqueda secuencial según los datos del objeto lineas 219 hasta 264
    def buscar(self):
        if not self.productos:
            print('No hay productos registrados aún')
        else:
            lista_busqueda = Buscador() #Esta lista se llena segun los datos que se envian
            fin_busqueda = True #Si se desea terminar la busqueda esto cambiara

            productos_lista = [
                {
                    "codigo": codigo,
                    "nombre": datos["Articulo"].nombre,
                    "precio": datos["Articulo"].precio,
                    "categoria" : datos["Articulo"].categoria,
                    "stock": datos["Articulo"].stock,
                    "copia": datos["Articulo"]
                    # Este es una copia original para que despues se pueda acceder a todos los metodos del mismo
                }
                for codigo, datos in self.productos.items()
            ]

            while fin_busqueda:
                print('\t\t\tBienvenido a realizar busqueda: ')
                print('1.Codigo \n2.Nombre \n3.Categoria \n4.Regresar')
                op_e = int(input('Ingrese la opción que desea ingresar: '))
                match op_e:
                    case 1:
                        lista_busqueda.busqueda_secuencial(productos_lista, "codigo")
                        break
                    case 2:
                        lista_busqueda.busqueda_secuencial(productos_lista, "nombre")
                        break
                    case 3:
                        lista_busqueda.busqueda_secuencial(productos_lista, "categoria")
                        break
                    case 4:
                        print('Regresando al menú principal')
                        fin_busqueda = False
                    case _ :
                        print('Opcion incorrecta por favor vuelva a intentarlo')


            for tmp in lista_busqueda:
                tmp["copia"].mostrar_producto()




class Administrador:
    def __init__(self,user,password):
        self.nombre=user
        self.contra=password


def validacion_admin(administradores):
    intentos =0
    while intentos<3:
        try:
            print(f'Esta accion requiere perfil de administrador...\nTienes {3-intentos} intentos')
            nombre_tmp = input('Ingrese nombre de usuario: ')
            contra_tmp = input('Ingrese la contraseña: ')
            for ob in administradores:
                if ob.nombre ==nombre_tmp:
                    if ob.contra == contra_tmp:
                        print('Bienvenido! permiso concedido')
                        return True
            print('Usuario o contraseña incorrecta por favor intente de nuevo')
            print('\n')
            intentos+=1

        except Exception as e:
            print('Error por favor ingrese un dato valido')
    print('Intentos fallidos no tiene acceso a estas funciones')
    return False


admin1 = Administrador("Erick29", "Erick2000") #Administrador creado
admin2 = Administrador("Darwin04", "TuCuate")  #Administrador creado
administradores = [admin1, admin2] #lista de administradores
fin_menu = True
registro=Inventario()


while fin_menu:
    try:
        print('\t\t\t\t****Bienvenido usuario****')
        print('1.Ingreso de mercaderia\n2.Listado de productos \n3.Buscar producto')
        print('4.Actualizar \n5.Eliminar\n6.salir')
        opcion=int(input("Digite la opción a ingresar: "))
        match opcion:
            case 1:
                registro.ingreso_producto()
            case 2:
                registro.mostrar()
            case 3:
                pass
            case 4:
                if validacion_admin(administradores):
                    registro.actualiza()
            case 5:
                if validacion_admin(administradores):
                    registro.eliminar()
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