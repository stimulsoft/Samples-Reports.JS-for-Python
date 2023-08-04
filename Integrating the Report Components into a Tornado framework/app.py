import asyncio
import tornado
import os
from tornado.web import url

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")

class ViewerHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("viewer.html")

class DesignerHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("designer.html")

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            url(r"/", MainHandler),
            url(r"/viewer", ViewerHandler, name="viewer"),
            url(r"/designer", DesignerHandler, name="designer"),
        ]
        settings = dict(
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
        )
        tornado.web.Application.__init__(self, handlers, **settings)

PORT=8000
async def main():
    app = Application()
    app.listen(PORT)
    print("Starting development server at http://127.0.0.1:{0}/".format(PORT))
    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())