from moviepy.editor import VideoFileClip, concatenate_videoclips
clip1 = VideoFileClip("sample.mp4")
clip2 = VideoFileClip("new.mp4").subclip(10, 13)
clip3 = VideoFileClip("tik.mp4")
final_clip = concatenate_videoclips([clip1, clip2, clip3])
final_clip.write_videofile("mixed.mp4")