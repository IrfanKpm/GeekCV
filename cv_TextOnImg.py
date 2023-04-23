# Python program to explain cv2.putText() method
	
# importing cv2
import cv2
	
# path	
# Reading an image in default mode
image = cv2.imread('images/mango.jpg')
	
# Window name in which image is displayed
window_name = 'Image'
# font
font = cv2.FONT_HERSHEY_SIMPLEX
# org ( org: It is the coordinates of the bottom-left corner of the text string )
org = (20, 80) 
# fontScale
fontScale = 1
# color in BGR
color = (150, 120, 255)
# Line thickness of 2 px
thickness = 2
# Using cv2.putText() method
image = cv2.putText(image, 'OpenCV', org, font,
				fontScale, color, thickness, cv2.LINE_AA)

# Displaying the image
cv2.imshow(window_name, image)
cv2.waitKey(0)
cv2.destroyAllWindows()
