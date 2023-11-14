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

    def sendClient(self, message):
        stadistics = self.stats(message)
        listDep = self.searchDep(message)
        listProv = self.searchProv(message)
        listDis = self.searchDis(message)
        
    def stats(self, message):
        pass

    def searchDep(self, message):
        pass

    def searchProv(self, message):
        pass

    def searchDis(self, message):
        pass

    def searchCalles(self, message):
        pass

objServer = Server()

print("Ready")

while True:
    #  Wait for next request from client
    message = socket.recv_json()
    print("Received request: %s" % message)

    objServer.sendClient(message)

    #  Do some 'work'
    time.sleep(1)
