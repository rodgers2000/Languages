#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  3 15:18:21 2018

@author: Mjr
"""

def create_map_inside_map(init_map, keys, values):
        
    if len(values) == 1:
        hold_me = []
        for i in range(len(keys)):
            hold_me.append(values[0])
        values = hold_me
        
    if init_map.keys() != []:
        for key1 in init_map.keys():
            ind_val = 0
            for key2 in keys:
                    init_map[key1][key2] = values[ind_val]
                    ind_val += 1
    else:
        ind_val = 0
        for key2 in keys:
                init_map[key2] = values[ind_val]
                ind_val += 1
    return init_map

one = create_map_inside_map({}, [1, 2, 3], [{}])
two = create_map_inside_map(one, ['a', 'b', 'c'], ['the', 'beast', 'man'])
print two
