#!/usr/bin/env python
# -*- coding: utf-8 -*-



import Tornados.ioloop
import Tornados.web
import Tornados.httpclient

class MainHandler(Tornados.web.RequestHandler):
    @Tornados.web.asynchronous
    def get(self):
        http = Tornados.httpclient.AsyncHTTPClient()
        http.fetch("http://www.baidu.com",
                   callback=self.on_response)

    def on_response(self, response):
        if response.error: raise Tornados.web.HTTPError(500)
        self.write(response.body)
        self.finish()


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
