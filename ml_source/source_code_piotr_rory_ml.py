import sys
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import keras
from keras import train_images, train_labels, test_images, test_labels
from tensorflow.keras.datasets import cifar10
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, Flatten, MaxPooling2D, Dense, Dropout, BatchNormalization
from tensorflow.keras.optimizers import SGD
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from sklearn.metrics import confusion_matrix, precision_score, recall_score, f1_score
from sklearn.model_selection import train_test_split

"""
## ANN baseline model
- one layer of ten neurons
"""

inputs = keras.Input(shape=train_images.shape[1:])

layer = keras.layers.Flatten()(inputs)

outputs = keras.layers.Dense(10)(layer)

model = keras.Model(inputs=inputs,
                    outputs=outputs,
                    name="ann_baseline_onelayer")

model.summary()

loss_fn = keras.losses.SparseCategoricalCrossentropy(from_logits=True)

model.compile(optimizer='sgd',
              loss=loss_fn,
              metrics=['accuracy'])

training = model.fit(train_images,
                    train_labels,
                    epochs=10,
                    validation_data=(test_images, test_labels))

training_data = pd.DataFrame.from_dict(training.history)
sns.lineplot(data = training_data[['accuracy', 'val_accuracy']])



"""## ANN baseline model three
- layer one: 25 neurons
- layer two: 25 neurons
- layer three: ten neurons

"""

inputs = keras.Input(shape=train_images.shape[1:])

layer = keras.layers.Flatten()(inputs)

layer = keras.layers.Dense(100)(layer)

layer = keras.layers.Dense(50)(layer)

outputs = keras.layers.Dense(10)(layer)

model = keras.Model(inputs=inputs,
                    outputs=outputs,
                    name="ann_baseline_twolayer")

model.summary()

loss_fn = keras.losses.SparseCategoricalCrossentropy(from_logits=True)

model.compile(optimizer='sgd',
              loss=loss_fn,
              metrics=['accuracy'])

training = model.fit(train_images,
                    train_labels,
                    epochs=10,
                    validation_data=(test_images, test_labels))

training_data = pd.DataFrame.from_dict(training.history)
sns.lineplot(data = training_data[['accuracy', 'val_accuracy']])



"""## CNN model one

- conv layers = 1
- filters = 50
- filter kernel = (3,3)
- stride = 1
- activation = relu
- pooling = none
- dense = 10 (10 output classes)
- optimizer  = adam
- metric = accuracy
"""

inputs = keras.Input(shape=train_images.shape[1:])

layer = keras.layers.Conv2D(filters=50,
                        kernel_size=(3, 3),
                        strides=1,
                        padding="same",
                        activation='relu')(inputs)

layer = keras.layers.Flatten()(layer)

outputs = keras.layers.Dense(10)(layer)

model = keras.Model(inputs=inputs, outputs=outputs, name="cnn_one")

loss_fn = keras.losses.SparseCategoricalCrossentropy(from_logits=True)

model.compile(optimizer='adam',
              loss=loss_fn,
              metrics=['accuracy'])

model.summary()

training = model.fit(train_images,
                    train_labels,
                    epochs=10,
                    validation_data=(test_images, test_labels))

training_data = pd.DataFrame.from_dict(training.history)
sns.lineplot(data=training_data[['accuracy', 'val_accuracy']])

for layer in model.layers:
 # check for convolutional layer
 if 'conv' not in layer.name:
  continue
 # get filter weights
 filters, biases = layer.get_weights()
 print(layer.name, filters.shape)

"""### Plot the filters"""

filters, biases = model.layers[1].get_weights()

# normalize filter values to 0-1
f_min, f_max = filters.min(), filters.max()
filters = (filters - f_min) / (f_max - f_min)

ix=1
for i in range(6):
  # plot the first 6 filters
 f = filters[:, :, :, i]
 # plot each channel
 for j in range(3):
 # specify subplot and turn of axis
      ax = plt.subplot(6, 3, ix)
      ax.set_xticks([])
      ax.set_yticks([])
      # plot filter channel in grayscale
      plt.imshow(f[:, :, j], cmap='gray')
      ix += 1
# show the figure
plt.show()

"""### Plot the feature maps"""

model = keras.models.Model(inputs=model.inputs, outputs=model.layers[1].output)
model.summary()

test_image = test_images[0]

plt.imshow(test_image)

img = np.expand_dims(test_image, axis=0)

feature_maps = model.predict(img)

feature_maps.shape

square = 7
ix = 1
for _ in range(square):
  for _ in range(square):
    ax = plt.subplot(square, square, ix)
    ax.set_xticks([])
    ax.set_yticks([])
    plt.imshow(feature_maps[0, :, :, ix-1], cmap='gray')
    ix += 1

plt.show()



