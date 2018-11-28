from twisted.internet.defer import Deferred


def myCallback(result):
    print result


def myErrback(f):
    print f


def addBold(result):
    return "<b>%s</b>" % (result,)


def addItalic(result):
    return "<i>%s</i>" % (result,)


def printHTML(result):
    print result

d = Deferred()
# d.addCallback(myCallback)
d.addCallbacks(myCallback, myErrback)
d.errback(u"Triggering callback.")
# d.addErrback(myErrback)
# d.errback('2321')
# d.addCallback(addItalic)
# d.addCallback(addBold)
# d.addCallback(printHTML)
# d.callback("Hello world!")
