# from module.camper import *
# from module.camper import save
# from module.camper import delete as eliminar
# import json
# from os import system
# import module.camper as camper
# import module.trainer as trainer
# from module.validate import menuNoValid
# def menu():
#     print("Sistema de almacenamiento de datos para campus")
#     print("\t1. Informacion del camper")
#     print("\t2. Informacion del trainer")
#     print("\t0. Salir")
# bandera=True
# while (bandera):
#     menu()
#     opc = int(input())
#     match(opc):
#         case 1:
#             with open("module/storage/camper.json", "r") as f:
#                 camper.camper = json.loads(f.read())
#                 f.close()
#                 system("clear")
#                 camper.menu()
#         case 2:
#             with open("module/storage/trainer.json", "r") as f:
#                 trainer.trainer = json.loads(f.read())
#                 f.close()
#                 system("clear")
#                 trainer.menu()
#         case 0:
#             system("clear")
#             bandera = False
#         case _:
#             menuNoValid(opc)




import json
import module.ruta as ruta
import module.modulo as modulo
from module.data import modulos, rutas

rutas = ruta.carga()
modulos = modulo.carga()

# print(rutas)
# print(modulos)

print("CRUD de rutas")
print("1. Asignar modulos a las ruta")
print("2. Buscar")
print("3. Actualizar")
print("4. Eliminar")
opc = int(input())

def plantilla(data):
    lista = []
    for i,val in enumerate(data):
        lista.append(f"\n\t\t{i+1} - {val}")
    return "".join(lista)

def asignarModulos():
    # Temario: {"".join([f"{i} - {val}" for i,val in enumerate(val.get("temario"))])}
    selecion = set()
    nuevaLista = []
    while(True):
        for val in modulos:
            print(f"""
            ________________
            Codigo: {val.get("codigo")}
            Nombre: {val.get("nombre_modulo")}
            Prioridad: {val.get("prioridad")}
            Temario: {plantilla(val.get("temario"))}
            ________________
            """)

        selecion.add(input("¿Selecione el modulo que deseas ingresando el codigo?\n"))
        if(not int(input("¿Deseas agregar otro modulo?\n1.SI\n0.NO\n"))):
            for i in selecion:
                for val in modulos:
                   if(val.get("codigo") == i):
                        nuevaLista.append(val)
            break
    return nuevaLista
match(opc):
    case 1:
        Myruta = {
            "codigo": f"R{len(rutas)+1}",
            "nombre_ruta": input("Ingrese el nombre de la ruta: "),
            "modulo": asignarModulos()
        }
        rutas.append(Myruta)
        path = "module/storage/"
        with open(path+"rutas.json", "w") as f:
            f.write(json.dumps(rutas, indent=4))
            f.close()
    case _:
        print("La opcion no esta habilitada")























# import json
# info = {
#     "Nombre": input("Ingrese el nombre: "),
#     "Telefono" : [
#         {
#             f"{'Fijo' if(int(input('1. Fijo 0. Celular: '))) else 'Celular'}": 
#             input(f'Numero de contacto {x+1}: ')
#         } 
#         for x in range((int(input("¿Cuantos numero de contacto tiene?: ")))) 
#     ] 
# }

# busqueda = input("Numero")
# for x,val in enumerate(info["Telefono"]):
#     if( busqueda in val.get("Celular")):
#         print(val)
        
