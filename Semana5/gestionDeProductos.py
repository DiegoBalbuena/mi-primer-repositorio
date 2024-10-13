import os

# Lista de productos
productos = []

def cargar_datos():
    """Cargar datos desde un archivo al inicio del programa."""
    if os.path.exists("productos.txt"):
        with open("productos.txt", "r") as file:
            for line in file:
                nombre, precio, cantidad = line.strip().split(", ")
                productos.append({
                    'nombre': nombre,
                    'precio': float(precio),
                    'cantidad': int(cantidad)
                })

def guardar_datos():
    """Guardar los datos de los productos en un archivo."""
    with open("productos.txt", "w") as file:
        for producto in productos:
            file.write(f"{producto['nombre']}, {producto['precio']}, {producto['cantidad']}\n")

def añadir_producto():
    """Añadir un nuevo producto a la lista."""
    nombre = input("Introduce el nombre del producto: ")
    while True:
        try:
            precio = float(input("Introduce el precio del producto: "))
            cantidad = int(input("Introduce la cantidad del producto: "))
            break  # Salir del bucle si la entrada es válida
        except ValueError:
            print("Por favor, introduce un valor numérico válido para el precio y la cantidad.")
    
    producto = {'nombre': nombre, 'precio': precio, 'cantidad': cantidad}
    productos.append(producto)
    print(f"Producto '{nombre}' añadido correctamente.")

def ver_productos():
    """Mostrar todos los productos."""
    if not productos:
        print("No hay productos en la lista.")
        return
    print("\nLista de productos:")
    for producto in productos:
        print(f"Nombre: {producto['nombre']}, Precio: {producto['precio']}, Cantidad: {producto['cantidad']}")
    print()  # Línea en blanco para mayor claridad

def actualizar_producto():
    """Actualizar un producto existente."""
    nombre = input("Introduce el nombre del producto a actualizar: ")
    for producto in productos:
        if producto['nombre'].lower() == nombre.lower():
            print("Producto encontrado.")
            while True:
                campo = input("¿Qué deseas actualizar? (nombre, precio, cantidad): ").lower()
                if campo == 'nombre':
                    nuevo_nombre = input("Introduce el nuevo nombre: ")
                    producto['nombre'] = nuevo_nombre
                elif campo == 'precio':
                    try:
                        nuevo_precio = float(input("Introduce el nuevo precio: "))
                        producto['precio'] = nuevo_precio
                    except ValueError:
                        print("Por favor, introduce un valor numérico válido.")
                elif campo == 'cantidad':
                    try:
                        nueva_cantidad = int(input("Introduce la nueva cantidad: "))
                        producto['cantidad'] = nueva_cantidad
                    except ValueError:
                        print("Por favor, introduce un valor numérico válido.")
                else:
                    print("Opción no válida. Por favor, elige entre 'nombre', 'precio', o 'cantidad'.")
                    continue

                print(f"Producto '{nombre}' actualizado a: {producto}")
                return
    print("Producto no encontrado.")

def eliminar_producto():
    """Eliminar un producto de la lista."""
    nombre = input("Introduce el nombre del producto a eliminar: ")
    for i, producto in enumerate(productos):
        if producto['nombre'].lower() == nombre.lower():
            del productos[i]
            print(f"Producto '{nombre}' eliminado correctamente.")
            return
    print("Producto no encontrado.")

def menu():
    """Mostrar el menú y manejar las opciones del usuario."""
    cargar_datos()  # Cargar los productos desde el archivo al iniciar
    while True:
        print("\n--- Sistema de Gestión de Productos ---")
        print("1: Añadir producto")
        print("2: Ver productos")
        print("3: Actualizar producto")
        print("4: Eliminar producto")
        print("5: Guardar datos y salir")
        
        opcion = input("Selecciona una opción: ")
        
        if opcion == '1':
            añadir_producto()
        elif opcion == '2':
            ver_productos()
        elif opcion == '3':
            actualizar_producto()
        elif opcion == '4':
            eliminar_producto()
        elif opcion == '5':
            guardar_datos()
            print("Datos guardados. Saliendo del programa.")
            break
        else:
            print("Por favor, selecciona una opción válida.")

# Ejecutar el programa
menu()
