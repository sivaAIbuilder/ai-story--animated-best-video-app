from gtts import gTTS

with open("script.txt", "r") as file:
    text = file.read()

tts = gTTS(text)
tts.save("voice.mp3")

print("Voice created")
