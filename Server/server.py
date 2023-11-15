from multiprocessing.managers import ListProxy
import time
import json
import zmq
import networkx as nx

import src.loadGraph as lG
import src.algorithm as algo
import src.tools as tools

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")


class Server:
    def __init__(self):
        self.Grafo = nx.Graph()
        lG.loadGraph(self.Grafo)
        print("Graph loaded")

    def parseJSON(self, message):
        print(type(message))
        print(message["Departamento"])

        """
        "Departamento": "NULL",
        "Provincia": "NULL",
        "Distrito": "NULL",
        """

        """
        "listDep": "A"
        "listProv": "B"
        "listDis": "C"
        "Calles": "D"
        "STATS": "E"
        """

        listDep = self.listDepartamento(message)
        listProv = self.listProvincia(message)
        listDist = self.listDistrito(message)
        listCalles = self.listCalles(message)

        print(listDep)
        print(listProv)
        print(listDist)
        print(listCalles)

        dictInformacion = {
            "listaDepartamentos": listDep,
            "listaProvincias": listProv,
            "listaDistritos": listDist,
            "listCalles": listCalles,
            "listStats": {},
        }

        JSONinf = json.dumps(dictInformacion)

        socket.send_string(JSONinf)

    def listDepartamento(self, JSON):
        listDep = []

        if JSON["Departamento"] == "None":
            listDep = algo.getAll(self.Grafo, 1)
            listDep = tools.saveDepartamentosJSON(listDep)

        return listDep

    def listProvincia(self, JSON):
        listProv = []

        if JSON["Departamento"] == "None" and JSON["Provincia"] == "None":
            listProv = algo.getAll(self.Grafo, 2)
            listProv = tools.saveProvinciasJSON(listProv)

        elif JSON["Departamento"] != "None" and JSON["Provincia"] == "None":
            listProv = algo.getProvincia(self.Grafo, JSON["Departamento"])
            listProv = tools.saveProvinciasJSON(listProv)

        return listProv

    def listDistrito(self, JSON):
        listDist = []

        if JSON["Departamento"] == "None" and JSON["Provincia"] == "None":
            listDist = algo.getAll(self.Grafo, 3)
            listDist = tools.saveDistritosJSON(listDist)

        return listDist

    def listCalles(self, JSON):
        listCalles = []

        if (
            JSON["Departamento"] == "None"
            and JSON["Provincia"] == "None"
            and JSON["Distrito"] == "None"
        ):
            listCalles = algo.getAll(self.Grafo, 4)
            listCalles = tools.saveDepartamentosJSON(listCalles)

        return listCalles

    """
    def JSONlistDepartamento(self, JSONReceived):
        # Obtener todos los departamentos
        listDep = algo.getAll(self.Grafo, 1)
        listDep = tools.saveDepartamentosJSON(listDep)

        dictDep = {"departamentos": listDep}

        JSONlistDep = json.dumps(dictDep)

        print(JSONlistDep)
        socket.send_string(JSONlistDep)

        print("JSON Departamentos Sent")

    def JSONlistProvincia(self, JSONReceived):
        listProv = []

        # Obtener todas las provincias
        if JSONReceived["Departamento"] == "NULL":
            listProv = algo.getAll(self.Grafo, 2)

        # Obtener ciertas provincias
        else:
            listProv = algo.getProvincia(
                self.Grafo, tools.addDepartamentoString(JSONReceived["Departamento"])
            )
            pass

        listProv = tools.saveProvinciasJSON(listProv)

        dictProv = {"provincias": listProv}

        JSONlistProv = json.dumps(dictProv)

        print(JSONlistProv)

        socket.send_string(JSONlistProv)

        print("JSON Provincias Sent")

    def JSONlistDistrito(self, JSONReceived):
        listDis = []

        if (
            JSONReceived["Provincia"] == "NULL"
            and JSONReceived["Departamento"] == "NULL"
        ):
            # Obtener todos los distritos
            listDis = algo.getAll(self.Grafo, 3)
        elif (
            JSONReceived["Provincia"] != "NULL"
            and JSONReceived["Departamento"] == "NULL"
        ):
            # Obtener ciertos distritos - Provincias
            pass
        # Obtener ciertos distritos - Departamento
        elif (
            JSONReceived["Provincia"] == "NULL"
            and JSONReceived["Departamento"] != "NULL"
        ):
            listDis = algo.getDistritoD(
                self.Grafo, tools.addDepartamentoString(JSONReceived["Departamento"])
            )
        # Obtener cierto distrito - Departamento y Provincia
        else:
            pass
        pass

        listDis = tools.saveDistritosJSON(listDis)
        print(listDis)

        dictDis = {"distritos": listDis}

        JSONlistDis = json.dumps(dictDis)

        print(JSONlistDis)

        socket.send_string(JSONlistDis)

        print("JSON Distritos Sent")
    """


objServer = Server()

print("Ready")

while True:
    message = socket.recv_json()
    print("Received request: %s" % message)

    objServer.parseJSON(message)

    print("Message Sent")

    time.sleep(1)
