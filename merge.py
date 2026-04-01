from moviepy.editor import *

video = VideoFileClip("media/videos/animation/480p15/StoryScene.mp4")
audio = AudioFileClip("voice.mp3")

final = video.set_audio(audio)
final.write_videofile("final_video.mp4")

print("Final video created")
