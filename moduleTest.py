import cv2
import mediapipe as mp
import time
import handTrackingModule as htm


pTime = 0
cTime = 0
cap = cv2.VideoCapture(0)
detector = htm.handDetector()

while True:
    success, img = cap.read()
    # setting draw to true will allow you to see points along the hand
    img = detector.findHands(img, draw=True)

    #setting draw to true makes points larger or what is set within the handtrackingmodule
    lmList = detector.findPosition(img, draw=False)
    if len(lmList) != 0:
        print(lmList[4])

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 3, (255, 0, 255), 3)
    cv2.imshow("Image", img)
    cv2.waitKey(1)
