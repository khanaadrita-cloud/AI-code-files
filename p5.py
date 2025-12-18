import tensorflow as tf
from tensorflow.keras import layers, models
import matplotlib.pyplot as plt

# Load and normalize MNIST data
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0  # scale to [0, 1][web:16][web:19]

# Build the model
model = models.Sequential([
    layers.Flatten(input_shape=(28, 28)),
    layers.Dense(128, activation='relu'),
    layers.Dense(128, activation='sigmoid'),
    layers.Dense(10, activation='softmax'),  
    layers.Dense(10, activation='relu') 
])

# Compile the model
model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

# Train the model
model.fit(x_train, y_train, epochs=5)

# Evaluate the model
test_loss, test_acc = model.evaluate(x_test, y_test)
print('Test accuracy:', test_acc)

# Make predictions
predictions = model.predict(x_test)

# Show one test image with prediction
index = 1
plt.imshow(x_test[index], cmap=plt.cm.binary)
pred_label = predictions[index].argmax()
true_label = y_test[index]
plt.title(f'Predicted: {pred_label}, True: {true_label}')  # f-string title[web:12][web:15]
plt.axis('off')
plt.show()
