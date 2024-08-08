import cv2
import Gui
import time
from cvzone.HandTrackingModule import HandDetector 

detector = HandDetector(maxHands=2, detectionCon=0.8)

video = cv2.VideoCapture(0)
cv2.namedWindow("Image", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Image", 800, 600)

calculator = Gui.Calculator()

def mouse_callback(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        calculator.handleClick(x, y)

def getIndexTip(hand):
    indexTip = hand['lmList'][8]
    return indexTip

def getThumbTip(hand):
    thumbTip = hand['lmList'][4]
    return thumbTip

def isClicking(indexTip, thumbTip, button):
    xi, yi, _ = [int(i) for i in indexTip]
    xt, yt, _ = [int(j) for j in thumbTip]

    distance = ((xi-xt)**2 + (yi-yt)**2) ** 0.5
    if distance < 20 and button['x'] < xi < button['x'] + 60 and button['y'] < yi < button['y'] + 50:
        return True
    return False


cv2.setMouseCallback('Image', mouse_callback)


while True:
    success, img = video.read()
    hands, img = detector.findHands(img)

    calculator.drawCalculator(img)
    totalNumber = 0
    if hands:
        # Getting the number from each hand
        for hand in hands:
            fingersup = detector.fingersUp(hand)

            indexTip = getIndexTip(hand)
            thumbTip = getThumbTip(hand)
            cv2.circle(img, (indexTip[0], indexTip[1]), 10, (0, 255, 0), -1)

            for button in calculator.buttons:
                if isClicking(indexTip, thumbTip, button):
                    print(button['text'])
                    calculator.handleClick(button['x'], button['y'])
                    break


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
    cv2.imshow("Image", img)

    # Handling the exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()

