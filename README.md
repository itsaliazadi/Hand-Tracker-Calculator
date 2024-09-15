# Hand Gesture Calculator
# Overview
This project uses computer vision and machine learning to detect hand gestures and recognize user's index finger and numbers shown by the user's fingers. The calculator interface is displayed on the screen, and the user can interact with it using hand gestures to input numbers and perform calculations.
# Features
* Recognizes numbers shown by the user's fingers (1-10)
* Performs basic arithmetic operations (+, -, *, /)
* Displays the calculation result in real-time
# How it Works
* 1-The user opens the calculator application and is presented with a calculator interface on the screen.
* 2-The user shows a number with their fingers, and the application detects the hand gesture using computer vision.
* 3-The application recognizes the number shown by the user's fingers and inputs it into the calculator.
* 4-The user can perform arithmetic operations by clicking on the corresponding buttons using their hand gestures too.
* 5-The application displays the calculation result.
# Technical Details
* The HandTrackingModule from cvzone is used to detect hand gestures.
* The calculator interface is implemented using Python and OpenCV.
* The application uses a simple machine learning model to recognize numbers shown by the user's fingers.
# Getting Started
* 1-Clone the repository: git clone https://github.com/itsaliazadi/Hand-Tracker-Calculator
* 2-Run the application: python main.py
