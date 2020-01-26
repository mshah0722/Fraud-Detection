import tensorflow.compat.v1 as tf
import numpy as np

tf.disable_v2_behavior()

𝒷 = tf.Variable([.3], tf.float32)
𝓌 = tf.Variable([-.3], tf.float32)

x =  tf.placeholder(tf.float32)
y =  tf.placeholder(tf.float32)

x_data = [79.5389363074,79.5381323935,79.527194372,79.527194372,79.5389363074,79.5389363074]
y_data = [3.73,2.93,4.42,1.51,7.66,4.34]

learning_rate = 0.003
model = (𝓌 * 𝓌 * x) + 𝒷
delta = tf.square(model - y)
loss = tf.reduce_sum(delta)
optimizer = tf.train.AdamOptimizer(learning_rate).minimize(loss)
init = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)

    for i in range(10000):
        feed_dict_batch = {x: x_data, y: y_data}
        sess.run(optimizer, feed_dict = feed_dict_batch)

    approx_w, approx_b = sess.run([𝓌, 𝒷])
    print("𝓌 ≈", approx_w, "and 𝒷 ≈", approx_b)