import cv2

source = 'race_car.mp4'
cap = cv2.VideoCapture(source)

if not cap.isOpened():
    print("Error: Could not open video.")
    
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

# Ensure the codec is correct
out_avi = cv2.VideoWriter("race_car_out.avi", cv2.VideoWriter_fourcc("M", "J", "P", "G"), 10, (frame_width, frame_height))
out_mp4 = cv2.VideoWriter("race_car_out.mp4", cv2.VideoWriter_fourcc(*"XVID"), 10, (frame_width, frame_height))

while cap.isOpened():
    ret, frame = cap.read()

    if ret:
        out_avi.write(frame)
        out_mp4.write(frame)
    else:
        break

cap.release()
out_avi.release()
out_mp4.release()
