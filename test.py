# The usage of tf.dynamic_partition() and tf.dynamic_stitch().
# Kind of tricky if we use it under the batch settings. Should be reshape to 1-D.
import tensorflow as tf

x=tf.reshape(tf.constant([[0.1, -1., 5.2, 4.3, -1., 7.4],[-1,1,2,3,4,-1]]), (-1,))
condition_mask=tf.not_equal(x,tf.constant(-1.))
partitioned_data = tf.dynamic_partition(
    x, tf.cast(condition_mask, tf.int32) , 2)
# partitioned_data[0] = tf.reshape(partitioned_data[0], (2,-1))
# partitioned_data[1] = tf.reshape(partitioned_data[1], (2,-1))

# partitioned_data[1] = partitioned_data[1] + 1.0
condition_indices = tf.dynamic_partition(
   tf.range(tf.shape(x)[0]) , tf.cast(condition_mask, tf.int32) , 2)
# condition_indices[0] = tf.reshape(condition_indices[0], (2,-1))
# condition_indices[1] = tf.reshape(condition_indices[1], (2,-1))

x = tf.dynamic_stitch(condition_indices, partitioned_data)

with tf.Session() as sess:
	print(sess.run(x))