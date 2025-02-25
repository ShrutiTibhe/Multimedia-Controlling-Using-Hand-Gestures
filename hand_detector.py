
import cv2
import mediapipe as mp

class HandDetector:
    def __init__(self):
        self.drawing = mp.solutions.drawing_utils
        self.hands = mp.solutions.hands
        self.hand_obj = self.hands.Hands(max_num_hands=1)

    def detect_hand(self, image):
        res = self.hand_obj.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
        if res.multi_hand_landmarks:
            return res.multi_hand_landmarks[0]
        return None

    def draw_landmarks(self, image, hand_keypoints):
        self.drawing.draw_landmarks(image, hand_keypoints, self.hands.HAND_CONNECTIONS)
