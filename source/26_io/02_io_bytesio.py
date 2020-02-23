#!/usr/bin/env python3
"""Simple examples with BytesIO class
"""

#end_pymotw_header
import io

# Writing to a buffer
output = io.BytesIO()
output.write('This goes into the buffer. '.encode('utf-8'))
output.write('ÁÇÊ'.encode('utf-8'))

# Retrieve the value written
print(output.getvalue())

output.close()  # discard buffer memory

# Initialize a read buffer
input = io.BytesIO(b'Inital value for read buffer')

# Read from the buffer
print(input.read())

"""
b'This goes into the buffer. \xc3\x81\xc3\x87\xc3\x8a'
b'Inital value for read buffer'
"""
