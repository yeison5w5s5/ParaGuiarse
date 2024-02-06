import modulos.variables as variables
import modulos.camper as camper

dataCamper = variables.loadFileCamper()
dataAcudiente = variables.loadFileAcudiente()
dataContacto = variables.loadFileContact()


camper.menu(dataCamper, dataAcudiente)

