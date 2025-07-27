import logging

logging.warning("%s before you %s", "Look", "leap!")
var1 = 2
var2 = [1, 2, 3, 4, 5, 6]
var3 = "qwe"
var4 = {"a": "a_v", "b": "b_v"}
logging.warning(var1)
logging.warning(var2)
logging.warning(var3)
logging.warning(var4)

"""
$ python 04_Logging_variable_data.py
WARNING:root:Look before you leap!
WARNING:root:2
WARNING:root:[1, 2, 3, 4, 5, 6]
WARNING:root:qwe
WARNING:root:{'a': 'a_v', 'b': 'b_v'}
$
"""
