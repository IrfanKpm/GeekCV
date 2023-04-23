import cv2
from matplotlib import pyplot as plt

img = cv2.imread('images/mango.jpg',0) 
plt.hist(img.ravel(),256,[0,256])

cv2.imshow("image",img)
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
