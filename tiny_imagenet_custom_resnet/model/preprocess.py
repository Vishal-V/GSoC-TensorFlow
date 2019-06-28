import os
import cv2 # Transfer import to main.py
import imutils # Transfer import to main.py
import tensorflow # Transfer import to main.py
from tensorflow.keras.callbacks import Callback
from tensorflow.keras.preprocessing.image import img_to_array

class EpochCheckpoint(Callback):
	def __init__(self, every=5, startAt=0):
		super(Callback, self).__init__()
		self.outputPath = outputPath
		self.every = every
		self.intEpoch = startAt

	def on_epoch_end(self, epoch, logs={}):
		# Save the model to disk at 'every' interval
		if (self.intEpoch + 1) % self.every == 0:
			p = os.path.sep.join([self.outputPath,
				"epoch_{}.hdf5".format(self.intEpoch + 1)])
			self.model.save(p, overwrite=True)

		self.intEpoch += 1


class ImageToArrayPreprocessor:
	def __init__(self, dataFormat=None):
		self.dataFormat = dataFormat

	def preprocess(self, image):
		# Rearranges the dimensions of the image
		return img_to_array(image, data_format=self.dataFormat)

class AspectRatioPreprocessor:
	def __init__(self, width, height, inter=cv2.INTER_AREA):
		self.width = width
		self.height = height
		self.inter = inter

	def preprocess(self, image):
		(h, w) = image.shape[:2]
		dW = 0
		dH = 0

		if w < h:
			image = imutils.resize(image, width=self.width, inter=self.inter)
			dH = int((image.shape[0] - self.height)/2.0)

		else:
			image = imutils.resize(image, height=self.height, inter=self.inter)
			dW = int((image.shape[1] - self.width)/2.0)


		(h,w) = image.shape[:2]
		image = image[dH:h - dH, dW:w - dW]

		return cv2.resize(image, (self.width, self.height), interpolation=self.inter)

