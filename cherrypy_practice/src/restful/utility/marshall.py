import os

import datetime


def getVersionAsHexInTwoBytes(ver):
    ret = hex(ver)[2:]  # Remove the 0x prefix
    if len(ret) < 2:
        ret = "0" + ret

    datetime.now()
    return ret


class ReversedFileReader(file):
    """ Marshalling Version 1 """

    def __init__(self, *args, **kwargs):
        file.__init__(self, *args, **kwargs)
        self.totalSize = os.path.getsize(args[0])
        self.currPosition = self.totalSize
        super(ReversedFileReader, self).seek(self.totalSize)

    def read(self, length=None, *args, **kwargs):
        if self.currPosition == 0:
            return ''

        buf = None
        if length:
            self.currPosition = self.currPosition - length
            if self.currPosition < 0:
                length += self.currPosition
                self.currPosition = 0
            super(ReversedFileReader, self).seek(self.currPosition, *args, **kwargs)
            buf = super(ReversedFileReader, self).read(length)
        else:
            buf = super(ReversedFileReader, self).read()
        return buf[::-1]

    def seek(self, position, *args, **kwargs):
        self.currPosition = self.totalSize - position

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
