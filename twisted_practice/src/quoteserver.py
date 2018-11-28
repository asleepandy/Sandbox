from twisted.internet.protocol import Factory
from twisted.internet import reactor, protocol


class QuoteProtocol(protocol.Protocol):
    def __init__(self, factory):
        self.factory = factory

    def connectionMade(self):
        self.factory.num_connections += 1

    def dataReceived(self, data):
        print "Number of active connections: %d" % (self.factory.num_connections,)
        print "> Received: ``%s''\n> Sending: ``%s''" % (data, self.get_quote())
        self.transport.write(self.get_quote())
        self.update_quote(data)

    def connectionLost(self, reason):
        self.factory.num_connections -= 1

    def get_quote(self):
        return self.factory.quote

    def update_quote(self, quote):
        self.factory.quote = quote


class QuoteFactory(Factory):
    num_connections = 0

    def __init__(self, quote=None):
        self.quote = quote or "An apple a day keeps the doctor away"

    def buildProtocol(self, addr):
        return QuoteProtocol(self)

reactor.listenTCP(8000, QuoteFactory())
reactor.run()
