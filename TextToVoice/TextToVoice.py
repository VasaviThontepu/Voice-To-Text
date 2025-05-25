from gtts import gTTS 
from playsound import playsound
print("=====audio is playing====")
audio ="speech.mp3"
language='en'
voice=gTTS(text="I am Vasavi hailing from the vibrant city of Rajahmundry and Graduated my BTech degree at Aditya University ECE with overall CGPA of 8.64 ",lang=language,slow=True)
voice.save(audio)
playsound(audio)