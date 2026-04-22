import cv2
import mediapipe as mp
import numpy as np
import joblib
import math
from collections import deque
model_1 = joblib.load("hand_sign_model-9S.pkl")
model_2 = joblib.load("hand_sign_model-2B.pkl")

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=2)
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

pred_buffer = deque(maxlen=8)
THRESHOLD = 0.5

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
    return features

print("Press ESC to exit")
while True:
    ret, frame = cap.read()
    if not ret:
        break
    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb)
    h, w, _ = frame.shape
    prediction = ""
    confidence = 0
    if results.multi_hand_landmarks and results.multi_handedness:
        hand_count = len(results.multi_hand_landmarks)

        if hand_count == 1:
            lm_list = []
            for lm in results.multi_hand_landmarks[0].landmark:
                lm_list.append((int(lm.x*w), int(lm.y*h)))
            label = results.multi_handedness[0].classification[0].label
            feats = extract_features(lm_list, label)
            if len(feats) == model_1.n_features_in_:
                probs = model_1.predict_proba([feats])[0]
                idx = np.argmax(probs)
                pred = model_1.classes_[idx]
                conf = probs[idx]
                if conf > THRESHOLD:
                    pred_buffer.append(pred)
                else:
                    pred_buffer.clear()
                if len(pred_buffer) > 0:
                    prediction = max(set(pred_buffer), key=pred_buffer.count)
                    confidence = conf

        elif hand_count == 2:
            left = [0]*70
            right = [0]*70
            for hand_landmarks, handedness in zip(results.multi_hand_landmarks,
                                                  results.multi_handedness):
                lm_list = []
                for lm in hand_landmarks.landmark:
                    lm_list.append((int(lm.x*w), int(lm.y*h)))
                label = handedness.classification[0].label
                feats = extract_features(lm_list, label)
                if label == "Left":
                    left = feats
                else:
                    right = feats
            feats = left + right + [2]
            if len(feats) == model_2.n_features_in_:
                probs = model_2.predict_proba([feats])[0]
                idx = np.argmax(probs)
                pred = model_2.classes_[idx]
                conf = probs[idx]
                if conf > THRESHOLD:
                    pred_buffer.append(pred)
                else:
                    pred_buffer.clear()
                if len(pred_buffer) > 0:
                    prediction = max(set(pred_buffer), key=pred_buffer.count)
                    confidence = conf

        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    cv2.putText(frame, f'Word: {prediction}', (10,50),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)
    cv2.putText(frame, f'Conf: {confidence:.2f}', (10,90),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255,0,0), 2)
    cv2.imshow("Gesture Recognition", frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break
cap.release()
cv2.destroyAllWindows()