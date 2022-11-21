from Sintaxis import Sintaxis

def mostrar_menu(opciones):
    print('Bienvenido, seleccione una opción:')
    for clave in sorted(opciones):
        print(f' {clave}) {opciones[clave][0]}')




def leer_opcion(opciones):
    while (a := input('Opción: ')) not in opciones:
        print('Opción incorrecta, vuelva a intentarlo.')
    return a




def ejecutar_opcion(opcion, opciones):
    opciones[opcion][1]()




def generar_menu(opciones, opcion_salida):
    opcion = None
    while opcion != opcion_salida:
        mostrar_menu(opciones)
        opcion = leer_opcion(opciones)
        ejecutar_opcion(opcion, opciones)
        print()




def menu_principal():
    opciones = {
        '1': ('Opción 1: Verificar oración', accion1),
        '2': ('Opción 2: Salir', salir)
      
    }



    generar_menu(opciones, '2')




def accion1():
    oraciones = input('Porfavor ingrese una frase para ser evaluada' "\n").split("\n")
    verificador = Sintaxis()
    print(verificador.verificar(oraciones))



def salir():
    print('Saliendo')




if __name__ == '__main__':
    menu_principal()

