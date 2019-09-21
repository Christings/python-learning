#!/usr/bin/env python
# -*- coding: utf-8 -*-



import Tornados.ioloop
import Tornados.web

class MainHandler(Tornados.web.RequestHandler):
    def get(self):
        self.write("Hello world")

def make_app():
    return Tornados.web.Application([
        (r"/", MainHandler),
    ])

def main():
    app = make_app()
    app.listen(8888)
    Tornados.ioloop.IOLoop.current().start()

if __name__ == "__main__":
    main()
