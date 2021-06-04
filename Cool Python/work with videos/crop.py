import cv2

top, right, bottom, left = 0, 450, 360, 0  # Sample values.


input_video = cv2.VideoCapture('tik.mp4')

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
output_movie = cv2.VideoWriter('output.mp4', fourcc, 30, (450, 360))

while True:
    ret, frame = input_video.read()

    if not ret:
        break

    # Following crop assumes the video is colored, 
    # in case it's Grayscale, you may use: crop_img = frame[top:bottom, left:right]  
    crop_img = frame[top:bottom, left:right]

    output_movie.write(crop_img)


# Closes the video writer.
output_movie.release()