from flask import Flask
from flask_ask import Ask, statement, convert_errors
import logging

app = Flask(__name__)
ask = Ask(app, '/')
app.config['ASK_VERIFY_REQUESTS'] = False
@ask.intent('Help', mapping={'guide': 'guide'})
def help(guide):
    if guide in ['help', 'guide', 'assist']: return statement('To turn on the light or ask the room temperature, say: Alexa, Ask home light on. Or: Alexa, Ask home room temperature')
    if (guide == "developer"): return statement('This skill has been developed by Mr Jeevesh Awal of Tech maniacs Edu services. I hope you liked the skill.')
    if(guide == "welcome"): return statement('Hello friends. Welcome to IIT BHU, my name is Alexa. A natural Language Understanding system developed by Amazon and customised for this skill at Tech maniacs Edu services. I wish you all the very best for your workshop ahead. I hope you\'ll enjoy.')
    return statement('Sorry! I didnt understand.')
