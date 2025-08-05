import numpy as np, cv2
import matplotlib.pyplot as plt
img = None
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

labels =[]
colors = [
    'red',
    'blue',
    'green',
    'yellow',
    'black',
    'white',
    'gray'
]

while cap.isOpened():
    ret, frame = cap.read()
    

def train_event(event, x, y, flags, param):
    global frame
    if event == cv2.EVENT_LBUTTONDOWN:
        color = frame[x, y]
        cv2.circle(frame, (x, y), 3, (int(color[0]), int(color[1]), int(color[3])), -1)
        print("색상을 입력해 주십시오. \n1: red, 2: blue, 3: green, 4: yellow, 5: black, 6: white, 7: gray, C to cancle")
        key = cv2.waitKey(0)
        if key == 67:
            pass
        elif 49 < key < 55:
            print(f'{color}가 {colors[key-49]}로 저장되었습니다.')



cv2.setMouseCallback(img, train_event)
cv2.waitKey(0)
cv2.destroyAllWindows()