import moviepy.editor as mpy
from moviepy.video.fx.all import crop

clip = mpy.VideoFileClip("tik.mp4")
(w, h) = clip.size
cropped_clip = crop(clip, width=320, height=320, x_center=w/2, y_center=h/2)
cropped_clip.write_videofile('cropped.mp4')