import cv2
import Gui
import time
from NumberDetection import *
from cvzone.HandTrackingModule import HandDetector


detector = HandDetector(maxHands=2, detectionCon=0.9)

screenWidth = 800
screenHeight = 600

video = cv2.VideoCapture(0)
cv2.namedWindow("Image", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Image", screenWidth, screenHeight)

calculator = Gui.Calculator()

# These variables are used to calculate the finger movement velocity
preIndexTip = (0, 0)
lastClickTime = 0

# Previous number the user showed with their fingers
preNumber = 0

while True:
    success, img = video.read()
    img = cv2.flip(img, 1)

    # Detecting hands in the image
    hands, img = detector.findHands(img)

    # Deawing the calculator
    calculator.drawCalculator(img)

    totalNumber = 0
    if hands:
        # Getting the number from each hand
        for hand in hands:
            indexTip = getIndexTip(hand)
            thumbTip = getThumbTip(hand)
            
            # Moving a green circle as the user's index finger moves as a marker
            greenColor = (0, 255, 0)
            cv2.circle(img, (indexTip[0], indexTip[1]), 10, greenColor, -1)

            # Looking for the button that's been clicked and then handle the click
            for button in calculator.buttons:
                if isClicking(indexTip, thumbTip, button, preIndexTip, lastClickTime):
                    calculator.handleClick(button['x'], button['y'])
                    time.sleep(0.1)
                    break
            
            # Detecting the number user shows with their fingers
            fingersup = detector.fingersUp(hand)

            number = 0
            # Recognizing the number
            if fingersup == [0, 1, 0, 0, 0]:
                number = 1
            elif fingersup == [0, 1, 1, 0, 0]:
                number = 2
            elif fingersup == [0, 1, 1, 1, 0]:
                number = 3
            elif fingersup == [0, 1, 1, 1, 1]:
                number = 4
            elif fingersup == [1, 1, 1, 1, 1]:
                number = 5

            # The reason for totalNumber is that we want to capture the number shown with both hands
            totalNumber += number

    # To prevent the totalNumber from being typed in the number bar repeatedly
    if totalNumber != 0 and totalNumber != preNumber:  
        calculator.handleHandInput(totalNumber)
        preNumber = totalNumber
        totalNumber = 0

    # Showing the number to the user
    cv2.putText(img, f"Number: {totalNumber}", (450, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (36, 8, 8), 2)
    cv2.imshow("Image", img)

    # Handling the exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()