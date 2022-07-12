import numpy as np
import cv2 

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()
a=0;
while True:
    
    image_path = r'C:\Users\...'
    ret, frame = cap.read()
    
   
    cv2.cvtColor
    
    if a==0:
        print("ready")
    
    cv2.imshow('frame',frame)
    
    a+=1
    
    if cv2.waitKey(1) == ord('q'):
        print("q pushed")
        
    
        im = cv2.imread("img_vert2.jpg")
        
        
        
        #mask1 = cv2.inRange(image, (0, 80, 0), (150, 255,150))
        
        
        

 
 
 
        for x in range(im.shape[0]):
            for y in range(im.shape[1]):#on balaye l'image
                R,G,B=cv2.split(im)
                
                   
                
                if im[x,y][1] >= 80 and im[x,y][0] <= 140  and im[x,y][2] <= 140 and im[x,y][0]+15 < im[x,y][1] and im[x,y][2]+15< im[x,y][1] :   
                    
                    print(im[x][y])
                else :
                    im[x,y][0]=0 
                    im[x,y][1]=0
                    im[x,y][2]=0
                    
                    
                    
                
        
        

        

        cv2.imwrite("img2.jpg", im)
        break
    
cap.release()
cv2.destroyAllWindows()