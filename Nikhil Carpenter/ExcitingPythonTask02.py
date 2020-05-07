import speech_recognition as s_r
from textblob import TextBlob

print(s_r.__version__)
r = s_r.Recognizer()
my_mic = s_r.Microphone(device_index=1)
try:    
    with my_mic as source:
        print("Say now!!!!")
        audio = r.listen(source)
    print(r.recognize_google(audio))
except:
    print("not getting")  
 
blob = TextBlob(r.recognize_google(audio))

if blob.sentiment.polarity < 0:
	print("your words seems Negative")
elif blob.sentiment.polarity > 0:
	print("your words seems Good")
else:
        print("your words seems Normal")    