from re import M
from numpy import sort
import zmq
import json

context = zmq.Context()

#  Socket to talk to server
print("Connecting to hello world server…")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

messageServer = json.dumps(
    {   
        "type": "ListDepartamentos",
        "Departamentos": "NULL",
        "Provincias": "NULL",
        "Distritos": "NULL"
    }
)

#  Do 10 requests, waiting each time for a response
for request in range(10):
    print(f"Sending request {request} …")
    socket.send_json(messageServer)

    #  Get the reply.
    message = socket.recv_json()
    print(f"Received reply {request} [ {message} ]")