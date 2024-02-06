from .variables import modifyFileAcudiente

def listarTodos(dataAcudiente):
    plantilla = "Lista de Acudientes\n"
    for i,val in enumerate(dataAcudiente):
        plantilla += f"""
        ___________________________
        Cedula: {val.get("n_identificacion")}
        Nombre Completo: {val.get("nombre")}
        ___________________________        
        """
    return plantilla

def obtenerAcudienteCedula(dataAcudiente, cedula):
    for i,val in enumerate(dataAcudiente):
        if(val.get("n_identificacion") == cedula):
            return val

def guardar(dataAcudiente):
    info = {
        "n_identificacion": int(input("Ingrese su cedula del acudiente: ")),
        "nombre": input("Ingrese el nombre del acudiente: "),
    }
    dataAcudiente.append(info)
    modifyFileAcudiente(dataAcudiente)