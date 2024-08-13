import cv2
import Gui
import time
from cvzone.HandTrackingModule import HandDetector 


def getIndexTip(hand) -> list:
    indexTip = hand['lmList'][8]
    return indexTip

def getThumbTip(hand) -> list:
    thumbTip = hand['lmList'][4]
    return thumbTip

def isClicking(indexTip, thumbTip, button, preIndexTip, lastClickTime) -> bool:
    xi, yi, _ = [int(i) for i in indexTip]
    xt, yt, _ = [int(j) for j in thumbTip]

    avgX = int((xi + preIndexTip[0]) / 2)
    avgY = int((yi + preIndexTip[1]) / 2)

    preIndexTip = (avgX, avgY)

    distance = ((xi-xt)**2 + (yi-yt)**2) ** 0.5
    velocity = distance / (time.time() - lastClickTime)
    buttonWidth = 70
    buttonHeight = 60
    if distance < 20 and (button['x'] <= xi <= button['x'] + buttonWidth) and (button['y'] <= yi <= button['y'] + buttonHeight) and velocity < 200:
        lastClickTime = time.time()
        return True
    return False