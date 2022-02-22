from flask import Blueprint
from flask import request
import random

auth = Blueprint('auth', __name__)

Speed = 0

@auth.route('/setSpeed', methods=['POST'])
def setspeed():
    global Speed
    Speed = request.json["speed"]
    return {"speed": Speed}

@auth.route('/getSpeed')
def getspeed():
    return{"speed": Speed}

Temperature = 20

@auth.route ('/setTemperature', methods=['POST'])
def setTemp():
    global Temperature
    Temperature = request.json["temperature"]
    return {"temperature": Temperature}

@auth.route ('/getTemperature')
def getTemp ():
    return {"temperature": Temperature}

Angle = 10

@auth.route ('/setAngle', methods=['POST'])
def setAngle ():
    global Angle
    Angle = request.json["angle"]
    return {"angle": Angle}

@auth.route ('/getAngle')
def getAngle ():
    return {"angle": Angle}

Engspeed = 0

@auth.route ('/getRpm')
def getEng ():
    return {"engine_speed": Speed / 2}

lightsetting = [True, False]

lightsetting = False

@auth.route ('/setLightStatus', methods=['POST'])
def setLights():
    global Lights
    Lights = request.json["lights"]
    return {"lights": Lights}

@auth.route ('/getLightStatus')
def getLights():
    return {"lights": Lights}