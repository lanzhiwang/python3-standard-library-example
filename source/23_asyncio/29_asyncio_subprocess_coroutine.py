#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2014 Doug Hellmann.  All rights reserved.
"""Starting a subprocess using coroutines"""

# end_pymotw_header
import asyncio
import asyncio.subprocess


def _parse_results(output):
    print("parsing results")
    # Output has one row of headers, all single words.  The
    # remaining rows are one per filesystem, with columns more or
    # less matching the headers (assuming that none of the mount
    # points have whitespace in the names).
    if not output:
        return []
    lines = output.splitlines()
    headers = lines[0].split()
    devices = lines[1:]
    results = [dict(zip(headers, line.split())) for line in devices]
    return results


async def run_df():
    print("in run_df")

    buffer = bytearray()

    create = asyncio.create_subprocess_exec(
        "df",
        "-hl",
        stdout=asyncio.subprocess.PIPE,
    )
    print("launching process")
    proc = await create
    print("process started {}".format(proc.pid))

    while True:
        line = await proc.stdout.readline()
        print("read {!r}".format(line))
        if not line:
            print("no more output from command")
            break
        buffer.extend(line)

    print("waiting for process to complete")
    await proc.wait()

    return_code = proc.returncode
    print("return code {}".format(return_code))
    if not return_code:
        cmd_output = bytes(buffer).decode()
        results = _parse_results(cmd_output)
    else:
        results = []

    return (return_code, results)


event_loop = asyncio.get_event_loop()
try:
    return_code, results = event_loop.run_until_complete(run_df())
finally:
    event_loop.close()

if return_code:
    print("error exit {}".format(return_code))
else:
    print("\nFree space:")
    for r in results:
        print("{Mounted:25}: {Avail}".format(**r))

"""
in run_df
launching process
process started 24
read b'Filesystem      Size  Used Avail Use% Mounted on\n'
read b'overlay          59G   44G   12G  80% /\n'
read b'tmpfs            64M     0   64M   0% /dev\n'
read b'shm              64M     0   64M   0% /dev/shm\n'
read b'grpcfuse        932G  167G  765G  18% /python3-standard-library-example\n'
read b'/dev/vda1        59G   44G   12G  80% /etc/hosts\n'
read b'tmpfs           3.9G     0  3.9G   0% /proc/acpi\n'
read b'tmpfs           3.9G     0  3.9G   0% /sys/firmware\n'
read b''
no more output from command
waiting for process to complete
return code 0
parsing results

Free space:
/                        : 12G
/dev                     : 64M
/dev/shm                 : 64M
/python3-standard-library-example: 765G
/etc/hosts               : 12G
/proc/acpi               : 3.9G
/sys/firmware            : 3.9G
"""
