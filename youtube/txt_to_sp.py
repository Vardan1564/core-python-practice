from gtts import gTTS
import os
from playsound import playsound


txt=input("ENTER SPEECH YOU WANT IT : ")
# lan e ak obj che je ma language nakhi che 
lan="en"

out=gTTS(text=txt ,lang=lan,slow=False)

out.save("myspeech1.mp3")
playsound("myspeech1.mp3")