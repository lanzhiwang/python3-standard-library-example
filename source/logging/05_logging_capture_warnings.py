#!/usr/bin/env python3
"""Simple logging to stderr using different levels.
"""

#end_pymotw_header
import logging
import warnings

logging.basicConfig(
    level=logging.INFO,
)

warnings.warn('This warning is not sent to the logs')

logging.captureWarnings(True)

warnings.warn('This warning is sent to the logs')

"""
[root@huzhi-code logging]# python3 05_logging_capture_warnings.py
05_logging_capture_warnings.py:13: UserWarning: This warning is not sent to the logs
  warnings.warn('This warning is not sent to the logs')
WARNING:py.warnings:05_logging_capture_warnings.py:17: UserWarning: This warning is sent to the logs
  warnings.warn('This warning is sent to the logs')

[root@huzhi-code logging]#
"""