import Tornados.ioloop
import Tornados.web


class MainHandler(Tornados.web.RequestHandler):
    def get(self):
        self.write("Hello world1")


def make_app():
    return Tornados.web.Application(
        [
            (r"/index", MainHandler),
            (r"/entry/([^/]+)", EntryHandler),
        ],
        debug=True)


class EntryHandler(Tornados.web.RequestHandler):
    def get(self, slug):
        self.write(slug)


def main():
    app = make_app()
    app.listen(8888)
    try:
        Tornados.ioloop.IOLoop.current().start()
    except KeyboardInterrupt:
        Tornados.ioloop.IOLoop.current().stop()
    print("killed")


if __name__ == "__main__":
    main()
