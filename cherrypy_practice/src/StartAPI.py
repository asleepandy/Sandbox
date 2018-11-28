# -*- coding:utf-8 -*-
import cherrypy
import gc
import glob
import os
import pdb

from cherrypy.lib.static import serve_file, serve_fileobj
from sys import argv

from restful.utility.marshall import ReversedFileReader, getVersionAsHexInTwoBytes
from restful.utility.memory_tool import output_memory_heapy


class Root:
    def index(self, directory="."):
        html = """<html><body><h2>Here are the files in the selected directory:</h2>
        <a href="index?directory=%s">Up</a><br />
        """ % os.path.dirname(os.path.abspath(directory))

        for filename in glob.glob(directory + '/*'):
            absPath = os.path.abspath(filename)
            if os.path.isdir(absPath):
                html += '<a href="/index?directory=' + absPath + '">' + os.path.basename(filename) + "</a> <br />"
            else:
                html += '<a href="/download/?filepath=' + absPath + '">' + os.path.basename(filename) + "</a> <br />"

        html += """</body></html>"""
        return html
    index.exposed = True


class Download:

    def index(self, filepath):
        gc.collect()
        output_memory_heapy()
        # pdb.set_trace()
        version = getVersionAsHexInTwoBytes(1)
        version += getVersionAsHexInTwoBytes(1)
        cherrypy.response.headers['Content-Extra'] = version
        f = ReversedFileReader(filepath)
        return serve_fileobj(f, "application/zip", "attachment", 'all.sbz')
    index.exposed = True


def main():
    root = Root()
    root.download = Download()
    cherrypy.quickstart(root)


if __name__ == '__main__':
    if len(argv) == 1:
        main()
    else:
        args = []
        for i in argv[1:]:
            args.append(int(i))
        main(*args)
