from twisted.internet import defer
from twisted.internet import reactor


class HeadlineRetriever(object):
    def processHeadline(self, headline):
        if len(headline) > 50:
            self.d.errback(u"The headline ``%s'' is too long!" % (headline,))
        else:
            self.d.callback(headline)

    def _toHTML(self, result):
        return "<h1>%s</h1>" % (result,)

    def getHeadline(self, input):
        self.d = defer.Deferred()
        reactor.callLater(1, self.processHeadline, input)
        self.d.addCallback(self._toHTML)
        return self.d


def printData(result):
    print result
    reactor.stop()


def printError(fail):
    print fail
    reactor.stop()

h = HeadlineRetriever()
d = h.getHeadline(u"Breaking News: Twisted Takes Us to the Moon!")
d.addCallbacks(printData, printError)

reactor.run()
