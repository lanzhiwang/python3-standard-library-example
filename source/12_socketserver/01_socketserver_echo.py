#!/usr/bin/env python3
"""Echo server example for SocketServer"""

# end_pymotw_header
import logging
import sys
import socketserver

logging.basicConfig(
    level=logging.DEBUG,
    format="%(name)s: %(message)s",
)


class EchoRequestHandler(socketserver.BaseRequestHandler):

    def __init__(self, request, client_address, server):
        self.logger = logging.getLogger("EchoRequestHandler")
        self.logger.debug("__init__")
        socketserver.BaseRequestHandler.__init__(self, request, client_address, server)
        return

    def setup(self):
        self.logger.debug("setup")
        return socketserver.BaseRequestHandler.setup(self)

    def handle(self):
        self.logger.debug("handle")

        # Echo the back to the client
        data = self.request.recv(1024)
        self.logger.debug('recv()->"%s"', data)
        self.request.send(data)
        return

    def finish(self):
        self.logger.debug("finish")
        return socketserver.BaseRequestHandler.finish(self)


class EchoServer(socketserver.TCPServer):

    def __init__(
        self,
        server_address,
        handler_class=EchoRequestHandler,
    ):
        self.logger = logging.getLogger("EchoServer")
        self.logger.debug("__init__")
        socketserver.TCPServer.__init__(self, server_address, handler_class)
        return

    def server_activate(self):
        self.logger.debug("server_activate")
        socketserver.TCPServer.server_activate(self)
        return

    def serve_forever(self, poll_interval=0.5):
        self.logger.debug("waiting for request")
        self.logger.info("Handling requests, press <Ctrl-C> to quit")
        socketserver.TCPServer.serve_forever(self, poll_interval)
        return

    def handle_request(self):
        self.logger.debug("handle_request")
        return socketserver.TCPServer.handle_request(self)

    def verify_request(self, request, client_address):
        self.logger.debug("verify_request(%s, %s)", request, client_address)
        return socketserver.TCPServer.verify_request(
            self,
            request,
            client_address,
        )

    def process_request(self, request, client_address):
        self.logger.debug("process_request(%s, %s)", request, client_address)
        return socketserver.TCPServer.process_request(
            self,
            request,
            client_address,
        )

    def finish_request(self, request, client_address):
        self.logger.debug("finish_request(%s, %s)", request, client_address)
        return socketserver.TCPServer.finish_request(
            self,
            request,
            client_address,
        )

    def close_request(self, request_address):
        self.logger.debug("close_request(%s)", request_address)
        return socketserver.TCPServer.close_request(
            self,
            request_address,
        )

    def shutdown(self):
        self.logger.debug("shutdown()")
        return socketserver.TCPServer.shutdown(self)

    def server_close(self):
        self.logger.debug("server_close")
        return socketserver.TCPServer.server_close(self)


if __name__ == "__main__":
    import socket
    import threading

    address = ("localhost", 0)  # let the kernel assign a port
    server = EchoServer(address, EchoRequestHandler)
    ip, port = server.server_address  # what port was assigned?

    # Start the server in a thread
    t = threading.Thread(target=server.serve_forever)
    t.setDaemon(True)  # don't hang on exit
    t.start()

    logger = logging.getLogger("client")
    logger.info("Server on %s:%s", ip, port)

    # Connect to the server
    logger.debug("creating socket")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    logger.debug("connecting to server")
    s.connect((ip, port))

    # Send the data
    message = "Hello, world".encode()
    logger.debug("sending data: %r", message)
    len_sent = s.send(message)

    # Receive a response
    logger.debug("waiting for response")
    response = s.recv(len_sent)
    logger.debug("response from server: %r", response)

    # Clean up
    server.shutdown()
    logger.debug("closing socket")
    s.close()
    logger.debug("done")
    server.socket.close()

"""
EchoServer: __init__
EchoServer: server_activate
EchoServer: waiting for request
client: Server on 127.0.0.1:52058
client: creating socket
EchoServer: Handling requests, press <Ctrl-C> to quit
client: connecting to server
client: sending data: b'Hello, world'
EchoServer: verify_request(<socket.socket fd=7, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 52058), raddr=('127.0.0.1', 52059)>, ('127.0.0.1', 52059))
client: waiting for response
EchoServer: process_request(<socket.socket fd=7, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 52058), raddr=('127.0.0.1', 52059)>, ('127.0.0.1', 52059))
EchoServer: finish_request(<socket.socket fd=7, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 52058), raddr=('127.0.0.1', 52059)>, ('127.0.0.1', 52059))
EchoRequestHandler: __init__
EchoRequestHandler: setup
EchoRequestHandler: handle
EchoRequestHandler: recv()->"b'Hello, world'"
EchoRequestHandler: finish
client: response from server: b'Hello, world'
EchoServer: close_request(<socket.socket fd=7, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 52058), raddr=('127.0.0.1', 52059)>)
EchoServer: shutdown()
client: closing socket
client: done


client: Server on 127.0.0.1:52058
client: creating socket
client: connecting to server
client: sending data: b'Hello, world'
client: waiting for response
client: response from server: b'Hello, world'
client: closing socket
client: done

EchoServer: __init__
EchoServer: server_activate
EchoServer: waiting for request
EchoServer: Handling requests, press <Ctrl-C> to quit
EchoServer: verify_request(<socket.socket fd=7, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 52058), raddr=('127.0.0.1', 52059)>, ('127.0.0.1', 52059))
EchoServer: process_request(<socket.socket fd=7, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 52058), raddr=('127.0.0.1', 52059)>, ('127.0.0.1', 52059))
EchoServer: finish_request(<socket.socket fd=7, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 52058), raddr=('127.0.0.1', 52059)>, ('127.0.0.1', 52059))
EchoServer: close_request(<socket.socket fd=7, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 52058), raddr=('127.0.0.1', 52059)>)
EchoServer: shutdown()

EchoRequestHandler: __init__
EchoRequestHandler: setup
EchoRequestHandler: handle
EchoRequestHandler: recv()->"b'Hello, world'"
EchoRequestHandler: finish

################################################

client: Server on 127.0.0.1:52219
client: creating socket
client: connecting to server
client: sending data: b'Hello, world'
client: waiting for response
client: response from server: b'Hello, world'
client: closing socket
client: done

EchoServer: __init__
EchoServer: server_activate
EchoServer: waiting for request
EchoServer: Handling requests, press <Ctrl-C> to quit
EchoServer: verify_request(<socket.socket fd=7, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 52219), raddr=('127.0.0.1', 52220)>, ('127.0.0.1', 52220))
EchoServer: process_request(<socket.socket fd=7, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 52219), raddr=('127.0.0.1', 52220)>, ('127.0.0.1', 52220))
EchoServer: finish_request(<socket.socket fd=7, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 52219), raddr=('127.0.0.1', 52220)>, ('127.0.0.1', 52220))
EchoServer: close_request(<socket.socket fd=7, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 52219), raddr=('127.0.0.1', 52220)>)
EchoServer: shutdown()

EchoRequestHandler: __init__
EchoRequestHandler: setup
EchoRequestHandler: handle
EchoRequestHandler: recv()->"b'Hello, world'"
EchoRequestHandler: finish

"""
