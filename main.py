# You may run into issues installing pytesseract, this is because python wants you to install things into virtual environments
# For our usecase, venv aren't super useful as we are only making one project at a time, so use the flags below:
# sudo pip3 install pytesseract --break-system-packages
# https://nanonets.com/blog/ocr-with-tesseract/
from PIL import Image
#import pytesseract
import cv2
import os, sys, inspect #For dynamic filepaths
import numpy as np;
import heapq


#Find the execution path and join it with the direct reference


cam = cv2.VideoCapture(0)
while True:

  check, frame = cam.read()
  frame = cv2.resize(frame,(640,480))


  image = cv2.imread('video', frame)
  #cols = raw.shape[1]


  # Resize
  #image = cv2.resize(image, (320, 120))

  # Greyscale
  image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

  # Threshold         120 is threshold, 255 is what we assign if it is below this
  _, image = cv2.threshold(image, 200, 255, cv2.THRESH_BINARY)

  # Canny
  raw = cv2.Canny(image, 20,40)

  #Countours (needs canny)
  contours, _ = cv2.findContours(raw, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
  
  contours_poly = [None]*len(contours)
#   boundRect = [None]*len(contours)
  fitLine = [None] * len(contours)
  contourArea = [None] * len(contours)

  for i, c in enumerate(contours):
      contours_poly[i] = cv2.approxPolyDP(c, 3, True)
    #   boundRect[i] = cv2.boundingRect(contours_poly[i])
      fitLine[i] = cv2.fitLine(contours[i], cv2.DIST_L2,0,0.01,0.01)
      contourArea[i] = cv2.contourArea(contours[i])
      #lefty = int((-))
  # rows,cols = image.shape[:2]
  image = np.zeros((image.shape[0], image.shape[1],3), dtype=np.uint8)
  lines = heapq.nlargest(2, contourArea)
  print(lines)

  for i in range(len(lines)):
      cv2.drawContours(image, contours, i, (255,0,0),2)
    # #   cv2.rectangle(image, (int(boundRect[i][0]), int(boundRect[i][1])), 
    # #                  (int(boundRect[i][0]+boundRect[i][2]), int(boundRect[i][1]+boundRect[i][3])),(0,255,0),2)
    #   vx = fitLine[i][0]
    #   vy = fitLine[i][1]
    #   x = fitLine[i][2]
    #   y = fitLine[i][3]


    #   # lefty = int(((int(-fitLine[i][2])*int(fitLine[i][1])) / (int(fitLine[i][0])))+int(fitLine[i][3])) 
    #   # righty = int(((cols-int(fitLine[i][2]))*int(fitLine[i][1])/int(fitLine[i][0]))+int(fitLine[i][3]))
    #   lefty = int((-x*vy/vx) + y) 
    #   righty = int(((cols-x)*vy/vx)+y)
    #   # p1 = np.array(cols-1,righty).astype(np.unit8)
    #   # p2 =np.array(0,lefty).astype(np.unit8)
    #   # p1x = cols-1
    #   # p1x = p1x.to_bytes(8, 'little', signed=True)
    #   # p1y = righty.to_bytes(8, 'little', signed=True)
    #   # p2y = lefty.to_bytes(8, 'little', signed=False)
    #   # p1 = tuple([(cols-1), righty])
    #   # p2 = tuple([0, lefty])

    #   # pk1 = np.zeros(p1, dtype=np.uint8)
    #   # pk2 = np.zeros(p2, dtype=np.uint8)
    #   # p2x = 0
    #   print(righty)
    #   # point1 = cv2.Point(cols-1, righty)
    #   # point2 = cv2.Point(0, lefty)
    #   if(righty > 0 and lefty > 0):
    #     cv2.line(image, (639, righty),(0, lefty),(0,255,0),2)
    #   # print(lefty)
      
    #   #print(cols)
  

  

  # contours = cnt
  # print("Number of Contours Found = " + str(len(contours)))
  # image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
   
  
  # x,y,w,h = cv2.boundingRect(cnt)
  # rect = cv2.minAreaRect(cnt)
  # box = cv2.boxPoints(rect)
  # box = np.int0(box)
  # cv2.drawContours(image,[box],0,(0,0,255),2)



  cv2.imshow('video', image)
  cv2.imshow('raw', raw)

  # if len(contours) > 0:
  #     c = max(contours, key=cv2.contourArea)
  #     M = cv2.moments(c)

  #     if M["m00"] != 0:
  #         cX = int(M["m10"]/ M["m00"])
  #         cY = int(M["m01"]/ M["m00"])
          

  #         height, width, _ = frame.shape
  #         center_x = width // 2

  #         if cX < center_x - 50:
  #             print("move left")
  #         elif cY > center_x + 50:
  #             print("move right")
  #         else:
  #             print("foward")

        



  key = cv2.waitKey(1)

  if key == 27:

       break

# def bigTwo(NUMBERS):
#     max1 = max2 = float('-inf')

#     for num in NUMBERS:
#         if num > max 


cam.release()
cv2.destroyAllWindows()
