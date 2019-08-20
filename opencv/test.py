import numpy as np
import cv2

# code for reading an image and displaying it to screen
img = cv2.imread("grass.jpeg", 1)
#cv2.namedWindow('Original', cv2.WINDOW_NORMAL)
#cv2.namedWindow('binary', cv2.WINDOW_NORMAL)
#cv2.namedWindow('Blue', cv2.WINDOW_NORMAL)
#cv2.namedWindow('Green', cv2.WINDOW_NORMAL)
#cv2.namedWindow('Red', cv2.WINDOW_NORMAL)

thr = 220
matrix = (3,3)

blur = cv2.GaussianBlur(img, matrix, 0)

gray = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)
(T_val, bin_thr) = cv2.threshold(gray, thr, 255, cv2.THRESH_BINARY)
print(bin_thr.shape)
#cv2.imshow('gray', gray)
kernel = np.ones((5,5),np.uint8)
dilated = cv2.dilate(bin_thr,kernel,iterations = 2)
contours, hierarchy = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#cv2.imshow('binary', bin_thr)
print(contours)
cv2.drawContours(bin_thr, contours, -1, (255,255,255), 3)
cv2.imshow('countour', bin_thr)
#cv2.imshow('Original', img)
#cv2.imshow('Blue', img[:,:,0])
#cv2.imshow('Green', img[:,:,1])
#cv2.imshow('Red', img[:,:,2])
cv2.waitKey(0)
cv2.destroyAllWindows()


""" code for drawing an image
pic = np.zeros((300,300,3), dtype = 'uint8')
cv2.rectangle(pic, (100,100), (200,200), (255,255,255), 3)
cv2.line(pic, (100,100), (200,200), (255,255,255))
cv2.circle(pic, (150,150), 75, (255,255,0))
cv2.putText(pic, 'Dagan', (20, 150), cv2.FONT_HERSHEY_PLAIN, 0.5, (255,255,255))

cv2.imshow('dark', pic)"""

"""
img = cv2.imread("test.jpg", 0)
cols = img.shape[1]
rows = img.shape[0]

M = np.float32([[1,0,150],[0,1,70]])
shifted = cv2.warpAffine(img, M, (cols,rows))

cv2.imshow('shifted', shifted)

cv2.waitKey(0)
center = (cols/2, rows/2)
angle = 90
scale = 0.5

M = cv2.getRotationMatrix2D(center, angle, scale)

rotate = cv2.warpAffine(img, M, (cols,rows))
cv2.imshow('rotate', rotate)
cv2.waitKey(0)
cv2.destroyAllWindows()"""

""" biary thresholding
img = cv2.imread("test.jpg", 0)

thr = 220

(T_val, bin_thr) = cv2.threshold(img, thr, 255, cv2.THRESH_BINARY)

cv2.imshow('binary', bin_thr)


cv2.waitKey(0)
cv2.destroyAllWindows()"""

""" blur an image
img = cv2.imread("test.jpg")

matrix = (7,7)

blur = cv2.GaussianBlur(img, matrix, 0)

cv2.imshow('blur', blur)

cv2.waitKey(0)
cv2.destroyAllWindows()"""

"""
img = cv2.imread("test.jpg")
kernel = 5
median = cv2.medianBlur(img, kernel)

cv2.imshow('median', median)

cv2.waitKey(0)
cv2.destroyAllWindows()"""
"""
img = cv2.imread("test.jpg")
dimpixel = 7
color = 200
space =100

filter =cv2.bilateralFilter(img, dimpixel, color, space)

cv2.imshow('bilat', filter)

cv2.waitKey(0)
cv2.destroyAllWindows()"""
"""
img = cv2.imread("test.jpg")
thr1 = 50
thr2 = 100
canny = cv2.Canny(img, thr1, thr2)

cv2.imshow('canny', canny)

cv2.waitKey(0)
cv2.destroyAllWindows()
"""
"""
videocap = cv2.VideoCapture(0)
ret, pic = videocap.read()
cv2.imshow('test', pic)
cv2.waitKey(0)
cv2.destroyAllWindows()"""
