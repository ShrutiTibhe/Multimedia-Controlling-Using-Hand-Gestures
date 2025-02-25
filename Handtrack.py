import cv2
from hand_detector import HandDetector
from gestures import count_fingers, perform_gesture_action, draw_gesture_text
import pyautogui
import time

cap = cv2.VideoCapture(0)

hand_detector = HandDetector()

start_init = False
prev = -1

while True:
    end_time = time.time()
    ret, frm = cap.read()


    frm = cv2.flip(frm, 1)

    hand_keypoints = hand_detector.detect_hand(frm)

    if hand_keypoints is not None:
        cnt = count_fingers(hand_keypoints)

        if not(prev == cnt):
            if not(start_init):
                start_time = time.time()
                start_init = True
            elif (end_time-start_time) > 0.2:
                perform_gesture_action(cnt)
                prev = cnt
                start_init = False

        hand_detector.draw_landmarks(frm, hand_keypoints)
        draw_gesture_text(frm, cnt)

    cv2.imshow("window", frm)

    if cv2.waitKey(1) == 27:
        cv2.destroyAllWindows()
        cap.release()
        break