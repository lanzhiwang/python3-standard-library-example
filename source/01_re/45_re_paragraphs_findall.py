#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2010 Doug Hellmann.  All rights reserved.
#
"""Splitting input based on a pattern.
"""

#end_pymotw_header
import re

text = '''Paragraph one\non two lines.\n\nParagraph two.\n\n\nParagraph three.'''

for num, para in enumerate(re.findall(r'(.+?)\n{2,}',
                                      text,
                                      flags=re.DOTALL)
                           ):
    print(num, repr(para))
    print()


print(re.findall(r'(.+?)\n{2,}', text, flags=re.DOTALL))
print(type(re.findall(r'(.+?)\n{2,}', text, flags=re.DOTALL)))

print(re.findall(r'(.+?)(\n{2,})', text, flags=re.DOTALL))

print(re.findall(r'.+?\n{2,}', text, flags=re.DOTALL))
"""
0 'Paragraph one\non two lines.'

1 'Paragraph two.'

['Paragraph one\non two lines.', 'Paragraph two.']
<class 'list'>

[('Paragraph one\non two lines.', '\n\n'), ('Paragraph two.', '\n\n\n')]

['Paragraph one\non two lines.\n\n', 'Paragraph two.\n\n\n']
"""
