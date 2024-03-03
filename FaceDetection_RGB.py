import cv2
from cvzone.FaceDetectionModule import FaceDetector
from cvzone.SerialModule import SerialObject
from time import sleep

cap = cv2.VideoCapture(0) # 0 for camera nb 0
detector = FaceDetector(minDetectionCon=0.9)
arduino = SerialObject("COM7")

running = True  # Flag to indicate if the program is running

def send_data(data):
    arduino.sendData(data)

try:
    while running:
        success, img = cap.read()
        img, bboxs = detector.findFaces(img)

        if bboxs:  # If there is a face in the box
            send_data([1, 0, 0])
        else:
            arduino.sendData([0, 1, 0])
            sleep(1)
            arduino.sendData([0, 0, 1])
            sleep(1)

        cv2.imshow("Say Hi", img) # Display the image
        if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to quit
            running = False

except KeyboardInterrupt:
    print("Exiting program")

finally:
    send_data([0, 0, 0])  # Send [0, 0, 0] before exiting
    cap.release()
    cv2.destroyAllWindows()
