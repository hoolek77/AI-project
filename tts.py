import speake3

def speak(phrase):
    engine = speake3.Speake()
    engine.set('voice', 'en')
    engine.set('speed', '107')
    engine.set('pitch', '99')
    engine.say(phrase)
    engine.talkback()
