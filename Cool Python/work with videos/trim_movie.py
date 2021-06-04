from moviepy.editor import VideoFileClip

file = VideoFileClip("tik.mp4")
new = file.subclip(t_start=1, t_end=15)
new.write_videofile("new.mp4")