import threading
from conexoes import rabbit
from conexoes import socket_obj
import tornado.ioloop

main_io_loop = tornado.ioloop.IOLoop.current()


def main():
    threading.Thread(target=rabbit.procurar, args=()).start()
    application = tornado.web.Application([(r"/", socket_obj.WebSocketHandler), ])
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()

def get_main_io_loop():
    global main_io_loop
    return main_io_loop

if __name__ == "__main__":
    main()