import cv2

img = cv2.imread("images/mango.jpg")
cv2.imshow("image1", img)
img2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imwrite("images/mango2.jpg", img2) 


cv2.imshow("image2", img2)

cv2.waitKey(0)
cv2.destroyAllWindows()

