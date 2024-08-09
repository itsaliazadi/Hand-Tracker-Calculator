import cv2
import Gui
import time
from cvzone.HandTrackingModule import HandDetector 


def getIndexTip(hand):
    indexTip = hand['lmList'][8]
    return indexTip

def getThumbTip(hand):
    thumbTip = hand['lmList'][4]
    return thumbTip

def isClicking(indexTip, thumbTip, button, preIndexTip, lastClickTime):
    xi, yi, _ = [int(i) for i in indexTip]
    xt, yt, _ = [int(j) for j in thumbTip]

    avg_x = int((xi + preIndexTip[0]) / 2)
    avg_y = int((yi + preIndexTip[1]) / 2)

    preIndexTip = (avg_x, avg_y)

    distance = ((xi-xt)**2 + (yi-yt)**2) ** 0.5
    velocity = distance / (time.time() - lastClickTime)
    if distance < 20 and button['x'] <= xi <= button['x'] + 70 and button['y'] <= yi <= button['y'] + 60 and velocity < 200:
        lastClickTime = time.time()
        return True
    return False