"""## CNN model four

- conv layers = 3
- filters = 25,50,100
- filter kernel = (3,3)
- stride = 1
- activation = relu
- pooling = maxpooling (2,2) after each conv
- dense = 25,10 (10 output classes)
- optimizer  = adam
- metric = accuracy
"""

inputs = keras.Input(shape=train_images.shape[1:])

layer = keras.layers.Conv2D(filters=50,
                        kernel_size=(3, 3),
                        strides=1,
                        padding="same",
                        activation='relu')(inputs)

layer = keras.layers.MaxPooling2D((2, 2))(layer)

layer = keras.layers.Conv2D(filters=100,
                        kernel_size=(3, 3),
                        strides=1,
                        padding="same",
                        activation='relu')(layer)

layer = keras.layers.MaxPooling2D((2, 2))(layer)

layer = keras.layers.Conv2D(filters=200,
                        kernel_size=(3, 3),
                        strides=1,
                        padding="same",
                        activation='relu')(layer)

layer = keras.layers.MaxPooling2D((2, 2))(layer)

layer = keras.layers.Flatten()(layer)

layer = keras.layers.Dense(40)(layer)

layer = keras.layers.Dense(40)(layer)

outputs = keras.layers.Dense(10)(layer)

model = keras.Model(inputs=inputs, outputs=outputs, name="cnn_four")

loss_fn = keras.losses.SparseCategoricalCrossentropy(from_logits=True)

model.compile(optimizer='adam',
              loss=loss_fn,
              metrics=['accuracy'])

model.summary()

training = model.fit(train_images,
                    train_labels,
                    epochs=10,
                    validation_data=(test_images, test_labels))

training_data = pd.DataFrame.from_dict(training.history)
sns.lineplot(data=training_data[['accuracy', 'val_accuracy']])

"""### Plot the feature maps"""

# model.layers[2] is the second Conv2D layer
model_layer = keras.models.Model(inputs=model.inputs, outputs=model.layers[1].output)
model_layer.summary()

test_image = test_images[0]
img = np.expand_dims(test_image, axis=0)

feature_maps = model_layer.predict(img)

square = 4

ax = plt.subplot(square, square, 1)
ax.set_xticks([])
ax.set_yticks([])
plt.imshow(test_image)

ix = 2
for _ in range(square):
  for _ in range(square-1):
    ax = plt.subplot(square, square, ix)
    ax.set_xticks([])
    ax.set_yticks([])
    plt.imshow(feature_maps[0, :, :, ix-1], cmap='gray')
    ix += 1

plt.show()

# model.layers[2] is the first max pooling
model_layer = keras.models.Model(inputs=model.inputs, outputs=model.layers[2].output)
model_layer.summary()

test_image = test_images[0]
img = np.expand_dims(test_image, axis=0)

feature_maps = model_layer.predict(img)

square = 4

ax = plt.subplot(square, square, 1)
ax.set_xticks([])
ax.set_yticks([])
plt.imshow(test_image)

ix = 2
for _ in range(square):
  for _ in range(square-1):
    ax = plt.subplot(square, square, ix)
    ax.set_xticks([])
    ax.set_yticks([])
    plt.imshow(feature_maps[0, :, :, ix-1], cmap='gray')
    ix += 1

plt.show()

# model.layers[3] is the second conv
model_layer = keras.models.Model(inputs=model.inputs, outputs=model.layers[3].output)
model_layer.summary()

test_image = test_images[0]
img = np.expand_dims(test_image, axis=0)

feature_maps = model_layer.predict(img)

square = 4

ax = plt.subplot(square, square, 1)
ax.set_xticks([])
ax.set_yticks([])
plt.imshow(test_image)

ix = 2
for _ in range(square):
  for _ in range(square-1):
    ax = plt.subplot(square, square, ix)
    ax.set_xticks([])
    ax.set_yticks([])
    plt.imshow(feature_maps[0, :, :, ix-1], cmap='gray')
    ix += 1

plt.show()

# model.layers[4] is the second max pooling
model_layer = keras.models.Model(inputs=model.inputs, outputs=model.layers[4].output)
model_layer.summary()

test_image = test_images[0]
img = np.expand_dims(test_image, axis=0)

feature_maps = model_layer.predict(img)

square = 4

ax = plt.subplot(square, square, 1)
ax.set_xticks([])
ax.set_yticks([])
plt.imshow(test_image)

ix = 2
for _ in range(square):
  for _ in range(square-1):
    ax = plt.subplot(square, square, ix)
    ax.set_xticks([])
    ax.set_yticks([])
    plt.imshow(feature_maps[0, :, :, ix-1], cmap='gray')
    ix += 1

plt.show()

# model.layers[5] is the third conv
model_layer = keras.models.Model(inputs=model.inputs, outputs=model.layers[5].output)
model_layer.summary()

