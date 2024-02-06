from os import system
import json
from .validate import menuNoValid
from .data import trainer, generos

def save():
    system("clear")
    print("""
    ***************************
    *  Formulario del trainer  *
    ***************************
    """)
    info = {
        "Nombre": input("Ingrese el nombre del trainer\n"),
        "Apellido": input("Ingrese el apellido del trainer\n"),
        "Edad": int(input("Ingrese la edad del trainer\n")),
        "Genero": input("Elija su genero:\n\t"+"\t".join([f"{generos.index(i)+1}. {i}\n" for i in sorted(generos)]))
    }
    trainer.append(info)
    with open("module/storage/trainer.json", "w") as f:
        data = json.dumps(trainer, indent=4)
        f.write(data)
        f.close()
    return "Sucessfully trainer"

def edit():
    bandera=True
    while (bandera):
        system("clear")
        print("""
        ***************************
        * Acualizacion del trainer *
        ***************************
        """)
        codigo = int(input("Ingrese el codigo del trainer que deseas actualizar"))
        print(f"""
________________________
Codigo: {codigo}
Nombre: {trainer[codigo].get('Nombre')}
Apellido: {trainer[codigo].get('Apellido')}
Edad: {trainer[codigo].get('Edad')}
Genero: {trainer[codigo].get('Genero')}
________________________
        """)
        print("¿Este es el trainer que deseas actualizar?")
        print("1. Si")
        print("2. No")
        print("3. Salir")
        opc = int(input())
        if(opc == 1):
            info = {
                "Nombre": input("Ingrese el nombre del trainer\n"),
                "Apellido": input("Ingrese el apellido del trainer\n"),
                "Edad": int(input("Ingrese la edad del trainer\n")),
                "Genero": input("Elija su genero:\n\t"+"\t".join([f"{generos.index(i)+1}. {i}\n" for i in sorted(generos)]))
            }
            trainer[codigo] = info
            with open("module/storage/trainer.json", "w") as f:
                data = json.dumps(trainer, indent=4)
                f.write(data)
                f.close()
            bandera = False
        elif(opc == 3):
            bandera = False
    return "Edit to trainer"

def search():
    system("clear")
    print("""
    ********************
    * Lista de trainers *
    ********************
    """)
    for i,val in enumerate(trainer):
        print(f"""
________________________
Codigo: {i}
Nombre: {val.get('Nombre')}
Apellido: {val.get('Apellido')}
Edad: {val.get('Edad')}
Genero: {val.get('Genero')}
________________________
        """)
    return "The trainer is available"

def delete():
    bandera = True
    while(bandera):
        system("clear")
        print("""
        ***************************
        * Eliminacion del trainer  *
        ***************************
        """)
        codigo = int(input("Ingrese el codigo del trainer que deseas eliminar: "))
        print(f"""
________________________
Codigo: {codigo}
Nombre: {trainer[codigo].get('Nombre')}
Apellido: {trainer[codigo].get('Apellido')}
Edad: {trainer[codigo].get('Edad')}
Genero: {trainer[codigo].get('Genero')}
________________________
        """)
        print("¿Este es el trainer que deseas actualizar?")
        print("1. Si")
        print("2. No")
        print("3. Salir")
        opc = int(input())
        if(opc == 1):
            trainer.pop(codigo)
            with open("module/storage/trainer.json", "w") as f:
                data = json.dumps(trainer, indent=4)
                f.write(data)
                f.close()
            bandera = False
        elif(opc == 3):
            bandera = False
    return "trainer deleted"

def menu():
    bandera=True
    while (bandera):
        print("CRUD del trainer")
        print("\t1. Guardar trainer")
        print("\t2. Buscar trainer")
        print("\t3. Actualizar trainer")
        print("\t4. Eliminar trainer")
        print("\t0. Atras")
        opc = int(input())
        match(opc):
            case 1: save()
            case 2: search()
            case 3: edit()
            case 4: delete()
            case 0:
                system("clear")
                bandera = False
            case _: menuNoValid(opc)