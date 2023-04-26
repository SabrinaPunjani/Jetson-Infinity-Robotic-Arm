#created on 2023-04-16 author @sabrina
#MIT Open Source Initiative License 
##############################################
##############################################
#
##
#Problem/Challenge:
#use the robot to plug in the charge plug for an electric vehicle 
##############################################
##############################################
#---------------importing modules-----------------
import cv2
import xarm
import time
import numpy as np
#-------------------------------------------------
arm = xarm.Controller('USB')
#cam input
cap = cv2.VideoCapture(0)



arm.setPosition([[1,200],[2, 515],[3,840],[4,280],[5,620],[6,200]])
time.sleep(20)
#grip charging cable
arm.setPosition([[1,550],[2, 515],[3,840],[4,280],[5,620],[6,200]])


while(True):
	# Capture frame-by-frame
	ret, frame = cap.read()

	# load the image, clone it for output, and then convert it to grayscale
			
	output = frame.copy()
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	
	# apply GuassianBlur to reduce noise. medianBlur is also added for smoothening, reducing noise.
	gray = cv2.GaussianBlur(gray,(5,5),0)
	gray = cv2.medianBlur(gray,5)
	
	# Adaptive Guassian Threshold is to detect sharp edges in the Image. For more information Google it.
	gray = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv2.THRESH_BINARY,11,3.5)
	
	
	
	# detect circles in the image
	circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 200, param1=30, param2=45, minRadius=0, maxRadius=0)
	# print circles
	
	# ensure at least some circles were found
	if circles is not None:
		# convert the (x, y) coordinates and radius of the circles to integers
		circles = np.round(circles[0, :]).astype("int")
		
		# loop over the (x, y) coordinates and radius of the circles
		for (x, y, r) in circles:
			# draw the circle in the output image, then draw a rectangle in the image
			# corresponding to the center of the circle
			cv2.circle(output, (x, y), r, (0, 255, 0), 4)
			cv2.rectangle(output, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1) #this is where the charger must plug in 
			
		# Display the resulting frame
		cv2.imshow('gray',gray)
		cv2.imshow('frame',output)
	if cv2.waitKey(1) & 0xFF == ord('q'): #press q to exit 
		break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()