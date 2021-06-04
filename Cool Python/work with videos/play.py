import cv2

cap = cv2.VideoCapture("sample.mp4")
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Can not receive")
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame', gray)
    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()