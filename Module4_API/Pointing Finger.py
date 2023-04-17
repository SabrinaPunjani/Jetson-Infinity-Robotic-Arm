# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 14:05:44 2023

@author: micha
"""

########################################
########################################
#CHALLENGE:
#how would u scale the x and y movement to the position on the screen?
#
#
#hint1: x and y coordinates on lines 112 and 113 correspond to position
#
#hint2: do u need to pass more paramters through the movement function?
#
########################################
########################################
########################################
import cv2
import mediapipe as mp
import xarm
import time
import threading




mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
arm = xarm.Controller('USB')
servo4 = xarm.Servo(4)
servo5 = xarm.Servo(5)
servo6 = xarm.Servo(6)
# For webcam input:
cap = cv2.VideoCapture(0)

with mp_hands.Hands(
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as hands:
  while cap.isOpened():
    success, image = cap.read()
    if not success:
      print("Ignoring empty camera frame.")
      continue

    # Flip the image horizontally for a later selfie-view display, and convert
    # the BGR image to RGB.
    image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
    # To improve performance, optionally mark the image as not writeable to
    # pass by reference.
    image.flags.writeable = False
    results = hands.process(image)

    # Draw the hand annotations on the image.
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    if results.multi_hand_landmarks:
      for hand_landmarks in results.multi_hand_landmarks:
        mp_drawing.draw_landmarks(
            image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
    
        # Get coordinates of index finger
        index_finger = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
        x, y, z = int(index_finger.x * image.shape[1]), int(index_finger.y * image.shape[0]), int(index_finger.z * image.shape[1])
        def movement(direction):
          position4 = arm.getPosition(servo4)
          position5 = arm.getPosition(servo5)
          position6 = arm.getPosition(servo6)
          
          if direction == "upleft":
            arm.setPosition(4, 295, 10, wait=True)
          
            arm.setPosition(4, 1000, 30,wait=True)
              
            arm.setPosition(6, position6+16, wait=False)
            return
            #time.sleep(3)
            #arm.setPosition([[1,500],[2, 500],[3, 300],[4,500],[5,500],[6,840]])
          elif direction == "downright":
            
            arm.setPosition(4, 0, 50,wait=True)
            arm.setPosition(4, 700, 10, wait=True)
            
            return
            #time.sleep(3)
            #arm.setPosition([[1,500],[2, 500],[3, 300],[4,500],[5,500],[6,165]])
          elif direction =="upright":
            arm.setPosition(4, 295, 10, wait=True)
            arm.setPosition(4, 0, 30,wait=True)
            
           
              
            return
            #time.sleep(3)
            #arm.setPosition([[1,300],[2, 500],[3, 475],[4,410],[5,700],[6,500]])
          elif direction =="downleft":
            arm.setPosition(4, 1000, 50,wait=True)
           
            arm.setPosition(4, 700, 50, wait=True)
          
            return
            #arm.setPosition([[1,500],[2, 500],[3, 170],[4,900],[5,500],[6,500]])
          
        
        
        
        
        # Determine direction based on x and y coordinates
        
        
        if y < image.shape[0]/2:
            if x < image.shape[1]/2:
              direction = "upleft"
              movement(direction)
            else: 
              direction = "upright"
              movement(direction)
              
              
        else:
            if x < image.shape[1]/2:
              direction = "downleft"
              
              movement(direction)
             
            else:
              direction = "downright"
              
              movement(direction)
             
        
        print(direction)
        
        
       
        
        
            

            
            

    # Show the annotated image.
    cv2.imshow('Hand Gestures', image)
    arm.setPosition([[1,500],[2, 500],[3, 300],[4,500],[5,500],[6,165]])
    if cv2.waitKey(5) & 0xFF == 27:
      break
cap.release()