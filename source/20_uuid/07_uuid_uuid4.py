#!/usr/bin/env python3
# encoding: utf-8
""" """

# end_pymotw_header
import uuid

for i in range(3):
    u = uuid.uuid4()
    print(u)
    print(u.hex)
    print()


"""
(venv) huzhi@huzhideMacBook-Pro 20_uuid % python 07_uuid_uuid4.py
0c4093cf-ef68-4f7b-bd84-d0232409c178
0c4093cfef684f7bbd84d0232409c178

6959bd9c-f6b0-4cde-92d0-1d6f7dad646a
6959bd9cf6b04cde92d01d6f7dad646a

698aed16-dc4e-4d6d-ad70-295efa0b78be
698aed16dc4e4d6dad70295efa0b78be

(venv) huzhi@huzhideMacBook-Pro 20_uuid %
"""
