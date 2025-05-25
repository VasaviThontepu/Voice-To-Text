from gtts import gTTS 
from playsound import playsound
print("=====audio is playing====")
audio ="speech.mp3"
language='en'
voice=gTTS(text="my name is vasavi",lang=language,slow=False)
voice.save(audio)
playsound(audio)