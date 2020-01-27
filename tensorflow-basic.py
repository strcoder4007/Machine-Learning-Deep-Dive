import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()


mnist = tf.keras.datasets.mnist # 28x28 images of handwritten digits 0-9

(x_train, y_train), (x_test, y_test) = mnist.load_data()

x_train = tf.keras.utils.normalize(x_train, axis=1)
x_test = tf.keras.utils.normalize(x_test, axis=1)

model = tf.keras.models.Sequential()
model.add = (tf.keras.layers.Flatten())
model.add = (tf.keras.layers.Dense(128, activation=tf.nn.relu))
model.add = (tf.keras.layers.Dense(128, activation=tf.nn.relu))
model.add = (tf.keras.layers.Dense(10, activation=tf.nn.softmax))

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

model.fit(x_train, y_train, epochs=3)

val_loss, val_acc = model.evaluate(x_test, y_test)
print(val_loss, val_acc)


model.save('epic_num_reader.model')
new_model = tf.keras.models.load_model('epic_num_reader.model')

predictions = new_model.predict([x_test])

print(predictions)

import numpy as np
import matplotlib.pyplot as plt

print(np.argmax(predictions[0]))

plt.imshow(x_test[0])
plt.show()