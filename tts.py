import speake3

engine = speake3.Speake()
engine.set('voice', 'pl')
engine.set('speed', '107')
engine.set('pitch', '99')
engine.say("Hello world!")
engine.talkback()