test_image = test_images[0]
img = np.expand_dims(test_image, axis=0)

feature_maps = model_layer.predict(img)

square = 4

ax = plt.subplot(square, square, 1)
ax.set_xticks([])
ax.set_yticks([])
plt.imshow(test_image)

ix = 2
for _ in range(square):
  for _ in range(square-1):
    ax = plt.subplot(square, square, ix)
    ax.set_xticks([])
    ax.set_yticks([])
    plt.imshow(feature_maps[0, :, :, ix-1], cmap='gray')
    ix += 1

plt.show()

# model.layers[6] is the third maxpooling
model_layer = keras.models.Model(inputs=model.inputs, outputs=model.layers[6].output)
model_layer.summary()

test_image = test_images[0]
img = np.expand_dims(test_image, axis=0)

feature_maps = model_layer.predict(img)

square = 4

ax = plt.subplot(square, square, 1)
ax.set_xticks([])
ax.set_yticks([])
plt.imshow(test_image)

ix = 2
for _ in range(square):
  for _ in range(square-1):
    ax = plt.subplot(square, square, ix)
    ax.set_xticks([])
    ax.set_yticks([])
    plt.imshow(feature_maps[0, :, :, ix-1], cmap='gray')
    ix += 1

plt.show()



"""## CNN model seven"""

inputs = keras.Input(shape=train_images.shape[1:])

layer = keras.layers.Conv2D(filters=50,
                        kernel_size=(3, 3),
                        strides=1,
                        padding="same",
                        activation='relu')(inputs)

layer = keras.layers.MaxPooling2D((2, 2))(layer)

layer = keras.layers.Conv2D(filters=100,
                        kernel_size=(3, 3),
                        strides=1,
                        padding="same",
                        activation='relu')(layer)

layer = keras.layers.MaxPooling2D((2, 2))(layer)

layer = keras.layers.Conv2D(filters=200,
                        kernel_size=(3, 3),
                        strides=1,
                        padding="same",
                        activation='relu')(layer)

layer = keras.layers.Conv2D(filters=200,
                        kernel_size=(3, 3),
                        strides=1,
                        padding="same",
                        activation='relu')(layer)

layer = keras.layers.Conv2D(filters=100,
                        kernel_size=(3, 3),
                        strides=1,
                        padding="same",
                        activation='relu')(layer)

layer = keras.layers.MaxPooling2D((2, 2))(layer)

layer = keras.layers.Flatten()(layer)

layer = keras.layers.Dropout(0.3)(layer)

layer = keras.layers.Dense(40)(layer)

layer = keras.layers.Dense(40)(layer)

outputs = keras.layers.Dense(10)(layer)

model = keras.Model(inputs=inputs, outputs=outputs, name="cnn_seven")

loss_fn = keras.losses.SparseCategoricalCrossentropy(from_logits=True)

optimizer = keras.optimizers.Adam(learning_rate=0.001)

model.compile(optimizer=optimizer,
              loss=loss_fn,
              metrics=['accuracy'])

model.summary()

training = model.fit(train_images,
                    train_labels,
                    epochs=8,
                    validation_data=(test_images, test_labels))

training_data = pd.DataFrame.from_dict(training.history)
sns.lineplot(data=training_data[['accuracy', 'val_accuracy']])

"""## CNN final model"""

# Load train and test dataset
def load_dataset():
  # Load dataset
  (trainX, trainY), (testX, testY) = cifar10.load_data()
  # Split train data into train and validation sets
  trainX, valX, trainY, valY = train_test_split(trainX, trainY, test_size=0.15, random_state=42)
  # One hot encode/final_model.h5 target values
  trainY = to_categorical(trainY)
  valY = to_categorical(valY)
  testY = to_categorical(testY)
  return trainX, trainY, valX, valY, testX, testY

# Scale pixels
def normalisation_of_pixels(train, val, test):
    # Convert from integers to floats
    train_norm = train.astype('float32')
    val_norm = val.astype('float32')
    test_norm = test.astype('float32')
    # Normalize to range 0-1
    train_norm = train_norm / 255.0
    val_norm = val_norm / 255.0
    test_norm = test_norm / 255.0
    # Return normalized images
    return train_norm, val_norm, test_norm

