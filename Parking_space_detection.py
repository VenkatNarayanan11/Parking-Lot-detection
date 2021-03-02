import numpy as np
import cv2

image = cv2.imread("parking_lines.png")

# Class to get the position of each point by left mouse click


class CoordinateStore:
    def __init__(self):
        self.points = []

    def select_point(self, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDBLCLK:
            cv2.circle(image, (x, y), 3, (255, 0, 0), -1)
            self.points.append((x, y))


# instantiate the class
coordinateStore1 = CoordinateStore()


# Passing the parking lines image and binding the function to a window
cv2.namedWindow('image')
cv2.setMouseCallback('image', coordinateStore1.select_point)

while(1):
    cv2.imshow('image', image)
    k = cv2.waitKey(20) & 0xFF
    if k == 27:
        break


# print "Selected Coordinates: "
point = []
for i in coordinateStore1.points:
    point.append(i)

print(point)
