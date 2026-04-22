import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

hands = mp_hands.Hands(max_num_hands=1)

cap = cv2.VideoCapture(0)

tip_ids = [4, 8, 12, 16, 20]

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = hands.process(rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            lm_list = []
            h, w, _ = frame.shape

            for id, lm in enumerate(hand_landmarks.landmark):
                cx, cy = int(lm.x * w), int(lm.y * h)
                lm_list.append((cx, cy))

            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            if lm_list:
                fingers = []
                if lm_list[tip_ids[0]][0] > lm_list[tip_ids[0] - 1][0]:
                    fingers.append(1)
                else:
                    fingers.append(0)

                for i in range(1, 5):
                    if lm_list[tip_ids[i]][1] < lm_list[tip_ids[i] - 2][1]:
                        fingers.append(1)
                    else:
                        fingers.append(0)
                total_fingers = sum(fingers)
                gesture = ""
                if fingers == [0,0,0,0,0]:
                    gesture = "FIST"
                elif fingers == [1,1,1,1,1]:
                    gesture = "OPEN HAND"
                elif fingers == [0,1,0,0,0]:
                    gesture = "POINTING"
                elif fingers == [0,1,1,0,0]:
                    gesture = "PEACE"
                elif fingers == [1,1,0,0,1]:
                    gesture = "SPIDERMAN"
                elif fingers == [0,1,0,0,1]:
                    gesture = "Rock"
                elif fingers == [1,0,0,0,0] and lm_list[tip_ids[0]][1] < lm_list[tip_ids[0] - 1][1]:
                    gesture = "THUMBS UP"
                elif fingers == [1,0,0,0,0] and lm_list[tip_ids[0]][1] > lm_list[tip_ids[0] - 1][1]:
                    gesture = "THMBS DOWN"
                cv2.putText(frame, f'Fingers: {total_fingers}', (10,50),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)

                cv2.putText(frame, f'Gesture: {gesture}', (10,100),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2)
    cv2.imshow("Gesture Recognition", frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()