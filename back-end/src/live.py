import cv2
import mediapipe as mp
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands


#check if hand is facing up
def hand_facing_up(wrist_y, middle_mcp_y):
    print(f"WRIST: {wrist_y}")
    print(f"MIDDLE_FINGER_MCP: {middle_mcp_y}")
    if wrist_y > middle_mcp_y:
        print("hand is facing up")
    else:
        print("hand is facing down")


# webcam input:
cap = cv2.VideoCapture(0)

# parameters
with mp_hands.Hands(
    max_num_hands=1,
    model_complexity=1,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as hands:
    # while being captured
    while cap.isOpened():
        success, image = cap.read()
        #if capture failed
        if not success:
            continue

        # To improve performance, optionally mark the image as not writeable to
        # pass by reference.
        image.flags.writeable = False
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = hands.process(image)

        # Draw the hand annotations on the image.
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:

                # Get the coordinates of the wrist and middle finger mcp
                wrist_y = hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].y
                middle_finger_mcp_y = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_MCP].y
                hand_facing_up(wrist_y, middle_finger_mcp_y)

                mp_drawing.draw_landmarks(
                    image,
                    hand_landmarks,
                    mp_hands.HAND_CONNECTIONS,
                    mp_drawing_styles.get_default_hand_landmarks_style(),
                    mp_drawing_styles.get_default_hand_connections_style())

        # Flip the image horizontally for a selfie-view display.
        cv2.imshow('MediaPipe Hands', cv2.flip(image, 1))
        if cv2.waitKey(5) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()

# have python3 version 3.9-3.12 installed
# in projected directory, do a "pip install mediapipe"

# mp_hands.HandLandmark.WRIST                # 0
# mp_hands.HandLandmark.THUMB_CMC            # 1
# mp_hands.HandLandmark.THUMB_MCP            # 2
# mp_hands.HandLandmark.THUMB_IP             # 3
# mp_hands.HandLandmark.THUMB_TIP            # 4
# mp_hands.HandLandmark.INDEX_FINGER_MCP     # 5
# mp_hands.HandLandmark.INDEX_FINGER_PIP     # 6
# mp_hands.HandLandmark.INDEX_FINGER_DIP     # 7
# mp_hands.HandLandmark.INDEX_FINGER_TIP     # 8
# mp_hands.HandLandmark.MIDDLE_FINGER_MCP    # 9
# mp_hands.HandLandmark.MIDDLE_FINGER_PIP    # 10
# mp_hands.HandLandmark.MIDDLE_FINGER_DIP    # 11
# mp_hands.HandLandmark.MIDDLE_FINGER_TIP    # 12
# mp_hands.HandLandmark.RING_FINGER_MCP      # 13
# mp_hands.HandLandmark.RING_FINGER_PIP      # 14
# mp_hands.HandLandmark.RING_FINGER_DIP      # 15
# mp_hands.HandLandmark.RING_FINGER_TIP      # 16
# mp_hands.HandLandmark.PINKY_MCP            # 17
# mp_hands.HandLandmark.PINKY_PIP            # 18
# mp_hands.HandLandmark.PINKY_DIP            # 19
# mp_hands.HandLandmark.PINKY_TIP            # 20
