import cv2
cam = cv2.VideoCapture(0)
cv2.namedWindow("Test")
img_counter=0
while True:
    ret,frame =cam.read()
    if not ret:
        print("failed to grab frame")
        break
    cv2.imshow("Test",frame)
    
    k = cv2.waitKey(1)
    #using Esc key for closing window
    if k%256==27:
        print("closing...")
        break
    #using space key for capturing image
    if k%256 == 32:
        img_name ="opencv_frame{}.png".format(img_counter)
        cv2.imwrite(img_name,frame)
        print("{}written".format(img_name))
        img_counter+=1
        
cam.release()
cv2.destroyAllWindows()

img=cv2.imread("opencv_frame0.png")
# now printing captured  Image
cv2.imshow("output1",img)
gratImg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# we can use different algorithms for image bluring here we are using medianblur
blrImg=cv2.medianBlur(gratImg,7) 
edges=cv2.adaptiveThreshold(blrImg,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,7,7)# kernal value should be of k%2==1
color=cv2.bilateralFilter(img,7,255,250)
cartoon=cv2.bitwise_and(color,color,mask=edges)
# now printing gray Image
cv2.imshow("output2",gratImg) 
# now printing blur  Image
cv2.imshow("output3",blrImg)
# now printing edged
cv2.imshow("output4",edges)
# now printing colored image
cv2.imshow("output5",color)
# now printing Animated image
cv2.imshow("output6",cartoon)

cv2.waitKey(0)
cv2.destroyAllWindows()