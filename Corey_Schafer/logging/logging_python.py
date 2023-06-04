"""
Level       When it’s used

DEBUG       Detailed information, typically of interest only when diagnosing problems.

INFO        Confirmation that things are working as expected.

WARNING     An indication that something unexpected happened, or indicative of some problem in the near future (e.g. ‘disk space low’). The software is still working as expected.

ERROR       Due to a more serious problem, the software has not been able to perform some function.

CRITICAL    A serious error, indicating that the program itself may be unable to continue running.
"""

import logging

logging.basicConfig(filename="test.log", encoding='utf-8', level=logging.DEBUG)

def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    return x / y 

num1 = 4
num2 = 20



add_result = add(num1, num2)
logging.debug("add: {} + {} = {}".format(num1, num2, add_result))

sub_result = sub(num1, num2)
logging.debug("sub: {} + {} = {}".format(num1, num2, sub_result))

mul_result = mul(num1, num2)
logging.debug("mul: {} + {} = {}".format(num1, num2, mul_result))

div_result = div(num1, num2)
logging.debug("div: {} + {} = {}".format(num1, num2, div_result))