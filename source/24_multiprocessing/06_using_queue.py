#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
"""Spawn a Process – Chapter 3: Process Based Parallelism
"""
#end_pymotw_header
import multiprocessing
import random
import time


class Producer(multiprocessing.Process):
    def __init__(self, queue):
        multiprocessing.Process.__init__(self)
        self.queue = queue

    def run(self) :
        for i in range(10):
            item = random.randint(0, 256)
            self.queue.put(item) 
            print("Process Producer : item %d appended to queue %s" % (item, self.name))
            time.sleep(1)


class Consumer(multiprocessing.Process):
    def __init__(self, queue):
        multiprocessing.Process.__init__(self)
        self.queue = queue

    def run(self):
        while True:
            if self.queue.empty():
                print("the queue is empty")
                break
            else :
                time.sleep(2)
                item = self.queue.get()
                print ('Process Consumer : item %d popped from by %s' % (item, self.name))
                time.sleep(1)


if __name__ == '__main__':
    queue = multiprocessing.Queue()
    process_producer = Producer(queue)
    process_consumer = Consumer(queue)
    process_producer.start()
    process_consumer.start()
    process_producer.join()
    process_consumer.join()

"""
Process Producer : item 240 appended to queue Producer-1
Process Producer : item 7 appended to queue Producer-1
Process Producer : item 68 appended to queue Producer-1
Process Consumer : item 240 popped from by Consumer-2
Process Producer : item 236 appended to queue Producer-1
Process Producer : item 102 appended to queue Producer-1
Process Consumer : item 7 popped from by Consumer-2
Process Producer : item 209 appended to queue Producer-1
Process Producer : item 68 appended to queue Producer-1
Process Producer : item 251 appended to queue Producer-1
Process Consumer : item 68 popped from by Consumer-2
Process Producer : item 149 appended to queue Producer-1
Process Producer : item 164 appended to queue Producer-1
Process Consumer : item 236 popped from by Consumer-2
Process Consumer : item 102 popped from by Consumer-2
Process Consumer : item 209 popped from by Consumer-2
Process Consumer : item 68 popped from by Consumer-2
Process Consumer : item 251 popped from by Consumer-2
Process Consumer : item 149 popped from by Consumer-2
Process Consumer : item 164 popped from by Consumer-2
the queue is empty
"""