#!/usr/bin/env python3
# encoding: utf-8
""" """

# end_pymotw_header
import uuid

for node in [0x1EC200D9E0, 0x1E5274040E]:
    print(uuid.uuid1(node), hex(node))

"""
(venv) huzhi@huzhideMacBook-Pro 20_uuid % python 04_uuid_uuid1_othermac.py
b9d71782-a3f4-11ea-ae6a-001ec200d9e0 0x1ec200d9e0
b9d876e8-a3f4-11ea-aca7-001e5274040e 0x1e5274040e
(venv) huzhi@huzhideMacBook-Pro 20_uuid %
"""
