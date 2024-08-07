import cv2
import Gui
from cvzone.HandTrackingModule import HandDetector 

detector = HandDetector(maxHands=2, detectionCon=0.8)

video = cv2.VideoCapture(0)
cv2.namedWindow("Image", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Image", 800, 600)

calculator = Gui.Calculator()

def mouse_callback(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        calculator.handleClick(x, y)

cv2.setMouseCallback('Image', mouse_callback)

while True:
    success, img = video.read()
    hands, img = detector.findHands(img)

    totalNumber = 0
    if hands:
        # Getting the number from each hand
        for hand in hands:
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

            totalNumber += number

    # Showing the number to the user
    cv2.putText(img, f"Number: {totalNumber}", (300, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (36, 8, 8), 2)

    calculator.drawCalculator(img)
    cv2.imshow("Image", img)

    # Handling the exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()

