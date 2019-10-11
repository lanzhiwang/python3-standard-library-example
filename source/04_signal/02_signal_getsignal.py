#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
"""
"""


#end_pymotw_header
import signal


def alarm_received(n, stack):
    return


signal.signal(signal.SIGALRM, alarm_received)

signals_to_names = { getattr(signal, n): n for n in dir(signal) if n.startswith('SIG') and '_' not in n }
print(signals_to_names)

for s, name in sorted(signals_to_names.items()):
    handler = signal.getsignal(s)
    if handler is signal.SIG_DFL:
        handler = 'SIG_DFL'
    elif handler is signal.SIG_IGN:
        handler = 'SIG_IGN'
    print('{:<10} ({:2d}):'.format(name, s), handler)

"""
{1: 'SIGHUP', 2: 'SIGINT', 3: 'SIGQUIT', 4: 'SIGILL', 5: 'SIGTRAP', 6: 'SIGIOT', 7: 'SIGBUS', 
8: 'SIGFPE', 9: 'SIGKILL', 10: 'SIGUSR1', 11: 'SIGSEGV', 12: 'SIGUSR2', 13: 'SIGPIPE', 14: 'SIGALRM', 
15: 'SIGTERM', 17: 'SIGCLD', 18: 'SIGCONT', 19: 'SIGSTOP', 20: 'SIGTSTP', 21: 'SIGTTIN', 22: 'SIGTTOU', 
23: 'SIGURG', 24: 'SIGXCPU', 25: 'SIGXFSZ', 26: 'SIGVTALRM', 27: 'SIGPROF', 28: 'SIGWINCH', 
29: 'SIGPOLL', 30: 'SIGPWR', 31: 'SIGSYS', 34: 'SIGRTMIN', 64: 'SIGRTMAX'}
('SIGHUP     ( 1):', 'SIG_DFL')
('SIGINT     ( 2):', <built-in function default_int_handler>)
('SIGQUIT    ( 3):', 'SIG_DFL')
('SIGILL     ( 4):', 'SIG_DFL')
('SIGTRAP    ( 5):', 'SIG_DFL')
('SIGIOT     ( 6):', 'SIG_DFL')
('SIGBUS     ( 7):', 'SIG_DFL')
('SIGFPE     ( 8):', 'SIG_DFL')
('SIGKILL    ( 9):', 'SIG_DFL')
('SIGUSR1    (10):', 'SIG_DFL')
('SIGSEGV    (11):', 'SIG_DFL')
('SIGUSR2    (12):', 'SIG_DFL')
('SIGPIPE    (13):', 'SIG_IGN')
('SIGALRM    (14):', <function alarm_received at 0x7f8dcc1d3578>)
('SIGTERM    (15):', 'SIG_DFL')
('SIGCLD     (17):', 'SIG_DFL')
('SIGCONT    (18):', 'SIG_DFL')
('SIGSTOP    (19):', 'SIG_DFL')
('SIGTSTP    (20):', 'SIG_DFL')
('SIGTTIN    (21):', 'SIG_DFL')
('SIGTTOU    (22):', 'SIG_DFL')
('SIGURG     (23):', 'SIG_DFL')
('SIGXCPU    (24):', 'SIG_DFL')
('SIGXFSZ    (25):', 'SIG_IGN')
('SIGVTALRM  (26):', 'SIG_DFL')
('SIGPROF    (27):', 'SIG_DFL')
('SIGWINCH   (28):', 'SIG_DFL')
('SIGPOLL    (29):', 'SIG_DFL')
('SIGPWR     (30):', 'SIG_DFL')
('SIGSYS     (31):', 'SIG_DFL')
('SIGRTMIN   (34):', 'SIG_DFL')
('SIGRTMAX   (64):', 'SIG_DFL')
"""