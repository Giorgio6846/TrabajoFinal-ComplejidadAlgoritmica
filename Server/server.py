from multiprocessing.managers import ListProxy
from pickle import NONE
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

NONE_DATA = None


class Server:
    def __init__(self):
        self.Grafo = nx.Graph()
        lG.loadGraph(self.Grafo)
        print("Graph loaded")

    def parseJSON(self, message):
        if message["Departamento"] == "NULL":
            message["Departamento"] = None

        print(message)

        """
        "listDep": "A"
        "listProv": "B"
        "listDis": "C"
        "Calles": "D"
        "STATS": "E"
        """

        print(message["Departamento"], type(message["Departamento"]))
        print(message["Provincia"], type(message["Provincia"]))
        print(message["Distrito"], type(message["Distrito"]))

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

        if JSON["Departamento"] == NONE_DATA:
            listDep = algo.getAll(self.Grafo, 1)
            listDep = tools.saveDepartamentosJSON(listDep)

        return listDep

    def listProvincia(self, JSON):
        listProv = []

        if JSON["Departamento"] == NONE_DATA and JSON["Provincia"] == NONE_DATA:
            listProv = algo.getAll(self.Grafo, 2)
            listProv = tools.saveProvinciasJSON(listProv)

        elif JSON["Departamento"] != NONE_DATA and JSON["Provincia"] == NONE_DATA:
            listProv = algo.getProvincia(
                self.Grafo, tools.addDepartamentoString(JSON["Departamento"])
            )
            listProv = tools.saveProvinciasJSON(listProv)

        return listProv

    def listDistrito(self, JSON):
        listDist = []

        if JSON["Departamento"] == NONE_DATA and JSON["Provincia"] == NONE_DATA:
            listDist = algo.getAll(self.Grafo, 3)
            listDist = tools.saveDistritosJSON(listDist)

        elif JSON["Departamento"] != NONE_DATA and JSON["Provincia"] == NONE_DATA:
            listDist = algo.getDistritoD(
                self.Grafo, tools.addDepartamentoString(JSON["Departamento"])
            )
            listDist = tools.saveDistritosJSON(listDist)

        elif JSON["Departamento"] == NONE_DATA and JSON["Provincia"] != NONE_DATA:
            pass

        elif JSON["Departamento"] != NONE_DATA and JSON["Provincia"] != NONE_DATA:
            pass

        return listDist

    def listCalles(self, JSON):
        listCalles = []

        if (
            JSON["Departamento"] == NONE_DATA
            and JSON["Provincia"] == NONE_DATA
            and JSON["Distrito"] == NONE_DATA
        ):
            listCalles = algo.getAll(self.Grafo, 4)
            listCalles = tools.saveDepartamentosJSON(listCalles)

        return listCalles


objServer = Server()

print("Ready")

while True:
    message = socket.recv_json()
    print("Received request: %s" % message)

    objServer.parseJSON(message)

    print("Message Sent")

    time.sleep(1)
