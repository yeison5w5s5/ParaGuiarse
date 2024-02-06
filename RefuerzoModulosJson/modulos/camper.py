from os import system
from .variables import modifyFileCamper, loadFileAcudiente
from .acudiente import listarTodos as listarAcudiente, obtenerAcudienteCedula, guardar as guardarAcudiente


def menu(dataCamper, dataAcudiente):
    print("""
MENU CAMPER       
    1. Guardar
    2. Editar
    3. Buscar
    4. Eliminar
    """)
    opc = int(input())
    match(opc):
        case 1: guardar(dataCamper, dataAcudiente)

def opcionAcudiente(dataAcudiente):
    listaAcudientesSelecionados = []
    bandera = True
    while(bandera):
        system("clear")
        dataAcudiente = loadFileAcudiente()
        print(f"{listarAcudiente(dataAcudiente)}")
        opc = int(input("¿El acudiente se encunetra es la lista?\n1.SI\n0.NO\n"))
        if(opc):
            cedulaAcudiente = int(input("copia y pega la cedula del acudiente segun el la lista: "))
            listaAcudientesSelecionados.append(obtenerAcudienteCedula(dataAcudiente, cedulaAcudiente))
            opc2 = int(input("¿Desea selecionar otro acudiente?\n1.SI\n0.NO\n"))
            if(not opc2):
                bandera = False
        else:
            guardarAcudiente(dataAcudiente)
    return listaAcudientesSelecionados

def guardar(dataCamper, dataAcudiente):

    info = {
        "n_identificacion": int(input("Ingrese su cedula: ")),
        "nombre": input("Ingrese su nombre: "),
        "apellido": input("Ingrese su apellido: "),
        "dirrecion": input("Ingrese la dirrecion: "),
        "acudiente": opcionAcudiente(dataAcudiente),
        "estado": "preInscrita"
    },
    dataCamper.append(info)
    modifyFileCamper(dataCamper)