# define cnn model
def define_model():
    model = Sequential()
    model.add(Conv2D(32, (3, 3), activation='relu', kernel_initializer='he_uniform', padding='same', input_shape=(32, 32, 3)))
    model.add(BatchNormalization())
    model.add(Conv2D(32, (3, 3), activation='relu', kernel_initializer='he_uniform', padding='same'))
    model.add(BatchNormalization())
    model.add(MaxPooling2D((2, 2)))
    model.add(Dropout(0.2))
    model.add(Conv2D(64, (3, 3), activation='relu', kernel_initializer='he_uniform', padding='same'))
    model.add(BatchNormalization())
    model.add(Conv2D(64, (3, 3), activation='relu', kernel_initializer='he_uniform', padding='same'))
    model.add(BatchNormalization())
    model.add(MaxPooling2D((2, 2)))
    model.add(Dropout(0.3))
    model.add(Conv2D(128, (3, 3), activation='relu', kernel_initializer='he_uniform', padding='same'))
    model.add(BatchNormalization())
    model.add(Conv2D(128, (3, 3), activation='relu', kernel_initializer='he_uniform', padding='same'))
    model.add(BatchNormalization())
    model.add(MaxPooling2D((2, 2)))
    model.add(Dropout(0.4))
    model.add(Flatten())
    model.add(Dense(128, activation='relu', kernel_initializer='he_uniform'))
    model.add(BatchNormalization())
    model.add(Dropout(0.5))
    model.add(Dense(10, activation='softmax'))
    # compile model
    opt = SGD(learning_rate=0.001, momentum=0.9)
    model.compile(optimizer=opt, loss='categorical_crossentropy', metrics=['accuracy'])
    return model

# Plot diagnostic learning curves
def summarize_diagnostics(history):
    # Plot loss
    plt.subplot(211)
    plt.title('Cross Entropy Loss')
    plt.plot(history.history['loss'], color='blue', label='train')
    plt.plot(history.history['val_loss'], color='orange', label='val')
    # Plot accuracy
    plt.subplot(212)
    plt.title('Classification Accuracy')
    plt.plot(history.history['accuracy'], color='blue', label='train')
    plt.plot(history.history['val_accuracy'], color='orange', label='val')
    # Save plot to file
    filename = sys.argv[0].split('/')[-1]
    plt.savefig(filename + '_plot.png')
    plt.close()

# performance metrics
def performance_metrics(testY, predY):
    predY_classes = predY.argmax(1)
    testY_classes = testY.argmax(1)
    precision = precision_score(testY_classes, predY_classes, average='weighted')
    recall = recall_score(testY_classes, predY_classes, average='weighted')
    f1 = f1_score(testY_classes, predY_classes, average='weighted')
    # Visualize performance metrics using bar chart
    metrics = ['Precision', 'Recall', 'F1 Score']
    values = [precision, recall, f1]
    plt.figure(figsize=(10,5))
    bars = plt.bar(metrics, values, color=['purple', 'green', 'blue'])
    plt.ylabel("Score")
    plt.ylim([0.0, 1.0])
    plt.title('Performance Metrics')
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2.0, yval, round(yval, 2), va='bottom') # va: vertical alignment y positional argument
    plt.show()
    return precision, recall, f1

# Plot and return confusion matrix
def plot_confusion_matrix(testY, predY):
    predY_classes = predY.argmax(1)
    testY_classes = testY.argmax(1)
    cm = confusion_matrix(testY_classes, predY_classes)
    fig, ax = plt.subplots(figsize=(10,10))
    sns.heatmap(cm, annot=True, fmt='d', ax=ax, cmap=plt.cm.Blues,
                cbar=False)
    plt.xlabel('Predicted')
    plt.ylabel('Actual')
    plt.title('Confusion Matrix')
    plt.show()
    return cm

def plot_performance(history):
    plt.figure(figsize=(14, 5))
    plt.subplot(1, 2, 1)
    plt.plot(history.history['accuracy'], label='Training Accuracy')
    plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
    plt.xlabel('Epochs')
    plt.ylabel('Accuracy')
    plt.legend()

    plt.subplot(1, 2, 2)
    plt.plot(history.history['loss'], label='Training Loss')
    plt.plot(history.history['val_loss'], label='Validation Loss')
    plt.xlabel('Epochs')
    plt.ylabel('Loss')
    plt.legend()
    plt.show()

trainX, trainY, valX, valY, testX, testY = load_dataset()

trainX, valX, testX = normalisation_of_pixels(trainX, valX, testX)

model = define_model()

datagen = ImageDataGenerator(width_shift_range=0.1, height_shift_range=0.1, horizontal_flip=True)

it_train = datagen.flow(trainX, trainY, batch_size=64)

steps = int(trainX.shape[0] / 64)
history = model.fit(it_train, steps_per_epoch=steps, epochs=400, validation_data=(valX, valY), verbose=0)

_, acc = model.evaluate(testX, testY, verbose=0)
print('> Test accuracy: %.3f' % (acc * 100.0))
# evaluate model on the validation set
_, val_acc = model.evaluate(valX, valY, verbose=0)
print('> Validation accuracy: %.3f' % (val_acc * 100.0))

predY = model.predict(testX)

summarize_diagnostics(history)

performance_metrics(testY, predY)

plot_confusion_matrix(testY, predY)

plot_performance(history)

model.save('most_recent_model.h5')