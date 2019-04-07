#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 15 20:16:14 2018

@author: Mjr
"""

import math


class MinBinaryHeap():
    # =============================================================================
    #     this class produces a Min-Binary-Heap that has two main functions.
    # =============================================================================

    def __init__(self):
        self.array = []
        self.temp_min = -1

    def swapIndexs(self, idx1, idx2):
        pt1 = self.array[idx1]
        self.array[idx1] = self.array[idx2]
        self.array[idx2] = pt1

    def getValue(self, idx):
        valid_idx = (idx >= 0 and len(self.array) > idx)
        if valid_idx:
            return self.array[idx]
        else:
            return 1000000

    def insert(self, pt, child_idx=0, flag=1):
        # =============================================================================
        #     this function inserts the value and restructures the tree.
        # =============================================================================
        if flag == 1:
            self.array.append(pt)
            child_idx = len(self.array) - 1

        if child_idx == 0:
            return None

        prt_idx = math.floor(((child_idx - 1)/2))

        if self.getValue(prt_idx) > self.getValue(child_idx):
            self.swapIndexs(prt_idx, child_idx)
            self.insert(pt, child_idx=prt_idx, flag=0)
        else:
            return None

    def extract(self, prt_idx=0, flag=1):
        # =============================================================================
        #     this function restructures the tree and RETURNS the min value.
        # =============================================================================
        if flag == 1:
            self.temp_min = self.array[0]
            self.array[0] = self.array[-1]
            self.array.pop()
            self.extract(prt_idx=0, flag=0)  # start at top of binary tree

        left_child_idx = 2 * prt_idx + 1
        right_child_idx = 2 * prt_idx + 2

        left_child_val = self.getValue(left_child_idx)
        right_child_val = self.getValue(right_child_idx)
        prt_val = self.getValue(prt_idx)

        if right_child_val > left_child_val and prt_val > left_child_val:
            self.swapIndexs(left_child_idx, prt_idx)
            self.extract(left_child_idx, flag=0)

        if left_child_val > right_child_val and prt_val > right_child_val:
            self.swapIndexs(right_child_idx, prt_idx)
            self.extract(right_child_idx, flag=0)

        if left_child_val > prt_val and right_child_val > prt_val:
            return self.temp_min
        # if all else fails!!!
        if prt_val == 1000000:
            return self.temp_min
