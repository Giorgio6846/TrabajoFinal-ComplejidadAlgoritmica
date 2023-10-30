const zmq  = require("zeromq")

async function run(dataJSON) {
    const sock = new zmq.Request

    sock.connect("tcp://127.0.0.1:5555")
    console.log("Producer bound to port 5555")

    await sock.send(dataJSON)
    respuestaJSON = await sock.receive()
    
    console.log("Test")
    console.log(respuestaJSON)
    
    console.log("Closed Connection")
    sock.close()

    return respuestaJSON
}