from flask import Blueprint
import random

auth = Blueprint('auth', __name__)

@auth.route('/speed')
def speed():
    Speed = random.randint(1,10)
    return {"speed": Speed}

@auth.route ('/temperature')
def temperature():
    Temperature = random.uniform(0,200)
    return {"temperature": Temperature}

lightsetting = ['on', 'off']

@auth.route ('/lights')
def lights():
    Lights = random.choice(lightsetting)
    return {"lights": Lights}