import cv2 
from cvzone.HandTrackingModule import HandDetector 

detector = HandDetector(maxHands=3, detectionCon=0.8)

video = cv2.VideoCapture(0)
cv2.namedWindow("Image", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Image", 800, 600)
while True:
    success, img = video.read()
    hands, img = detector.findHands(img)

    totalNumber = 0
    if hands:
        for index, hand in enumerate(hands):
            fingersup = detector.fingersUp(hand)

            number = 0
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
            

    cv2.putText(img, f"Number: {totalNumber}", (10, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (36, 8, 8), 2)
    cv2.imshow("Image", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()