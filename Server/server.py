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
            self.JSONlistDepartamento()

    def JSONlistDepartamento(self):
        listDep = algo.getDepartamentos(self.Grafo)
        listDep = tools.saveDepartamentosJSON(listDep)

        dictDep = {"departamentos": listDep}
        
        JSONlistDep = json.dumps(dictDep)

        print(JSONlistDep)
        socket.send_string(JSONlistDep)
        
        print("Sent JSON")
        
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
    
