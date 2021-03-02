import numpy as np
import cv2

# Reading the detected parking lines image.
image = cv2.imread("parking_lines.png")

# Creating the points as array to draw polyline on each parking spot
spot0 = np.array([[35, 168], [101, 153], [140, 218], [66, 226]], np.int32)
spot1 = np.array([[102, 155], [163, 139], [206, 202], [140, 219]], np.int32)
spot2 = np.array([[163, 139], [222, 125], [270, 185], [206, 200]], np.int32)
spot3 = np.array([[222, 124], [280, 111], [332, 169], [272, 185]], np.int32)
spot4 = np.array([[60, 86], [117, 73], [162, 137], [100, 152]], np.int32)
spot5 = np.array([[116, 74], [172, 63], [221, 124], [162, 138]], np.int32)
spot6 = np.array([[172, 63], [227, 51], [278, 109], [222, 123]], np.int32)
spot7 = np.array([[227, 52], [278, 41], [332, 96], [278, 108]], np.int32)


# Function to draw the parking spot
def draw_parking_spot(points, color):
    cv2.fillPoly(image, [points], color=color)
    return image


# Applying the function to each spot in the image
draw_parking_spot(spot0, (0, 128, 255))
draw_parking_spot(spot1, (255, 0, 0))
draw_parking_spot(spot2, (0, 255, 0))
draw_parking_spot(spot3, (0, 0, 255))
draw_parking_spot(spot4, (50, 100, 0))
draw_parking_spot(spot5, (100, 50, 0))
draw_parking_spot(spot6, (0, 50, 100))
final_image = draw_parking_spot(spot7, (200, 0, 150))

# Visualizing the final image and saving it as .png file
while(1):
    cv2.imwrite("Parking_spot.png", final_image)
    cv2.imshow('Parking Spot', final_image)
    k = cv2.waitKey(20) & 0xFF
    if k == 27:
        break
