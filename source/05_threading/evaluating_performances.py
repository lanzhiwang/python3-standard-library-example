from threading import Thread
import multiprocessing


def show_results(func_name, results):
    print("%-23s %4.6f seconds" % (func_name, results))


class process_object(multiprocessing.Process):
    def __init__(self, func):
        multiprocessing.Process.__init__(self)
        self.func = func

    def run(self):
        self.func()


def process(num_process, func):
    funcs = []
    for i in range(int(num_process)):
        funcs.append(process_object(func))
    for i in funcs:
        i.start()
    for i in funcs:
        i.join()


class threads_object(Thread):
    def __init__(
        self, group=None, target=None, name=None, args=(), kwargs=None, *, daemon=None
    ):
        super().__init__(group=group, target=target, name=name, daemon=daemon)
        self.args = args
        self.kwargs = kwargs

    def run(self):
        self.args[0]()


def threaded(num_threads, func):
    funcs = []
    for i in range(int(num_threads)):
        funcs.append(threads_object(args=(func,)))
    for i in funcs:
        i.start()
    for i in funcs:
        i.join()


class non_object(object):
    def __init__(self, func):
        self.func = func

    def run(self):
        self.func()


def non(num_iter, func):
    funcs = []
    for i in range(int(num_iter)):
        funcs.append(non_object(func))
    for i in funcs:
        i.run()


def function_to_run1():
    pass


def function_to_run2():
    a, b = 1, 1
    for _ in range(10000):
        a, b = b, a + b


def function_to_run3():
    from urllib import request

    response = request.urlopen("http://www.baidu.com/")
    response.read(1024)


if __name__ == "__main__":
    import sys
    from timeit import Timer

    repeat = 10
    number = 1
    num = [1, 2, 4, 8]

    for func in [function_to_run1, function_to_run2, function_to_run3]:
        for i in num:
            t = Timer(
                "non(%s, %s)" % (i, func.__name__),
                "from __main__ import non",
                globals=globals(),
            )
            best_result = min(t.repeat(repeat=repeat, number=number))
            show_results("non (%s iters)" % i, best_result)

            t = Timer(
                "threaded(%s, %s)" % (i, func.__name__),
                "from __main__ import threaded",
                globals=globals(),
            )
            best_result = min(t.repeat(repeat=repeat, number=number))
            show_results("threaded (%s threads)" % i, best_result)

            t = Timer(
                "process(%s, %s)" % (i, func.__name__),
                "from __main__ import process",
                globals=globals(),
            )
            best_result = min(t.repeat(repeat=repeat, number=number))
            show_results("process (%s process)" % i, best_result)
        print("Iterations complete")
"""
non (1 iters)           0.000001 seconds
threaded (1 threads)    0.000069 seconds
process (1 process)     0.002885 seconds
non (2 iters)           0.000001 seconds
threaded (2 threads)    0.000115 seconds
process (2 process)     0.003724 seconds
non (4 iters)           0.000002 seconds
threaded (4 threads)    0.000189 seconds
process (4 process)     0.004960 seconds
non (8 iters)           0.000003 seconds
threaded (8 threads)    0.000364 seconds
process (8 process)     0.007469 seconds

"""
