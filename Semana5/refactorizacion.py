def ingresar_puntuacion_y_comentario():
    while True:
        print('Por favor, introduzca una puntuación en una escala de 1 a 5')
        point = input()
        
        if point.isdecimal():
            point = int(point)
            
            if point <= 0 or point > 5:  # Verificar si es menor que 0 o mayor que 5
                print('Por favor, introduzca un valor entre 1 y 5')
            else:
                print('Por favor, introduzca un comentario')
                comment = input()
                post = f'puntuación: {point} comentario: {comment}'
                with open("data.txt", 'a') as file_pc:  # Usar with para manejar archivos
                    file_pc.write(f'{post}\n')
                break
        else:
            print('Por favor, introduzca la puntuación en números')

def comprobar_resultados():
    print('Resultados hasta la fecha:')
    with open("data.txt", "r") as read_file:  # Usar with para manejar archivos
        print(read_file.read())

def main():
    while True:
        print('Seleccione el proceso que desea aplicar')
        print('1: Ingresar puntuación y comentario')
        print('2: Comprobar los resultados obtenidos hasta ahora.')
        print('3: Finalizar')
        
        num = input()
        
        if num.isdecimal():
            num = int(num)
            if num == 1:
                ingresar_puntuacion_y_comentario()  # Llamada al método para ingresar puntuación y comentario
            elif num == 2:
                comprobar_resultados()  # Llamada al método para comprobar resultados
            elif num == 3:
                print('Finalizando')
                break  # Finaliza el procesamiento
            else:
                print('Introduzca un número del 1 al 3')
        else:
            print('Introduzca un número del 1 al 3')

# Ejecutar el programa
if __name__ == "__main__":
    main()
