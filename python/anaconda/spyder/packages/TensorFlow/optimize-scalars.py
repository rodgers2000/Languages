import tensorflow as tf

x = tf.Variable(10, name='x', dtype=tf.float32)
y = tf.Variable(20, name='y', dtype=tf.float32)

z = tf.add(tf.add(tf.add(tf.pow(x, 2), x), y), tf.pow(y, 2))

optimizer = tf.train.GradientDescentOptimizer(learning_rate=.1)
objective = optimizer.minimize(z)

init = tf.global_variables_initializer()


with tf.Session() as Session:
    Session.run(init)
    print("x:", Session.run(x))
    print("y:", Session.run(x))
    print("z:", Session.run(z))
    for iteration in range(10):
        Session.run(objective)
        print("iter", iteration)
        print("x:", Session.run(x))
        print("y:", Session.run(x))
        print("z:", Session.run(z))
