var zmq  = require("zeromq");
sock = new zmq.Request;

const ipAddress = "tcp://127.0.0.1:5555";

const decoder = new TextDecoder();

async function run(dataJSON) {
    sock.connect(ipAddress)
    console.log("Connected to server in tcp://0.0.0.0:5555")

    await(sock.send(dataJSON))
    const result = await sock.receive()
    
    /*
    respuestaJSON = await sock.receive()
    
    console.log("Test")
    console.log(respuestaJSON)
    
    console.log("Closed Connection")
    sock.close()
    */

    //var dataServer = decoder.decode(result)
    dataServer = decoder.decode(result[0])
    console.log(dataServer)
    return dataServer   
}