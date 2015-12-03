import cv2
import time
import numpy as np
import qrtools
qrdeco = qrtools.QR()
camera = cv2.VideoCapture(0) # seleccionamos la camara
#circles = cv2.HoughCircles(gray, cv2.cv.CV_HOUGH_GRADIENT, 1.2, 100)

def get_image():
	retval, im = camera.read()
	return im

while True:
    ejemplo = None
    (grabbed, frame) = camera.read()
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # pasar a escala de grises
    #gray = cv2.GaussianBlur(gray, (21, 21), 0) # agregar blur, difuminar, sacar detalles
    camera_capture = get_image()
    
    #if ejemplo == None:
    #   ejemplo = gray
    
    #(grabbed, frame) = camera.read()
    #gray2 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # pasar a escala de grises
    #gray2 = cv2.GaussianBlur(gray, (21, 21), 0) # agregar blur, difuminar, sacar detalles
    
    #diffimg = cv2.absdiff(ejemplo, gray2)
    camera_capture = get_image()
    cv2.imwrite("./out.png", camera_capture)
    if qrdeco.decode('out.png'):
        print 'result: ' + qrdeco.data
    
    cv2.imshow("", frame)
    
    
    
    key = cv2.waitKey(1) & 0xFF
 
    # if the `q` key is pressed, break from the lop
    if key == ord("q"):
        break


camera.release()
cv2.destroyAllWindows()
