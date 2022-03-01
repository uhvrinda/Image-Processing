import cv2
import numpy as np

FILE_NAME = 'dog.jpeg'
try:
	# Read image from disk.
	img = cv2.imread(FILE_NAME)

	# Canny edge detection.
	edges = cv2.Canny(img, 100, 200)

	# Write image back to disk.
	cv2.imwrite('result.jpg', edges)
except IOError:
	print ('Error while reading files !!!')

cv2.imshow("newImage",edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
