import cv2
import numpy as np

class Calculator:
    def __init__(self):
        self.displayValue = "0"

        self.buttons = [
            {'text': '7', 'x': 10, 'y': 30},
            {'text': '8', 'x': 70, 'y': 30},
            {'text': '9', 'x': 130, 'y': 30},
            {'text': '/', 'x': 190, 'y': 30},
            {'text': '4', 'x': 10, 'y': 80},
            {'text': '5', 'x': 70, 'y': 80},
            {'text': '6', 'x': 130, 'y': 80},
            {'text': '*', 'x': 190, 'y': 80},
            {'text': '1', 'x': 10, 'y': 130},
            {'text': '2', 'x': 70, 'y': 130},
            {'text': '3', 'x': 130, 'y': 130},
            {'text': '-', 'x': 190, 'y': 130},
            {'text': '0', 'x': 10, 'y': 180},
            {'text': '.', 'x': 70, 'y': 180},
            {'text': '=', 'x': 130, 'y': 180},
            {'text': '+', 'x': 190, 'y': 180},
        ]
    
    def drawCalculator(self, frame):
        # Drawing the background
        cv2.rectangle(frame, (0, 0), (240, 230), (112, 19, 19), -1)

        # Displaying the number
        cv2.rectangle(frame, (10, 10), (190, 20), (255, 255, 255), -1)
        cv2.putText(frame, self.displayValue, (20, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 0), 1)

        for button in self.buttons:
            cv2.rectangle(frame, (button['x'], button['y']), (button['x'] + 40, button['y'] + 30), (200, 200, 200), -1)
            cv2.putText(frame, button['text'], (button['x'] + 15, button['y'] + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1)
    

    def handleClick(self, x, y):
        for button in self.buttons:
            if button['x'] <= x < button['x'] + 60 and button['y'] <= y < button['y'] + 50:
                if button['text'] == '=':
                    try:
                        self.displayValue = str(eval(self.displayValue))
                    except Exception as e:
                        self.displayValue = "Error"
                else:
                    if self.displayValue == "0" and button['text'] != '.':
                        self.displayValue = button['text']
                    else:
                        self.displayValue += button['text']
    


