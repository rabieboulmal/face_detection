import cv2
import os
import subprocess


def shot(fname):
    
    cam = cv2.VideoCapture(0)
    
    os.system(f"mkdir -p ./dataset/{fname}/")

    cv2.namedWindow("press space to take a photo", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("press space to take a photo", 500, 300)

    img_counter = 0
    img_name=""
    while True:
        ret, frame = cam.read()
        if not ret:
            print("failed to grab frame")
            break
        cv2.imshow("press space to take a photo", frame)

        k = cv2.waitKey(1)
        if k%256 == 27:
            # ESC pressed
            print("Escape hit, closing...")
            break
        elif k%256 == 32:
            # SPACE pressed
            img_name = f"dataset/{fname}/image_{img_counter}.jpg"
            cv2.imwrite(img_name, frame)
            print("{} written!".format(img_name))
            img_counter += 1
        

    cam.release()

    cv2.destroyAllWindows()