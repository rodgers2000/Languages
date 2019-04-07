import tensorflow as tf
import numpy as np

w = tf.Variable(initial_value=[[1], [2], [3]], name='w', dtype=tf.float32)
# x = tf.constant([[10, -20, 30], [-100, 200, -300]], dtype=tf.float32)
x = tf.placeholder(tf.float32, shape=[2, 3], name='x')
func = tf.reduce_sum(tf.matmul(x, w))

optimizer = tf.train.GradientDescentOptimizer(learning_rate=.1)
objective = optimizer.minimize(func)

Session = tf.Session()
Session.run(tf.global_variables_initializer())
print("w:", Session.run(w))
for iteration in range(10):
    x_data = np.random.normal(0, 1, size=6).reshape((2, 3))
    Session.run(objective, feed_dict={x: x_data})
    print("iter", iteration)
    print("w:", Session.run(w))
    print("func:", Session.run(func, feed_dict={x: x_data}))

Session.close()
