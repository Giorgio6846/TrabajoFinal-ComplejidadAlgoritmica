import zerorpc
import gevent, signal

class PythermalApi: 
    def echo(self,text):
        return text

port = 42690
address = 'tcp://127.0.0.1:' + port
s = zerorpc.Server(PythermalApi())
s.bind(address)

gevent.signal(signal.SIGTERM, s.stop)
gevent.signal(signal.SIGINT, s.stop)

s.run()

