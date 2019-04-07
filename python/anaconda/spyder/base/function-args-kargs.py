#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 15 11:36:27 2018

@author: Mjr
"""


# =============================================================================
# def print_args(*args):
#     for arg in args:
#         print(arg)
#
#
# print_args(1, 2, 3, 4)
#
#
# def print_kwargs(**kwargs):
#     for k, v in kwargs.items():
#         print("%s: %s" % (k, v))
#
#
# print_kwargs(one=1, two=2, three=3, four=4)
#
# my_list = [1, 2, 3, 4]
# print_args(*my_list)
#
# my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4}
# print_kwargs(**my_dict)
# =============================================================================


def test_function(**kwargs):
    print('my name is %s %s' % (kwargs['first'], kwargs['last']))
    d1 = kwargs['d1']
    d2 = kwargs['d2']
    print('the sum of %s and %s is %s' % (d1, d2, d1 + d2))


my_params = {'first': 'mike',
             'last': 'rodgers',
             'd1': 5,
             'd2': 2}
test_function(**my_params)
