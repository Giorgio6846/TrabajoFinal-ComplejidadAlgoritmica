import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)

socket.bind("tcp://0.0.0.0:5555")

while True:
    message = socket.recv_json()
    print("Received Request: ", message)
    ret = {"a": 123, "b":321}
    socket.send_json(ret)