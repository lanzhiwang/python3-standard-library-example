#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2010 Doug Hellmann.  All rights reserved.
#
"""Splitting input based on a pattern.
"""

#end_pymotw_header
import re

'''Paragraph one
on two lines.

Paragraph two.


Paragraph three.'''



text = '''Paragraph one\non two lines.\n\nParagraph two.\n\n\nParagraph three.'''

print('With split:')
for num, para in enumerate(re.split(r'(\n{2,})', text)):
    print(num, repr(para))
    print()

print(re.split(r'(\n{2,})', text))
print(type(re.split(r'(\n{2,})', text)))
"""
With split:
0 'Paragraph one\non two lines.'

1 '\n\n'

2 'Paragraph two.'

3 '\n\n\n'

4 'Paragraph three.'


['Paragraph one\non two lines.', '\n\n', 'Paragraph two.', '\n\n\n', 'Paragraph three.']
<class 'list'>
"""
