#----------------------------------------------------------------
import cv2
from cvzone import HandTrackingModule, overlayPNG
import numpy as np

# Load intro, kill, and winner images
intro = cv2.imread('frames/img1.jpeg')
kill = cv2.imread('frames/img2.png')
winner = cv2.imread('frames/img3.png')

# Read the camera
cam = cv2.VideoCapture(0)

# Initialize hand detector
detector = HandTrackingModule.HandDetector(maxHands=1, detectionCon=0.77)

# Load game components
sqr_img = cv2.imread('img/sqr (1).png')
mlsa = cv2.imread('img/mlsa.png')

# Intro screen will stay until 'q' is pressed
gameOver = False
NotWon = True

# Game logic up to the teams
# -----------------------------------------------------------------------------------------
while not gameOver:
    # Read camera feed
    success, img = cam.read()

    # Detect hands
    hands, img = detector.findHands(img)

    # Show intro screen until 'q' is pressed
    cv2.imshow("Intro", intro)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Loss screen
if NotWon:
    for i in range(10):
        # Show the kill image read before
        cv2.imshow("Loss", kill)
        cv2.waitKey(100)

    # End loss screen when 'q' is pressed
    while True:
        cv2.imshow("Loss", kill)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Win screen
else:
    # Show the winner image read before
    cv2.imshow("Winner", winner)

    # End win screen when 'q' is pressed
    while True:
        cv2.imshow("Winner", winner)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Destroy all the windows
cv2.destroyAllWindows()