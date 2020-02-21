#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2009 Doug Hellmann All rights reserved.
#
"""
"""

#end_pymotw_header
import json


class MyDecoder(json.JSONDecoder):

    def __init__(self):
        json.JSONDecoder.__init__(
            self,
            object_hook=self.dict_to_object,
        )

    def dict_to_object(self, d):
        print('dict_to_object: ', d)
        if '__class__' in d:
            class_name = d.pop('__class__')
            module_name = d.pop('__module__')
            module = __import__(module_name)
            print('MODULE:', module.__name__)
            class_ = getattr(module, class_name)
            print('CLASS:', class_)
            args = {
                key: value
                for key, value in d.items()
            }
            print('INSTANCE ARGS:', args)
            inst = class_(**args)
        else:
            inst = d
        return inst


encoded_object = '''
[{"a": "A", "b": [2, 4], "c": 3.0, "o": {"__class__": "MyObj", "__module__": "json_myobj", "s": "instance value goes here"}}]
'''

myobj_instance = MyDecoder().decode(encoded_object)
print(myobj_instance)

"""
dict_to_object:  {'__class__': 'MyObj', '__module__': 'json_myobj', 's': 'instance value goes here'}
MODULE: json_myobj
CLASS: <class 'json_myobj.MyObj'>
INSTANCE ARGS: {'s': 'instance value goes here'}
dict_to_object:  {'a': 'A', 'b': [2, 4], 'c': 3.0, 'o': <MyObj(instance value goes here)>}
[{'a': 'A', 'b': [2, 4], 'c': 3.0, 'o': <MyObj(instance value goes here)>}]
"""