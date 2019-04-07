#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 20 16:32:35 2018

@author: Mjr
"""


class Greedy():

    def __init__(self):
        self.jobs = []

    def addData(self, line, heuristic):
        weight = int(line[0])
        length = int(line[1])
        if heuristic == 1:
            this_pt = (weight - length, weight, length)
        if heuristic == 2:
            this_pt = (weight / length, weight, length)

        self.jobs.append(this_pt)

    def sortData(self, heuristic):

        if heuristic == 2:
            self.jobs.sort(key=lambda i: i[0], reverse=True)
        if heuristic == 1:
            self.jobs.sort(key=lambda i: i[0], reverse=True)
            items_sorted = {}
            new_jobs = []
            for job in self.jobs:
                if job[0] not in items_sorted:
                    temp_list = list(filter(lambda x: x[0] == job[0], self.jobs))
                    temp_list.sort(key=lambda i: i[1], reverse=True)
                    items_sorted[job[0]] = 1
                    new_jobs.extend(temp_list)
            self.jobs = new_jobs

    def computeCost(self):
        total, accum = 0, 0
        for job in self.jobs:
            accum += job[2]
            w = job[1]
            total += w * accum

        return total
