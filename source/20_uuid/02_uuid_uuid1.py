#!/usr/bin/env python3
# encoding: utf-8
"""
"""

#end_pymotw_header
import uuid

u = uuid.uuid1()

print(u)
print(type(u))
print('bytes   :', repr(u.bytes))
print('hex     :', u.hex)
print('int     :', u.int)
print('urn     :', u.urn)
print('variant :', u.variant)
print('version :', u.version)
print('fields  :', u.fields)
print('  time_low            : ', u.time_low)
print('  time_mid            : ', u.time_mid)
print('  time_hi_version     : ', u.time_hi_version)
print('  clock_seq_hi_variant: ', u.clock_seq_hi_variant)
print('  clock_seq_low       : ', u.clock_seq_low)
print('  node                : ', u.node)
print('  time                : ', u.time)
print('  clock_seq           : ', u.clock_seq)

"""
(venv) huzhi@huzhideMacBook-Pro 20_uuid % python 02_uuid_uuid1.py
0520129e-a3f4-11ea-b2ab-acde48001122
<class 'uuid.UUID'>
bytes   : b'\x05 \x12\x9e\xa3\xf4\x11\xea\xb2\xab\xac\xdeH\x00\x11"'
hex     : 0520129ea3f411eab2abacde48001122
int     : 6812671130561355942973093797634773282
urn     : urn:uuid:0520129e-a3f4-11ea-b2ab-acde48001122
variant : specified in RFC 4122
version : 1
fields  : (85987998, 41972, 4586, 178, 171, 190070690681122)
  time_low            :  85987998
  time_mid            :  41972
  time_hi_version     :  4586
  clock_seq_hi_variant:  178
  clock_seq_low       :  171
  node                :  190070690681122
  time                :  138103007041557150
  clock_seq           :  12971
(venv) huzhi@huzhideMacBook-Pro 20_uuid %
(venv) huzhi@huzhideMacBook-Pro 20_uuid % python 02_uuid_uuid1.py
09baf396-a3f4-11ea-87a6-acde48001122
<class 'uuid.UUID'>
bytes   : b'\t\xba\xf3\x96\xa3\xf4\x11\xea\x87\xa6\xac\xdeH\x00\x11"'
hex     : 09baf396a3f411ea87a6acde48001122
int     : 12933759738250904398012821938129342754
urn     : urn:uuid:09baf396-a3f4-11ea-87a6-acde48001122
variant : specified in RFC 4122
version : 1
fields  : (163246998, 41972, 4586, 135, 166, 190070690681122)
  time_low            :  163246998
  time_mid            :  41972
  time_hi_version     :  4586
  clock_seq_hi_variant:  135
  clock_seq_low       :  166
  node                :  190070690681122
  time                :  138103007118816150
  clock_seq           :  1958
(venv) huzhi@huzhideMacBook-Pro 20_uuid %
"""