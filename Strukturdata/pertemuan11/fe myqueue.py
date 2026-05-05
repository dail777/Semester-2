import gtts
import playsound
#contoh penggunaan gtts untuk membuat file audio dari teks
text = "Hello, this is a test of the gtts library."
tts = gtts.gTTS(text, lang='id')   
tts.save("test.mp3")

#play the audio file
playsound.playsound("test.mp3")



