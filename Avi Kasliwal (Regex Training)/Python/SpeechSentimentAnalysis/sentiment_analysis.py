import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
from textblob import TextBlob
import flair

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)

def speak(sent):
    engine.say(sent)
    engine.runAndWait()

def listen():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query


if __name__ == "__main__":
    sent = listen()
    speak(f"input sentence is : {sent}")
    speak("Sentiment of the sentence according to textblob is ...")
    speak(TextBlob(sent).sentiment.polarity)
    flair_sentiment = flair.models.TextClassifier.load('en-sentiment')
    s = flair.data.Sentence(sent)
    flair_sentiment.predict(s)
    total_sentiment = s.labels
    speak("Sentiment of the sentence according to flair is ...")
    speak(total_sentiment)