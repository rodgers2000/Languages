#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 15:15:33 2019

@author: mrodgers
"""

import tensorflow as tf #analysis:ignore

w = tf.Variable(initial_value=[[1, 2, 3], [4, 5, 6]], name='w', dtype=tf.float32)

x = tf.constant([[10, -20],[30, -100], [200, -300]], dtype=tf.float32)

func = tf.reduce_sum(tf.matmul(x, w))

optimizer = tf.train.GradientDescentOptimizer(learning_rate=.1)
objective = optimizer.minimize(func)

Session = tf.Session()
Session.run(tf.global_variables_initializer())

for iteration in range(10):
    Session.run(objective)
    print('iter', iteration)
    print('w', Session.run(w))
    print('loss', Session.run(func))



