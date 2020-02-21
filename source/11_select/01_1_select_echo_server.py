#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2010 Doug Hellmann.  All rights reserved.
#
"""Server half of echo example.
"""

#end_pymotw_header
import select
import socket
import sys
import queue

# Create a TCP/IP socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setblocking(0)

# Bind the socket to the port
server_address = ('localhost', 10001)
print('starting up on {} port {}'.format(*server_address),
      file=sys.stderr)
server.bind(server_address)

# Listen for incoming connections
server.listen(5)

# Sockets from which we expect to read
inputs = [server]

# Sockets to which we expect to write
outputs = []

# Outgoing message queues (socket:Queue)
message_queues = {}

while inputs:

    # Wait for at least one of the sockets to be
    # ready for processing
    print('waiting for the next event', file=sys.stderr)
    readable, writable, exceptional = select.select(inputs,
                                                    outputs,
                                                    inputs)

    # Handle inputs
    for s in readable:

        if s is server:
            # A "readable" socket is ready to accept a connection
            connection, client_address = s.accept()
            print('  connection from', client_address,
                  file=sys.stderr)
            connection.setblocking(0)
            inputs.append(connection)

            # Give the connection a queue for data
            # we want to send
            message_queues[connection] = queue.Queue()

        else:
            data = s.recv(1024)
            if data:
                # A readable client socket has data
                print('  received {!r} from {}'.format(
                    data, s.getpeername()), file=sys.stderr,
                )
                message_queues[s].put(data)
                # Add output channel for response
                if s not in outputs:
                    outputs.append(s)

            else:
                # Interpret empty result as closed connection
                print('  closing', client_address,
                      file=sys.stderr)
                # Stop listening for input on the connection
                if s in outputs:
                    outputs.remove(s)
                inputs.remove(s)
                s.close()

                # Remove message queue
                del message_queues[s]

    # Handle outputs
    for s in writable:
        try:
            next_msg = message_queues[s].get_nowait()
        except queue.Empty:
            # No messages waiting so stop checking
            # for writability.
            print('  ', s.getpeername(), 'queue empty',
                  file=sys.stderr)
            outputs.remove(s)
        else:
            print('  sending {!r} to {}'.format(next_msg,
                                                s.getpeername()),
                  file=sys.stderr)
            s.send(next_msg)

    # Handle "exceptional conditions"
    for s in exceptional:
        print('exception condition on', s.getpeername(),
              file=sys.stderr)
        # Stop listening for input on the connection
        inputs.remove(s)
        if s in outputs:
            outputs.remove(s)
        s.close()

        # Remove message queue
        del message_queues[s]

"""
starting up on localhost port 10001
waiting for the next event
  connection from ('127.0.0.1', 51775)
waiting for the next event
  connection from ('127.0.0.1', 51776)
waiting for the next event
  received b'This is the message. ' from ('127.0.0.1', 51775)
  received b'This is the message. ' from ('127.0.0.1', 51776)
waiting for the next event
  sending b'This is the message. ' to ('127.0.0.1', 51775)
  sending b'This is the message. ' to ('127.0.0.1', 51776)
waiting for the next event
   ('127.0.0.1', 51775) queue empty
   ('127.0.0.1', 51776) queue empty
waiting for the next event
  received b'It will be sent ' from ('127.0.0.1', 51775)
waiting for the next event
  received b'It will be sent ' from ('127.0.0.1', 51776)
  sending b'It will be sent ' to ('127.0.0.1', 51775)
waiting for the next event
   ('127.0.0.1', 51775) queue empty
  sending b'It will be sent ' to ('127.0.0.1', 51776)
waiting for the next event
   ('127.0.0.1', 51776) queue empty
waiting for the next event
  received b'in parts.' from ('127.0.0.1', 51775)
waiting for the next event
  received b'in parts.' from ('127.0.0.1', 51776)
  sending b'in parts.' to ('127.0.0.1', 51775)
waiting for the next event
   ('127.0.0.1', 51775) queue empty
  sending b'in parts.' to ('127.0.0.1', 51776)
waiting for the next event
   ('127.0.0.1', 51776) queue empty
waiting for the next event
  closing ('127.0.0.1', 51776)
waiting for the next event
  closing ('127.0.0.1', 51776)


waiting for the next event
  connection from ('127.0.0.1', 51822)
waiting for the next event
  connection from ('127.0.0.1', 51823)
waiting for the next event
  received b'This is the message. ' from ('127.0.0.1', 51822)
  received b'This is the message. ' from ('127.0.0.1', 51823)
waiting for the next event
  sending b'This is the message. ' to ('127.0.0.1', 51822)
  sending b'This is the message. ' to ('127.0.0.1', 51823)
waiting for the next event
   ('127.0.0.1', 51822) queue empty
   ('127.0.0.1', 51823) queue empty
waiting for the next event
  received b'It will be sent ' from ('127.0.0.1', 51822)
  received b'It will be sent ' from ('127.0.0.1', 51823)
waiting for the next event
  sending b'It will be sent ' to ('127.0.0.1', 51822)
  sending b'It will be sent ' to ('127.0.0.1', 51823)
waiting for the next event
   ('127.0.0.1', 51822) queue empty
   ('127.0.0.1', 51823) queue empty
waiting for the next event
  received b'in parts.' from ('127.0.0.1', 51822)
waiting for the next event
  received b'in parts.' from ('127.0.0.1', 51823)
  sending b'in parts.' to ('127.0.0.1', 51822)
waiting for the next event
   ('127.0.0.1', 51822) queue empty
  sending b'in parts.' to ('127.0.0.1', 51823)
waiting for the next event
   ('127.0.0.1', 51823) queue empty
waiting for the next event
  closing ('127.0.0.1', 51823)
waiting for the next event
  closing ('127.0.0.1', 51823)


waiting for the next event
  connection from ('127.0.0.1', 51848)
waiting for the next event
  received b'This is the message. ' from ('127.0.0.1', 51847)
waiting for the next event
  received b'This is the message. ' from ('127.0.0.1', 51848)
  sending b'This is the message. ' to ('127.0.0.1', 51847)
waiting for the next event
   ('127.0.0.1', 51847) queue empty
  sending b'This is the message. ' to ('127.0.0.1', 51848)
waiting for the next event
   ('127.0.0.1', 51848) queue empty
waiting for the next event
  received b'It will be sent ' from ('127.0.0.1', 51847)
waiting for the next event
  received b'It will be sent ' from ('127.0.0.1', 51848)
  sending b'It will be sent ' to ('127.0.0.1', 51847)
waiting for the next event
   ('127.0.0.1', 51847) queue empty
  sending b'It will be sent ' to ('127.0.0.1', 51848)
waiting for the next event
   ('127.0.0.1', 51848) queue empty
waiting for the next event
  received b'in parts.' from ('127.0.0.1', 51847)
  received b'in parts.' from ('127.0.0.1', 51848)
waiting for the next event
  sending b'in parts.' to ('127.0.0.1', 51847)
  sending b'in parts.' to ('127.0.0.1', 51848)
waiting for the next event
   ('127.0.0.1', 51847) queue empty
   ('127.0.0.1', 51848) queue empty
waiting for the next event
  closing ('127.0.0.1', 51848)
waiting for the next event
  closing ('127.0.0.1', 51848)
waiting for the next event

"""