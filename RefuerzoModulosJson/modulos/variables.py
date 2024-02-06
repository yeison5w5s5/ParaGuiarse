import json
path = "storage/"

def loadFileCamper():
    with open(f"{path}/camper.json", "r") as f:
        return json.loads(f.read())

def modifyFileCamper(camper):
    with open(f"{path}/camper.json", "w") as f:
        f.write(json.dumps(camper, indent=4))
        f.close()
        return "El archivo camper.json ha sido modificado"
    
def loadFileAcudiente():
    with open(f"{path}/acudiente.json", "r") as f:
        return json.loads(f.read())

def modifyFileAcudiente(acudiente):
    with open(f"{path}/acudiente.json", "w") as f:
        f.write(json.dumps(acudiente, indent=4))
        f.close()
        return "El archivo acudiente.json ha sido modificado"
    
def loadFileContact():
    with open(f"{path}/contacto.json", "r") as f:
        return json.loads(f.read())

def modifyFileContact(contacto):
    with open(f"{path}/contacto.json", "w") as f:
        f.write(json.dumps(contacto, indent=4))
        f.close()
        return "El archivo contacto.json ha sido modificado"