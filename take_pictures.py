# OPENCV CAPTURE VIDEO FROM CAMERA USING OPENCV

import cv2
import numpy

webcam = cv2.VideoCapture(0)  # 0 denotes default laptop webcam

img_saved = 0
num_pics = 51

while True:
    ret, frame = webcam.read()  # return

    if ret:
        cv2.imshow("Samarth_Video", frame)
        key = cv2.waitKey(1)  # wait 1 ms

        if img_saved < num_pics:
            cv2.imwrite(f"PiCamera Data\\img\\captured_frame{img_saved}.jpg", frame)
        img_saved += 1
        if key == ord("q"):  # q is quit
            break  # when user presses q, while loop breaks

webcam.release()
cv2.destroyAllWindows()



