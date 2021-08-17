import tornado.ioloop
import tornado.web

ips = []

class MainHandler(tornado.web.RequestHandler):

  def get(self):
    # We use an object with only one value that is our list because of this error message:
    # TypeError: write() only accepts bytes, unicode, and dict objects. Lists not accepted for security reasons; see http://www.tornadoweb.org/en/stable/web.html#tornado.web.RequestHandler.write
    self.write({"ips":ips})

  def post(self):
    visible_address_pair = self.request.connection.stream.socket.getpeername()
    invisible_address = self.request.body.decode()
    visible_address = "{}:{}".format(*visible_address_pair)

    ips.append(invisible_address)
    ips.append(visible_address)
    print(invisible_address)
    print(visible_address)
    print(ips)

def make_app():
  return tornado.web.Application([
    (r"/", MainHandler),
  ])

if __name__ == "__main__":
  app = make_app()
  app.listen(8888)
  tornado.ioloop.IOLoop.current().start()
