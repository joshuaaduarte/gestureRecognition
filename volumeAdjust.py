import cv2
import mediapipe as mp
import time
import handTrackingModule as htm
import math

pTime = 0
cTime = 0
cap = cv2.VideoCapture(0)
detector = htm.handDetector(detectionCon=0.7)

while True:
    success, img = cap.read()
    # setting draw to true will allow you to see points along the hand
    img = detector.findHands(img)

    #setting draw to true makes points larger or what is set within the handtrackingmodule
    lmList = detector.findPosition(img, draw=False)
    if len(lmList) != 0:
        # print(lmList[4], lmList[8])

        x1, y1 = lmList[4][1], lmList[4][2]
        x2, y2 = lmList[8][1], lmList[8][2]
        cx, cy = (x1 + x2)//2, (y1+y2)//2

        cv2.circle(img, (x1,y1), 14, (255,0,255), cv2.FILLED)
        cv2.circle(img, (x2,y2), 14, (255,0,255), cv2.FILLED)
        cv2.line(img, (x1,y1),(x2,y2), (255,0,255), 2 )
        cv2.circle(img, (cx, cy), 6, (20, 0, 255), cv2.FILLED)

        length = math.hypot(x2-x1,y2-y1)
        print(length)
        if length<40:
            cv2.circle(img, (cx, cy), 6, (0, 255, 0), cv2.FILLED)
        elif length>250:
            cv2.circle(img, (cx, cy), 6, (0, 9, 255), cv2.FILLED)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 3, (255, 0, 255), 3)
    cv2.imshow("Image", img)
    cv2.waitKey(1)
