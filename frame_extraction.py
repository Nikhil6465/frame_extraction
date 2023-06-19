# Project 2 Break video into multiple frames and store it in a folder called frames.

import cv2

cap = cv2.VideoCapture(r"D:\Drop_Project\drop_videos\drop_video2.mp4")
ret, image = cap.read() # Reading for the first frame here is important, because we are using ret in while loop.

count = 59407 # This is used for giving image names.

while True:
    if ret == True:
        cv2.imwrite(r'D:\Drop_Project\drop_video2_frames\image%d.jpg'%count, image)
        # 1st parameter => It tells the cap to read the value as milliseconds or other equivalent notation
        # 2nd parameter => It defines the value of the 1st parameter. eg. if 1st param is in ms then whatever value we pass as the second param, 
        # it will read by the cap as ms value and start capturing the frame from that position.
        # For exp, If we have to read a frame at 2sec then we have to pass 20000ms.
        #cap.set(cv2.CAP_PROP_POS_MSEC, count*100) # 0 --> 100, 100 --> 200, 200 --> 300 and so onnn...
        ret, image = cap.read()
        cv2.imshow('Frame', image)
        count += 1
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()