#!/usr/bin/env python
# -*- coding: utf-8 -*-



import Tornados.ioloop
import Tornados.web
import Tornados.httpclient


class MainHandler(Tornados.web.RequestHandler):
    @Tornados.gen.coroutine
    def get(self):
        http = Tornados.httpclient.AsyncHTTPClient()
        response = yield http.fetch("http://www.baidu.com")
        self.write(response.body)


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
