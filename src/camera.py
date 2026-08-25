import cv2
camera = cv2.VideoCapture(1) #camera
if not camera.isOpened():
    print("Error: Could not open camera.")
    raise SystemExit
else:
    print("Camera opened successfully. Press 'q' to quit.")

while True:
    success, frame = camera.read()
    if not success:
        print("Error: Could not read frame from camera.")
        break

    frame = cv2.flip(frame, 1) # Flip the frame horizontally
    cv2.imshow("Camera Feed", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()
