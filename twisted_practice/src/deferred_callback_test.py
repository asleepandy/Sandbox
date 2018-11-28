from twisted.internet.defer import Deferred


def callback1(result):
    print u"Callback 1 said:", result
    return result


def callback2(result):
    print u"Callback 2 said:", result


def callback3(result):
    raise Exception(u"Callback 3")


def errback1(failure):
    print u"Errback 1 had an an error on", failure
    return failure


def errback2(failure):
    raise Exception(u"Errback 2")


def errback3(failure):
    print u"Errback 3 took care of", failure
    return u"Everything is fine now."

d = Deferred()
# d.addCallback(callback1)
# d.addCallback(callback2)
d.addCallback(callback3)
# d.addErrback(errback1)
# d.addErrback(errback2)
# d.addErrback(errback3)
d.addCallbacks(callback2, errback3)
d.addCallbacks(callback1, errback2)
d.callback(u'Test')
# print (d.callbacks)
# d.errback(u'Test')

