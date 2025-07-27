#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2014 Doug Hellmann.  All rights reserved.
"""Dealing with individual background tasks as they finish"""

# end_pymotw_header
import asyncio


async def phase(i):
    print("in phase {}".format(i))
    await asyncio.sleep(0.5 - (0.1 * i))
    print("done with phase {}".format(i))
    return "phase {} result".format(i)


async def main(num_phases):
    print("starting main")
    phases = [phase(i) for i in range(num_phases)]
    print("waiting for phases to complete")
    results = []
    for next_to_complete in asyncio.as_completed(phases):
        answer = await next_to_complete
        print("received answer {!r}".format(answer))
        results.append(answer)
    print("results: {!r}".format(results))
    return results


event_loop = asyncio.get_event_loop()
try:
    event_loop.run_until_complete(main(3))
finally:
    event_loop.close()

"""
starting main
waiting for phases to complete
in phase 2
in phase 1
in phase 0
done with phase 2
received answer 'phase 2 result'
done with phase 1
received answer 'phase 1 result'
done with phase 0
received answer 'phase 0 result'
results: ['phase 2 result', 'phase 1 result', 'phase 0 result']
"""
