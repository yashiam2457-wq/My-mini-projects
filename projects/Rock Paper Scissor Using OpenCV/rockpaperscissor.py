import cv2
import mediapipe as mp
import time
import random
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils
rb = random.randint(0, 2)
hands = mp_hands.Hands(max_num_hands=1)
mv = ["Rock", "Paper", "Scissor"]
cap = cv2.VideoCapture(0)
ct = time.time()

tip_ids = [4, 8, 12, 16, 20]
red = cv2.imread('C:\\Users\\Loq\\Documents\\programs\\myprojects\\red.png')
red = cv2.resize(red, (150, 150))
overlay = red
rock = cv2.imread('C:\\Users\\Loq\\Documents\\programs\\myprojects\\rock.png')
rock = cv2.resize(rock, (150, 150))
paper = cv2.imread('C:\\Users\\Loq\\Documents\\programs\\myprojects\\paper.jpg')
paper = cv2.resize(paper, (150, 150))
scissor = cv2.imread('C:\\Users\\Loq\\Documents\\programs\\myprojects\\scissor.jpg')
scissor = cv2.resize(scissor, (150, 150))

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
                res =""
                if fingers == [0,0,0,0,0]:
                    gesture = "Rock"
                elif fingers == [1,1,1,1,1]:
                    gesture = "Paper"
                elif fingers == [0,1,1,0,0]:
                    gesture = "Scissor"
                elif time.time() - ct > 1:
                    overlay = red
                    ct = time.time()
                    rb = random.randint(0, 2)
                if rb == 0:
                    overlay = rock
                elif rb == 1:
                    overlay = paper
                elif rb == 2:
                    overlay = scissor
                # 0 - Rock, 1 - Paper, 2 - Scissor
                if (rb == 0 and gesture == "Rock") or (rb == 1 and gesture == "Paper") or (rb == 2 and gesture == "Scissor"):
                    res = "Draw"
                if (rb == 0 and gesture == "Scissor") or (rb == 1 and gesture == "Rock") or (rb == 2 and gesture == "Paper"):
                    res = "Robot Wins"
                if (rb == 0 and gesture == "Paper") or (rb == 1 and gesture == "Scissor") or (rb == 2 and gesture == "Rock"):
                    res = "Player Wins"
                h_f, w_f, _ = frame.shape
                h_o, w_o, _ = overlay.shape
                roi = frame[h_f - h_o : h_f, 0 : w_o]
                frame[h_f - h_o : h_f, 0 : w_o] = overlay
                # Display
                cv2.putText(frame, f'Player Move: {gesture}', (10,50),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)
                cv2.putText(frame, f'Robot Move: {mv[rb]}', (10,100),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2)
                cv2.putText(frame, f'Result: {res}', (10,150),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)
    cv2.imshow("Rock Paper Scissor Game", frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break
cap.release()
cv2.destroyAllWindows()