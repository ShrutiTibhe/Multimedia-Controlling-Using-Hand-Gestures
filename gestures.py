import cv2
import pyautogui

def count_fingers(lst):
    cnt = 0
    thresh = (lst.landmark[0].y * 100 - lst.landmark[9].y * 100) / 2

    if (lst.landmark[5].y * 100 - lst.landmark[8].y * 100) > thresh:
        cnt += 1

    if (lst.landmark[9].y * 100 - lst.landmark[12].y * 100) > thresh:
        cnt += 1

    if (lst.landmark[13].y * 100 - lst.landmark[16].y * 100) > thresh:
        cnt += 1

    if (lst.landmark[17].y * 100 - lst.landmark[20].y * 100) > thresh:
        cnt += 1

    if (lst.landmark[5].x * 100 - lst.landmark[4].x * 100) > 6:
        cnt += 1

    return cnt

def perform_gesture_action(cnt):
    if cnt == 1:
        pyautogui.press("right")
    elif cnt == 2:
        pyautogui.press("left")
    elif cnt == 3:
        pyautogui.press("up")
    elif cnt == 4:
        pyautogui.press("down")
    elif cnt == 5:
        pyautogui.press("playpause")

def draw_gesture_text(image, cnt):
    gesture_text = ""
    if cnt == 1:
        gesture_text = "Right"
    elif cnt == 2:
        gesture_text = "Left"
    elif cnt == 3:
        gesture_text = "Up"
    elif cnt == 4:
        gesture_text = "Down"
    elif cnt == 5:
        gesture_text = "Play/Pause"

    cv2.putText(image, gesture_text, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                               

 
 

 
 
 
 
 
 
 
 
