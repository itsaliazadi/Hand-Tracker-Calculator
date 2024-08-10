import cv2
import time
import numpy as np

class Calculator:
    def __init__(self):
        self.displayValue = "0"

        self.buttons = [
            {'text': '7', 'x': 30, 'y': 50},
            {'text': '8', 'x': 120, 'y': 50},
            {'text': '9', 'x': 210, 'y': 50},
            {'text': '/', 'x': 300, 'y': 50},
            {'text': '4', 'x': 30, 'y': 120},
            {'text': '5', 'x': 120, 'y': 120},
            {'text': '6', 'x': 210, 'y': 120},
            {'text': '*', 'x': 300, 'y': 120},
            {'text': '1', 'x': 30, 'y': 190},
            {'text': '2', 'x': 120, 'y': 190},
            {'text': '3', 'x': 210, 'y': 190},
            {'text': '-', 'x': 300, 'y': 190},
            {'text': '0', 'x': 30, 'y': 260},
            {'text': '.', 'x': 120, 'y': 260},
            {'text': '=', 'x': 210, 'y': 260},
            {'text': '+', 'x': 300, 'y': 260},
        ]
    
    def drawCalculator(self, frame):
        # Drawing the background
        cv2.rectangle(frame, (0, 0), (400, 350), (112, 19, 19), -1)

        # Displaying the number
        cv2.rectangle(frame, (20, 20), (360, 40), (255, 255, 255), -1)
        cv2.putText(frame, self.displayValue, (30, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 0), 1)

        for button in self.buttons:
            cv2.rectangle(frame, (button['x'], button['y']), (button['x'] + 70, button['y'] + 50), (200, 200, 200), -1)
            cv2.putText(frame, button['text'], (button['x'] + 30, button['y'] + 40), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 0), 1)
    

    def handleClick(self, x, y):
        for button in self.buttons:
            if button['x'] <= x < button['x'] + 70 and button['y'] <= y < button['y'] + 50:
                if button['text'] == '=':
                    try:
                        self.displayValue = str(eval(self.displayValue))
                    except Exception as e:
                        self.displayValue = ""
                else:
                    if self.displayValue == "0" and button['text'] != '.':
                        self.displayValue = button['text']
                    else:
                        self.displayValue += button['text']

    def handleHandInput(self, number):
        if self.displayValue == "0":
            self.displayValue = ""
        for button in self.buttons:
            if button['text'] == str(number):
                self.displayValue += str(number)
    


