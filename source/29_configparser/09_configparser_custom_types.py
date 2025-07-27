#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2010 Doug Hellmann.  All rights reserved.
#
""" """

# end_pymotw_header
from configparser import ConfigParser
import datetime


def parse_iso_datetime(s):
    print("parse_iso_datetime({!r})".format(s))
    return datetime.datetime.strptime(s, "%Y-%m-%dT%H:%M:%S.%f")


parser = ConfigParser(
    converters={
        "datetime": parse_iso_datetime,
    }
)
parser.read("custom_types.ini")

string_value = parser["datetimes"]["due_date"]
value = parser.getdatetime("datetimes", "due_date")
print("due_date : {!r} -> {!r}".format(string_value, value))

"""
(venv) huzhi@huzhideMacBook-Pro 29_configparser % python 09_configparser_custom_types.py
parse_iso_datetime('2015-11-08T11:30:05.905898')
due_date : '2015-11-08T11:30:05.905898' -> datetime.datetime(2015, 11, 8, 11, 30, 5, 905898)
(venv) huzhi@huzhideMacBook-Pro 29_configparser %
"""
