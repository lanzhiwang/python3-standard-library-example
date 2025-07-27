#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
""" """

# end_pymotw_header
import mailbox
import email.utils

from_addr = email.utils.formataddr(("Author", "author@example.com"))
to_addr = email.utils.formataddr(("Recipient", "recipient@example.com"))

payload = """This is the body.
From (will not be escaped).
There are 3 lines.
"""

mbox = mailbox.mbox("example.mbox")
mbox.lock()
try:
    msg = mailbox.mboxMessage()
    msg.set_unixfrom("author Sat Feb  7 01:05:34 2009")
    msg["From"] = from_addr
    msg["To"] = to_addr
    msg["Subject"] = "Sample message 1"
    msg.set_payload(payload)
    mbox.add(msg)
    mbox.flush()

    msg = mailbox.mboxMessage()
    msg.set_unixfrom("author")
    msg["From"] = from_addr
    msg["To"] = to_addr
    msg["Subject"] = "Sample message 2"
    msg.set_payload("This is the second body.\n")
    mbox.add(msg)
    mbox.flush()
finally:
    mbox.unlock()

print(open("example.mbox", "r").read())
