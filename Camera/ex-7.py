import cv2
import numpy as np

frame0 = None
frame1 = None
frame2 = None

f_x = 0.90
f_y = 0.80

blankimage = cv2.imread("frame.jpg")
blankimage = cv2.resize(blankimage, (0, 0), fx=f_x, fy=f_y)

cv2.namedWindow("preview0")
vc0 = cv2.VideoCapture(0)
vc1 = cv2.VideoCapture(1)
vc2 = cv2.VideoCapture(2)

if vc0.isOpened():  # try to get the first frame
    rval0, frame0 = vc0.read()
else:
    rval0 = False

if vc1.isOpened():  # try to get the first frame
    rval1, frame1 = vc1.read()
else:
    rval1 = False

if vc2.isOpened():  # try to get the first frame
    rval2, frame2 = vc2.read()
else:
    rval2 = False

while rval1 & rval0 & rval2:
    frame0 = cv2.resize(frame0, (0, 0), fx=f_x, fy=f_y)
    frame1 = cv2.resize(frame1, (0, 0), fx=f_x, fy=f_y)
    frame2 = cv2.resize(frame2, (0, 0), fx=f_x, fy=f_y)
    framearray1 = np.hstack((frame0, frame1))
    framearray2 = np.hstack((frame2, blankimage))
    framearray = np.vstack((framearray1, framearray2))
    cv2.imshow("preview0", framearray)
    rval0, frame0 = vc0.read()
    rval1, frame1 = vc1.read()
    rval2, frame2 = vc2.read()

    key = cv2.waitKey(20) & 0xFF
    if key == 27:  # exit on ESC
        break

cv2.destroyWindow("preview0")
