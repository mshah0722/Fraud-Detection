# import tensorflow as tf
import tensorflow.compat.v1 as tf
import numpy as np

tf.disable_v2_behavior()
print (tf.__version__)

b = tf.Variable([.3], tf.float32)
w = tf.Variable([-.3], tf.float32)

x = tf.placeholder(tf.float32)
y = tf.placeholder(tf.float32)

x_data = [4.0, 0.0, 12.0]
y_data = [5.0, 9, -3]

learning_rate = 0.001

model = w*x+b
delta = tf.square(model - y)
loss = tf.reduce_sum(delta)
optimizer = tf.train.GradientDescentOptimizer(learning_rate).minimize(loss)
init = tf.global_variables_initializer()

with tf.Session() as sess:
  sess.run(init)

  for i in range(10000):
    feed_dict_batch = {x: x_data, y: y_data}
    sess.run(optimizer, feed_dict = feed_dict_batch)
  
  approx_w, approx_b = sess.run([w,b])
  print ("w =", approx_w, "and b =", approx_b)