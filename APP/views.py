from django.shortcuts import render
import pyttsx3
# Create your views here.
def Speed(engine, speed):
    if speed == 'slow':
        engine.setProperty('rate', 100)
    elif speed == 'medium':
        engine.setProperty('rate', 150)
    elif speed == 'fast':
        engine.setProperty('rate', 200)

def index(request):
    if request.method=="POST":
        text=request.POST["text"]
        speed=request.POST["speed"]
        voice=request.POST["speaker"]
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        if voice=='male':
            engine.setProperty('voice', voices[0].id)
        elif voice=='female':
            engine.setProperty('voice',voices[1].id)
        Speed(engine, speed)
        engine.say(text)
        engine.runAndWait()

    return render(request,'index.htm')