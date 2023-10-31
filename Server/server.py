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
        print(message["type"])
        
        if message["type"] == "listDepartamento":
            print(message)
            self.JSONlistDepartamento(message)
        elif message["type"] == "listProvincia":
            print(message)
            self.JSONlistProvincia(message)
        elif message["type"] == "listDistrito":
            print(message)
            self.JSONlistDistrito(message)
            
    def JSONlistDepartamento(self, JSONReceived):
        
        #Obtener todos los departamentos
        listDep = algo.getDepartamentos(self.Grafo)
        listDep = tools.saveDepartamentosJSON(listDep)

        dictDep = {"departamentos": listDep}
        
        JSONlistDep = json.dumps(dictDep)

        print(JSONlistDep)
        socket.send_string(JSONlistDep)
        
        print("Sent JSON")
        
    def JSONlistProvincia(self, JSONReceived):
        if(JSONReceived["Departamento"] == "NULL"):
            pass         
        #Obtener todas las provincias
        else:
            pass
        #Obtener ciertas provincias
        
        pass
    
    def JSONlistDistrito(self, JSONReceived):
        if(JSONReceived["Provincia"] == "NULL" and JSONReceived["Departamento"] == "NULL"):
        #Obtener todos los distritos
            pass
        elif(JSONReceived["Provincia"] != "NULL" and JSONReceived["Departamento"] == "NULL"):
        #Obtener ciertos distritos - Provincias
            pass
        #Obtener ciertos distritos - Departamento
        elif(JSONReceived["Provincia"] == "NULL" and JSONReceived["Departamento"] != "NULL"):
            pass
        #Obtener cierto distrito - Departamento y Provincia
        else:
            pass
        pass
        
objServer = Server()

print("Ready")

while True:
    #  Wait for next request from client
    message = socket.recv_json()
    print("Received request: %s" % message)

    objServer.parseJSON(message)

    #  Do some 'work'
    time.sleep(1)

    #  Send reply back to client
    #socket.send_json({"World": "test1"})
    
