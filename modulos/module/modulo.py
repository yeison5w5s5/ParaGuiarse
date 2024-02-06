import json

path = "module/storage/"
def carga():
    with open(path+"modulos.json", "r") as f:
        return json.loads(f.read())
       