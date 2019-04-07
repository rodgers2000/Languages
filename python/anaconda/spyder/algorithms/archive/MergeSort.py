#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 22 12:55:24 2018

@author: Mjr
"""


class MergeSort():

    def __init__(self, A):
        self.A = A

    def merge(self, L, R):
        M = []
        while len(L) + len(R) != 0:
                if len(L) != 0 and len(R) != 0:
                    if (L[0] > R[0]):
                        M.append(R.pop(0))
                    else:
                        M.append(L.pop(0))
                else:
                    if len(L) != 0:
                        M.append(L.pop(0))
                    if len(R) != 0:
                        M.append(R.pop(0))
        return M

    def mergesort(self, A):
        if len(A) == 1:
            return A
        mid_idx = int(len(A) / 2)
        L = A[:mid_idx]
        R = A[mid_idx:]
        L = self.mergesort(L)
        R = self.mergesort(R)
        A = self.merge(L, R)
        return A


mike = MergeSort([3, 2, 5, 4, 10, 50, 1, 7, 69])
print(mike.mergesort(mike.A))
