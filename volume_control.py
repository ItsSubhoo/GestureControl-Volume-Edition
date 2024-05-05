import cv2
import mediapipe as mp
import time
import numpy as np
import math
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

cap = cv2.VideoCapture(0)


devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = interface.QueryInterface(IAudioEndpointVolume)
# volume.GetMute()
volume.GetMasterVolumeLevel()
maxvol = volume.GetVolumeRange()[0]


print(maxvol)


# volume.SetMasterVolumeLevel(-20.0, None)


pTime = 0
x1 = y1 = x2 = y2 = 0
mphands = mp.solutions.hands
hands = mphands.Hands(min_detection_confidence=.8)

mpDrow = mp.solutions.drawing_utils
while True:
    success, img = cap.read()
    imgRgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    reasults = hands.process(imgRgb)
    # print(reasults.multi_hand_landmarks)
    if reasults.multi_hand_landmarks:
        for onehand in reasults.multi_hand_landmarks:

            for idno, lm in enumerate(onehand.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                print(idno, cx, cy)

                # print(listlm)
                if idno == 8:
                    cv2.circle(img, (cx, cy), 8, (0, 250, 0), 3, cv2.FILLED)
                    x1, y1 = cx, cy
                    print(8, x1, y1)
                if idno == 4:
                    cv2.circle(img, (cx, cy), 8, (0, 250, 0), 3, cv2.FILLED)
                    x2, y2 = cx, cy
                    print(4, x2, y2)
                if x1 != 0 and x2 != 0 and y1 != 0 and y2 != 0:
                    cv2.line(img, (x2, y2), (x1, y1), (0, 250, 0), 3)
                    midx, midy = (x1+x2)//2, (y1+y2)//2
                    cv2.circle(img, (midx, midy), 8, (0, 250, 0))
                    length = math.hypot(x1-x2, y1-y2)
                    # print("clen= ", length)
                    dfac = 200/-maxvol

                    cvol = (length//dfac)+maxvol

                    print("Current vol000 :", cvol)

                    if length < 30:
                        cv2.circle(img, (midx, midy), 8,
                                   (0, 0, 250), cv2.FILLED)
                        volume.SetMasterVolumeLevel(maxvol, None)
                        print("len =", length, "vol= ", 94)
                        # volume.GetMute()
                    elif cvol > -1:
                        volume.SetMasterVolumeLevel(0.0, None)
                        print("len =", length, "vol= ", 0)
                    else:
                        volume.SetMasterVolumeLevel(cvol, None)
                        print("len =", length, "vol= ", cvol)

            mpDrow.draw_landmarks(img, onehand, mphands.HAND_CONNECTIONS)

    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (10, 70),
                cv2.FONT_HERSHEY_COMPLEX_SMALL, 3, (0, 255, 0), 2)

    cv2.imshow("image", img)
    cv2.waitKey(1)
