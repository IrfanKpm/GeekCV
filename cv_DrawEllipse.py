import cv2
import numpy as np	
	
# Reading an image in default mode
image = np.zeros((512, 512, 3), dtype='uint8')
	
# Window name in which image is displayed
window_name = 'Image'
center_coordinates = (120, 100)
axesLength = (100, 50)
angle = 30
startAngle = 0
endAngle = 360
# Blue color in BGR
color = (255, 0, 0)
# Line thickness of -1 px
thickness = -1
# Using cv2.ellipse() method
# Draw a ellipse with blue line borders of thickness of -1 px
image = cv2.ellipse(image, center_coordinates, axesLength, angle,
						startAngle, endAngle, color, thickness)

# Displaying the image
cv2.imshow(window_name, image)
cv2.waitKey(0)
cv2.destroyAllWindows()

