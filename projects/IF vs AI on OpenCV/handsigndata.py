
import cv2
import mediapipe as mp
import numpy as np
import csv
import time
import math
OUTPUT_FILE = r"C:\Users\Loq\Documents\programs\myprojects\image_dataset.csv"
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)
mp_draw = mp.solutions.drawing_utils
cap = cv2.VideoCapture(0)
FRAMES_TO_CAPTURE = 50
CAPTURE_DELAY = 3
FRAME_INTERVAL = 0.1

def normalize(lm_list):
    wrist = np.array(lm_list[0])
    ref = np.array(lm_list[9])
    scale = np.linalg.norm(ref - wrist) + 1e-6
    return list(((np.array(lm_list) - wrist) / scale).flatten())

def dist(a, b):
    return math.hypot(a[0]-b[0], a[1]-b[1])

def angle(a, b, c):
    a, b, c = np.array(a), np.array(b), np.array(c)
    ba = a - b
    bc = c - b
    cos_angle = np.dot(ba, bc) / (np.linalg.norm(ba)*np.linalg.norm(bc) + 1e-6)
    return np.degrees(np.arccos(cos_angle))

def thumb_direction(lm_list):
    return [1 if lm_list[4][1] < lm_list[0][1] else 0]

def thumb_angle(lm_list):
    wrist = np.array(lm_list[0])
    thumb_tip = np.array(lm_list[4])
    vec = thumb_tip - wrist
    return [np.degrees(np.arctan2(vec[1], vec[0]))]

def finger_states(lm_list, label):
    states = []
    if label == "Right":
        states.append(1 if lm_list[4][0] > lm_list[3][0] else 0)
    else:
        states.append(1 if lm_list[4][0] < lm_list[3][0] else 0)
    tips = [8, 12, 16, 20]
    pips = [6, 10, 14, 18]
    for tip, pip in zip(tips, pips):
        states.append(1 if lm_list[tip][1] < lm_list[pip][1] else 0)
    return states

def extract_features(lm_list, label):
    features = []
    features.extend(normalize(lm_list))
    joints = [
        (0,1,2),(1,2,3),(2,3,4),
        (5,6,7),(6,7,8),
        (9,10,11),(10,11,12),
        (13,14,15),(14,15,16),
        (17,18,19),(18,19,20)
    ]
    for a,b,c in joints:
        features.append(angle(lm_list[a], lm_list[b], lm_list[c]))
    tips = [4, 8, 12, 16, 20]
    for i in range(len(tips)):
        for j in range(i+1, len(tips)):
            features.append(dist(lm_list[tips[i]], lm_list[tips[j]]))
    features.extend(finger_states(lm_list, label))
    features.extend(thumb_direction(lm_list))
    features.extend(thumb_angle(lm_list))
    return features  # 70

print("Press 's' to capture / ESC to exit")
label = input("Enter word label: ")
with open(OUTPUT_FILE, "a", newline="") as f:
    writer = csv.writer(f)
    capturing = False
    count = 0
    start_time = 0
    last_capture = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frame = cv2.flip(frame, 1)
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(rgb)
        h, w, _ = frame.shape
        key = cv2.waitKey(1) & 0xFF
        if key == ord('s'):
            capturing = True
            count = 0
            start_time = time.time()
        if capturing and time.time() - start_time < CAPTURE_DELAY:
            t = int(CAPTURE_DELAY - (time.time() - start_time))
            cv2.putText(frame, f"Start in {t}", (10,50),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)
        elif capturing and count < FRAMES_TO_CAPTURE:
            if time.time() - last_capture > FRAME_INTERVAL:
                if results.multi_hand_landmarks and len(results.multi_hand_landmarks) == 1:
                    lm_list = []
                    for lm in results.multi_hand_landmarks[0].landmark:
                        lm_list.append((int(lm.x*w), int(lm.y*h)))
                    label_hand = results.multi_handedness[0].classification[0].label
                    feats = extract_features(lm_list, label_hand)
                    if len(feats) == 70:
                        writer.writerow(feats + [label])
                        count += 1
                        last_capture = time.time()
                cv2.putText(frame, f"{count}/{FRAMES_TO_CAPTURE}", (10,50),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)
        elif count >= FRAMES_TO_CAPTURE:
            capturing = False
            cv2.putText(frame, "DONE", (10,50),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2)
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
        cv2.imshow("Capture", frame)
        if key == 27:
            break
cap.release()
cv2.destroyAllWindows()