import cv2 as cv
import os

VIDEO_PATH = "./data/CutGrandprix.mp4"
OUTPUT_DIR = "./data/img/"
DELTA_TIME = 2

# Clear or create output directory
if os.path.exists(OUTPUT_DIR):
    for f in os.listdir(OUTPUT_DIR):
        os.remove(os.path.join(OUTPUT_DIR, f))
else:
    os.mkdir(OUTPUT_DIR)

cap = cv.VideoCapture(VIDEO_PATH)

# Calculate frame interval based on the FPS and DELTA_TIME
fps = cap.get(cv.CAP_PROP_FPS)
frame_interval = int(fps * DELTA_TIME)
frame_count = 0

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    # Capture a frame every 'frame_interval' frames
    if frame_count % frame_interval == 0:
        output_filename = os.path.join(OUTPUT_DIR, f"frame_{frame_count}.png")
        cv.imwrite(output_filename, frame)

    frame_count += 1

cap.release()
cv.destroyAllWindows()