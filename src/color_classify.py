import numpy as np, cv2
import matplotlib.pyplot as plt
import csv

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

colors = [
    'red',
    'blue',
    'green',
    'yellow',
    'black',
    'white',
    'gray']

def train_event(event, x, y, flags, param):
    global rgb, hsv, img
    if event == cv2.EVENT_LBUTTONDOWN:
        color = rgb[y, x]
        cv2.circle(img, (x, y), 3, (int(color[2]), int(color[1]), int(color[0])), -1)
        print("색상을 입력해 주십시오. \n1: red, 2: blue, 3: green, 4: yellow, 5: black, 6: white, 7: gray, C to cancle")
        key = cv2.waitKey(0)
        if key == 67:
            pass
        elif 49 <= key <= 55:
            color_code = [int(item) for item in rgb[y,x]]
            color_code.append((key-49))
            data = [color_code]
            with open('color_dataset.csv', 'a', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerows(data)
            print(f'{color}가 {colors[key-49]}로 저장되었습니다.')

def test_event(event, x, y, flags, param):
    global colors
    if event == cv2.EVENT_LBUTTONDOWN:
        newcomer = rgb[y, x]
        with open('color_dataset.csv', 'r') as d:
            color = []
            label = []
            for i in d:
                data = list(i)
                print(data)
            # knn = cv2.ml.KNearest_create()
            # knn.train(color, cv2.ml.ROW_SAMPLE, label)
            # ret, results, neighbours, dist = knn.findNearest(newcomer, 5)
            # print('ret:%s, result:%s, neighbours:%s, distance:%s' \
            #       %(ret, results, neighbours, dist))
            # print(f"해당 색은 {colors[label]}로 추정됩니다.")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    img = frame
    rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    cv2.imshow('camera', img)
    

    key = cv2.waitKey(1) & 0xFF
    if key == 27:
        break
    elif key == ord('l'):
        cv2.setMouseCallback('camera', train_event, img)
    elif key == ord('p'):
        cv2.setMouseCallback('camera', test_event, img)

cap.release()
cv2.destroyAllWindows()