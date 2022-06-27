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

    # represents the nodes that are at the tip of the finger (thumb, pointer, middle, ring, pinky)
    tipIDs = [4,8,12,16,20]

    # represents the nodes that are at the middle joint of the finger (thumb, pointer, middle, ring, pinky)
    midFingerIDs = [3,6,10,14,19]

    # represents the nodes that are at the upper middle joint of the finger (thumb, pointer, middle, ring, pinky)
    upperMidIds = [3,7,11,15,19]

    # represents the nodes that are at the base joint of the finger (thumb, pointer, middle, ring, pinky)
    baseJointIDs = [2,5,9,13,17]
    #setting draw to true makes points larger or what is set within the handtrackingmodule
    lmList = detector.findPosition(img, draw=False)
    if len(lmList) != 0:
        # used if user is making an 'A'
        if (lmList[tipIDs[0]][1] > lmList[baseJointIDs[0]][1]) and (
                lmList[tipIDs[1]][2] > lmList[baseJointIDs[1]][2]) and (
                lmList[tipIDs[2]][2] > lmList[baseJointIDs[2]][2]) and (
                lmList[tipIDs[3]][2] > lmList[baseJointIDs[3]][2]) and (
                lmList[tipIDs[4]][2] > lmList[baseJointIDs[4]][2]) and (
                lmList[tipIDs[1]][1] < lmList[midFingerIDs[0]][1]) and (
                lmList[tipIDs[0]][2] < lmList[baseJointIDs[1]][2]):
            cv2.putText(img, str('A'), (30, 70), cv2.FONT_HERSHEY_SIMPLEX, 3, (255, 0, 255), 3)

        # used if user makes an 'B'
        elif (lmList[tipIDs[0]][1] < lmList[baseJointIDs[0]][1]) and (
                lmList[tipIDs[0]][1] > lmList[baseJointIDs[2]][1]) and (
                lmList[tipIDs[0]][2] < lmList[baseJointIDs[1]][2]) and (
                lmList[tipIDs[0]][2] < lmList[midFingerIDs[0]][2]) and (
                lmList[tipIDs[1]][2] < lmList[midFingerIDs[1]][2]) and (
                lmList[tipIDs[2]][2] < lmList[midFingerIDs[2]][2]) and (
                lmList[tipIDs[3]][2] < lmList[midFingerIDs[3]][2]) and (
                lmList[tipIDs[4]][2] < lmList[midFingerIDs[4]][2]):
            cv2.putText(img, str('B'), (30, 70), cv2.FONT_HERSHEY_SIMPLEX, 3, (255, 0, 255), 3)

        # used if user makes an 'C'
        elif (lmList[tipIDs[0]][1] < lmList[midFingerIDs[0]][1]) and (
                lmList[midFingerIDs[0]][1] > lmList[baseJointIDs[1]][1]) and (
                lmList[tipIDs[1]][2] > lmList[upperMidIds[1]][2]) and (
                lmList[tipIDs[2]][2] > lmList[upperMidIds[2]][2]) and (
                lmList[tipIDs[3]][2] > lmList[upperMidIds[3]][2]) and (
                lmList[tipIDs[4]][2] > lmList[upperMidIds[4]][2]) and (
                lmList[tipIDs[0]][2] > lmList[baseJointIDs[1]][2]) and (
                lmList[tipIDs[1]][2] < lmList[baseJointIDs[1]][2]) and (
                lmList[tipIDs[2]][2] < lmList[baseJointIDs[2]][2]) and (
                lmList[tipIDs[3]][2] < lmList[baseJointIDs[3]][2]) and (
                lmList[tipIDs[4]][2] < lmList[baseJointIDs[4]][2]):
            cv2.putText(img, str('C'), (30, 70), cv2.FONT_HERSHEY_SIMPLEX, 3, (255, 0, 255), 3)

        # used if user makes an 'D'
        elif (lmList[tipIDs[0]][1] < lmList[baseJointIDs[0]][1]) and (
                lmList[tipIDs[0]][2] < lmList[midFingerIDs[0]][2]) and (
                lmList[tipIDs[0]][2] > lmList[midFingerIDs[2]][2]) and (
                lmList[tipIDs[1]][2] < lmList[upperMidIds[1]][2]) and (
                lmList[tipIDs[2]][2] > lmList[midFingerIDs[2]][2]) and (
                lmList[tipIDs[3]][2] > lmList[midFingerIDs[3]][2]) and (
                lmList[tipIDs[4]][2] > lmList[midFingerIDs[4]][2]):
            cv2.putText(img, str('D'), (30, 70), cv2.FONT_HERSHEY_SIMPLEX, 3, (255, 0, 255), 3)

        # used if user makes an 'E'
        elif (lmList[tipIDs[0]][1] < lmList[baseJointIDs[0]][1]) and (
                lmList[tipIDs[0]][1] < lmList[midFingerIDs[0]][1]) and (
                lmList[tipIDs[0]][2] > lmList[tipIDs[2]][2]) and (
                lmList[tipIDs[0]][2] > lmList[tipIDs[1]][2]) and (
                lmList[tipIDs[1]][2] > lmList[midFingerIDs[1]][2]) and (
                lmList[tipIDs[2]][2] > lmList[midFingerIDs[2]][2]) and (
                lmList[tipIDs[3]][2] > lmList[midFingerIDs[3]][2]) and (
                lmList[tipIDs[4]][2] > lmList[midFingerIDs[4]][2]) and (
                lmList[tipIDs[0]][1] < lmList[baseJointIDs[1]][1]):
            cv2.putText(img, str('E'), (30, 70), cv2.FONT_HERSHEY_SIMPLEX, 3, (255, 0, 255), 3)

        # used if user makes an 'F'
        elif (lmList[tipIDs[0]][1] < lmList[midFingerIDs[0]][1]) and (
                lmList[tipIDs[1]][2] > lmList[midFingerIDs[1]][2]) and (
                lmList[tipIDs[1]][2] > lmList[upperMidIds[1]][2]) and (
                lmList[tipIDs[2]][2] < lmList[midFingerIDs[2]][2]) and (
                lmList[tipIDs[3]][2] < lmList[midFingerIDs[3]][2]) and (
                lmList[tipIDs[4]][2] < lmList[midFingerIDs[4]][2]):
            cv2.putText(img, str('F'), (30, 70), cv2.FONT_HERSHEY_SIMPLEX, 3, (255, 0, 255), 3)

        # used if user makes a 'G'
        elif (lmList[tipIDs[0]][1] > lmList[baseJointIDs[0]][1]) and (
                lmList[tipIDs[0]][1] > lmList[midFingerIDs[0]][1]) and (
                lmList[tipIDs[1]][1] > lmList[upperMidIds[1]][1]) and (
                lmList[tipIDs[1]][1] > lmList[midFingerIDs[1]][1]) and (
                lmList[tipIDs[1]][1] > lmList[baseJointIDs[1]][1]) and (
                lmList[tipIDs[2]][2] > lmList[midFingerIDs[2]][2]) and (
                lmList[tipIDs[3]][2] > lmList[midFingerIDs[3]][2]) and (
                lmList[tipIDs[4]][2] > lmList[midFingerIDs[4]][2]) and (
                lmList[tipIDs[0]][1] > lmList[upperMidIds[1]][1]) and (
                lmList[tipIDs[1]][1] > lmList[midFingerIDs[0]][1]) and (
                lmList[tipIDs[0]][2] < lmList[baseJointIDs[4]][2]):
            cv2.putText(img, str('G'), (30, 70), cv2.FONT_HERSHEY_SIMPLEX, 3, (255, 0, 255), 3)

        # used if user makes an 'H'
        elif (lmList[tipIDs[1]][1] > lmList[upperMidIds[1]][1]) and (
                lmList[tipIDs[1]][1] > lmList[midFingerIDs[1]][1]) and (
                lmList[tipIDs[1]][1] > lmList[baseJointIDs[1]][1]) and (
                lmList[tipIDs[2]][1] > lmList[upperMidIds[2]][1]) and (
                lmList[tipIDs[2]][1] > lmList[midFingerIDs[2]][1]) and (
                lmList[tipIDs[2]][1] > lmList[baseJointIDs[2]][1]) and (
                lmList[tipIDs[1]][2] < lmList[tipIDs[2]][2]) and (
                lmList[upperMidIds[1]][2] < lmList[upperMidIds[2]][2]) and (
                lmList[baseJointIDs[1]][2] < lmList[baseJointIDs[2]][2]) and (
                lmList[tipIDs[0]][2] > lmList[tipIDs[1]][2]) and (
                lmList[tipIDs[1]][1] > lmList[upperMidIds[2]][1]) and (
                lmList[baseJointIDs[3]][2] > lmList[baseJointIDs[0]][2]) and (
                lmList[baseJointIDs[4]][2] > lmList[baseJointIDs[0]][2]):
            cv2.putText(img, str('H'), (30, 70), cv2.FONT_HERSHEY_SIMPLEX, 3, (255, 0, 255), 3)

        # used if user makes an 'i'
        elif (lmList[tipIDs[0]][1] > lmList[baseJointIDs[0]][1]) and (
                lmList[tipIDs[1]][2] > lmList[baseJointIDs[1]][2]) and (
                lmList[tipIDs[2]][2] > lmList[baseJointIDs[2]][2]) and (
                lmList[tipIDs[3]][2] > lmList[baseJointIDs[3]][2]) and (
                lmList[tipIDs[4]][2] < lmList[baseJointIDs[4]][2]) and (
                lmList[tipIDs[4]][2] < lmList[upperMidIds[4]][2]) and (
                lmList[tipIDs[4]][2] < lmList[midFingerIDs[4]][2]) and (
                lmList[tipIDs[1]][1] < lmList[midFingerIDs[0]][1]):
            cv2.putText(img, str('I'), (30, 70), cv2.FONT_HERSHEY_SIMPLEX, 3, (255, 0, 255), 3)

        # used if user makes a 'J'
        # currently unable to due to movement.

        # used if user makes a 'K'
        elif (lmList[midFingerIDs[0]][1] < lmList[baseJointIDs[0]][1]) and (
                lmList[tipIDs[0]][2] < lmList[midFingerIDs[0]][2]) and (
                lmList[tipIDs[1]][2] < lmList[upperMidIds[1]][2]) and (
                lmList[tipIDs[1]][2] < lmList[midFingerIDs[1]][2]) and (
                lmList[tipIDs[1]][2] < lmList[baseJointIDs[1]][2]) and (
                lmList[tipIDs[2]][2] < lmList[baseJointIDs[2]][2]) and (
                lmList[upperMidIds[2]][2] < lmList[baseJointIDs[2]][2]) and (
                lmList[midFingerIDs[2]][2] < lmList[baseJointIDs[2]][2]) and (
                lmList[tipIDs[2]][2] > lmList[tipIDs[1]][2]) and (
                lmList[tipIDs[3]][2] > lmList[baseJointIDs[3]][2]) and (
                lmList[tipIDs[4]][2] > lmList[baseJointIDs[4]][2]) and (
                lmList[tipIDs[3]][2] > lmList[midFingerIDs[3]][2]) and (
                lmList[tipIDs[4]][2] > lmList[midFingerIDs[4]][2]):
            cv2.putText(img, str('K'), (30, 70), cv2.FONT_HERSHEY_SIMPLEX, 3, (255, 0, 255), 3)


        # used if user makes an 'L'
        elif (lmList[tipIDs[0]][1] > lmList[midFingerIDs[0]][1]) and (
                lmList[tipIDs[0]][1] > lmList[baseJointIDs[0]][1]) and (
                lmList[tipIDs[0]][2] > lmList[midFingerIDs[2]][2]) and (
                lmList[tipIDs[1]][2] < lmList[upperMidIds[1]][2]) and (
                lmList[tipIDs[1]][2] < lmList[midFingerIDs[1]][2]) and (
                lmList[tipIDs[1]][2] < lmList[baseJointIDs[1]][2]) and (
                lmList[tipIDs[2]][2] > lmList[baseJointIDs[2]][2]) and (
                lmList[tipIDs[3]][2] > lmList[baseJointIDs[3]][2]) and (
                lmList[tipIDs[4]][2] > lmList[baseJointIDs[4]][2]):
            cv2.putText(img, str('L'), (30, 70), cv2.FONT_HERSHEY_SIMPLEX, 3, (255, 0, 255), 3)


        # used if user makes an 'M'
        elif (lmList[tipIDs[1]][2] > lmList[midFingerIDs[1]][2]) and (
                lmList[tipIDs[2]][2] > lmList[midFingerIDs[2]][2]) and (
                lmList[tipIDs[3]][2] > lmList[midFingerIDs[3]][2]) and (
                lmList[tipIDs[4]][2] > lmList[midFingerIDs[4]][2]) and (
                lmList[tipIDs[4]][2] > lmList[tipIDs[1]][2]) and (
                lmList[tipIDs[4]][2] > lmList[tipIDs[2]][2]) and (
                lmList[tipIDs[4]][2] > lmList[tipIDs[3]][2]) and (
                lmList[tipIDs[1]][2] > lmList[midFingerIDs[0]][2]) and (
                lmList[tipIDs[2]][2] > lmList[midFingerIDs[0]][2]) and (
                lmList[tipIDs[3]][2] > lmList[midFingerIDs[0]][2]) and (
                lmList[midFingerIDs[0]][1] < lmList[baseJointIDs[0]][1]) and (
                lmList[tipIDs[0]][2] > lmList[midFingerIDs[3]][2]):
            cv2.putText(img, str('M'), (30, 70), cv2.FONT_HERSHEY_SIMPLEX, 3, (255, 0, 255), 3)

        # Used if user makes an 'N'
        elif (lmList[tipIDs[0]][1] > lmList[midFingerIDs[3]][1]) and (
                lmList[tipIDs[0]][1] < lmList[midFingerIDs[2]][1]) and (
                lmList[tipIDs[1]][2] > lmList[midFingerIDs[1]][2]) and (
                lmList[tipIDs[2]][2] > lmList[midFingerIDs[2]][2]) and (
                lmList[tipIDs[3]][2] > lmList[midFingerIDs[3]][2]) and (
                lmList[tipIDs[4]][2] > lmList[midFingerIDs[4]][2])  and (
                lmList[tipIDs[1]][2] < lmList[tipIDs[3]][2]) and (
                lmList[tipIDs[2]][2] < lmList[tipIDs[3]][2]) and (
                lmList[tipIDs[0]][2] < lmList[midFingerIDs[3]][2]):
            cv2.putText(img, str('N'), (30, 70), cv2.FONT_HERSHEY_SIMPLEX, 3, (255, 0, 255), 3)

        # used if user makes an 'O'
        elif (lmList[tipIDs[0]][1] > lmList[tipIDs[1]][1]) and (
                lmList[tipIDs[0]][1] < lmList[midFingerIDs[0]][1]) and (
                lmList[tipIDs[1]][2] > lmList[upperMidIds[1]][2]) and (
                lmList[tipIDs[2]][2] > lmList[upperMidIds[2]][2]) and (
                lmList[tipIDs[3]][2] > lmList[upperMidIds[3]][2]) and (
                lmList[tipIDs[4]][2] > lmList[upperMidIds[4]][2]) and (
                lmList[tipIDs[1]][2] > lmList[midFingerIDs[1]][2]) and (
                lmList[tipIDs[2]][2] > lmList[midFingerIDs[2]][2]) and (
                lmList[tipIDs[3]][2] > lmList[midFingerIDs[3]][2]):
            cv2.putText(img, str('O'), (30, 70), cv2.FONT_HERSHEY_SIMPLEX, 3, (255, 0, 255), 3)

        # used if user makes a 'P'
        elif (lmList[tipIDs[1]][2] > lmList[baseJointIDs[1]][2]) and (
                lmList[tipIDs[2]][2] > lmList[upperMidIds[2]][2]) and (
                lmList[tipIDs[2]][2] > lmList[midFingerIDs[2]][2]) and (
                lmList[tipIDs[2]][2] > lmList[baseJointIDs[2]][2]) and (
                lmList[midFingerIDs[3]][2] > lmList[baseJointIDs[3]][2]) and (
                lmList[midFingerIDs[4]][2] > lmList[baseJointIDs[4]][2]) and (
                lmList[tipIDs[0]][1] < lmList[midFingerIDs[0]][1]):
            cv2.putText(img, str('P'), (30, 70), cv2.FONT_HERSHEY_SIMPLEX, 3, (255, 0, 255), 3)

        # used if user makes a 'Q'
        elif (lmList[tipIDs[1]][2] > lmList[upperMidIds[1]][2]) and (
                lmList[tipIDs[1]][2] > lmList[midFingerIDs[1]][2]) and (
                lmList[tipIDs[1]][2] > lmList[baseJointIDs[1]][2]) and (
                lmList[tipIDs[0]][2] > lmList[midFingerIDs[0]][2]) and (
                lmList[tipIDs[0]][2] > lmList[baseJointIDs[0]][2]) and (
                lmList[midFingerIDs[2]][2] > lmList[baseJointIDs[2]][2]) and (
                lmList[midFingerIDs[3]][2] > lmList[baseJointIDs[3]][2]) and (
                lmList[midFingerIDs[4]][2] > lmList[baseJointIDs[4]][2]) and (
                lmList[tipIDs[0]][1] > lmList[tipIDs[1]][1]) and (
                lmList[tipIDs[2]][2] < lmList[tipIDs[1]][2]) and (
                lmList[tipIDs[3]][2] < lmList[tipIDs[1]][2]) and (
                lmList[tipIDs[4]][2] < lmList[tipIDs[1]][2]):
            cv2.putText(img, str('Q'), (30, 70), cv2.FONT_HERSHEY_SIMPLEX, 3, (255, 0, 255), 3)


    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    #cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 3, (255, 0, 255), 3)
    cv2.imshow("Image", img)
    cv2.waitKey(1)
