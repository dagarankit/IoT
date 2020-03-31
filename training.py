from examples.livenessnet import LivenessNet
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from keras.preprocessing.image import ImageDataGenerator
from keras.optimizers import Adam
from keras.utils import np_utils
from imutils import paths
import matplotlib.pyplot as plotfig
import numpy as np
import argparse
import pickle
import cv2
import os
import matplotlib
matplotlib.use("Agg")

ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dataset", required=True,
	help="path to input dataset")
ap.add_argument("-m", "--model", type=str, required=True,
	help="path to trained model")
ap.add_argument("-l", "--le", type=str, required=True,
	help="path to label encoder")
ap.add_argument("-p", "--plot", type=str, default="newgraphtest.png",
	help="path to output loss/accuracy plot")
args = vars(ap.parse_args())

# we can pass script parameters using Edit Configuration where we can add script path and its parameters


INIT_LR = 1e-4
BS = 8
EPOCHS = 50

print("[INFO] loading images...")
imagePaths = list(paths.list_images(args["dataset"]))
data = []
labels = []

for imagePath in imagePaths:
	label = imagePath.split(os.path.sep)[-2]
	image = cv2.imread(imagePath)
	image = cv2.resize(image, (32, 32))

	data.append(image)
	labels.append(label)

data = np.array(data, dtype="float") / 255.0

le = LabelEncoder()
labels = le.fit_transform(labels)
labels = np_utils.to_categorical(labels, 3)

(trainX, testX, trainY, testY) = train_test_split(data, labels,
	test_size=0.25, random_state=42)

aug = ImageDataGenerator(rotation_range=20, zoom_range=0.15,
	width_shift_range=0.2, height_shift_range=0.2, shear_range=0.15,
	horizontal_flip=True, fill_mode="nearest")

print("[INFO] compiling model...")
opt = Adam(lr=INIT_LR, decay=INIT_LR / EPOCHS)
model = LivenessNet.build(width=32, height=32, depth=3,
	classes=len(le.classes_))
model.compile(loss="binary_crossentropy", optimizer=opt,
	metrics=["accuracy"])

print("[INFO] training network for {} epochs...".format(EPOCHS))
H = model.fit_generator(aug.flow(trainX, trainY, batch_size=BS),
	validation_data=(testX, testY), steps_per_epoch=len(trainX) // BS,
	epochs=EPOCHS)

print("[INFO] evaluating network...")
predictions = model.predict(testX, batch_size=BS)
print(classification_report(testY.argmax(axis=1),
	predictions.argmax(axis=1), target_names=le.classes_))

print("[INFO] serializing network to '{}'...".format(args["model"]))
model.save(args["model"])

file = open(args["le"], "wb")
file.write(pickle.dumps(le))
file.close()

plotfig.style.use("ggplot")
plotfig.figure()
plotfig.plot(np.arange(0, EPOCHS), H.history["loss"], label="train_loss")
plotfig.plot(np.arange(0, EPOCHS), H.history["val_loss"], label="val_loss")
plotfig.plot(np.arange(0, EPOCHS), H.history["acc"], label="train_acc")
plotfig.plot(np.arange(0, EPOCHS), H.history["val_acc"], label="val_acc")
plotfig.title("Training Loss and Accuracy on Dataset")
plotfig.xlabel("Epoch")
plotfig.ylabel("Loss/Accuracy")
plotfig.legend(loc="lower left")
plotfig.savefig(args["plot"])