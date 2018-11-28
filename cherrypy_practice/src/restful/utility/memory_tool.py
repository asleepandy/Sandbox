# -*- coding: utf-8 -*-
import pdb
import random

import cherrypy, time, os, gc, objgraph as og
from pympler import tracker, muppy, summary
from guppy import hpy
# tr = tracker.SummaryTracker()
# sum1 = summary.summarize(muppy.get_objects())
hp = hpy()
before = hp.heap()


def output_memory_state1():
    global sum1
    sum2 = summary.summarize(muppy.get_objects())
    if sum1 is not None:
        diff = summary.get_diff(sum1, sum2)
        summary.print_(diff)
    sum1 = sum2


def output_memory_heapy():
    global before
    after = hp.heap()
    leftover = after - before
    print leftover.bytype
    pdb.set_trace()
    before = after
    del after
    del leftover
    # print hp.heap()


def output_memory_state():
    tr = tracker.SummaryTracker()
    fp = './logs/memory_obj_{}.txt'

    while True:
        # print 'start record memory...'
        # cherrypy.log.error(tr.print_diff())

        time.sleep(100 + random.randint(1, 80))
        gc.collect()

        with open(fp.format(os.getpid()), 'aw') as ff:
            ff.write(gc.collect())
            ff.write(gc.collect())
            og.show_growth(limit=None, shortnames=False, file=ff)

        """
        text = []
        text.append('pid:{:d} memory check in heap...'.format(os.getpid()))
        text.append("{0} {1:d}".format(time.strftime('%Y/%m/%d %H:%M:%S'), os.getpid()))
        all_objects = muppy.get_objects()

        sum = summary.summarize(all_objects)

        for line in summary.format_(sum, limit=20):
            text.append(line)
        # print '\r\n'.join(text)
        # cherrypy.log.access(msg='\r\n'.join(text))

        f = open(fp.format(os.getpid()), 'aw')
        f.write('\r\n'.join(text))
        f.write('\r\n')
        f.flush()
        f.close()
        all_objects = None
        sum = None
        """