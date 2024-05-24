from gtts import gTTS
import os
text = 'sopiii cute'
tss = gTTS(text=text, lang='id' )
tss.save('selamatSore.mp3')
os.system('start selamatSore.mp3')