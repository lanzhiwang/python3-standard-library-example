#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
""" """

# end_pymotw_header
import mailbox

mbox = mailbox.Maildir("Example")
for message in mbox:
    print(message["subject"])
