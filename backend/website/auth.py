from flask import Blueprint
import random

auth = Blueprint('auth', __name__)

@auth.route('/setSpeed')
def setspeed():
    global Speed
    Speed = random.randint(1,10)
    return {"speed": Speed}

@auth.route('/getSpeed')
def getspeed():
    return{"speed": Speed}

Temperature = 0

@auth.route ('/setTemperature')
def setTemp():
    global Temperature
    Temperature = random.uniform(0,200)
    return {"temperature": Temperature}

@auth.route ('/getTemperature')
def getTemp ():
    return {"temperature": Temperature}

@auth.route ('/setAngle')
def setAngle ():
    global Angle
    Angle = random.randint(0,180)
    return {"angle": Angle}

@auth.route ('/getAngle')
def getAngle ():
    return {"angle": Angle}

@auth.route ('/setEngspeed')
def setEng ():
    global Engspeed
    Engspeed = random.randint(0,5000)
    return {"engine_speed": Engspeed}

@auth.route ('/getEngspeed')
def getEng ():
    return {"engine_speed": Engspeed}

lightsetting = [True, False]

@auth.route ('/setLightStatus')
def lights():
    global Lights
    Lights = random.choice(lightsetting)
    return {"lights": Lights}

@auth.route ('/getLightStatus')
def getLights():
    return {"lights": Lights}

radiosetting = [True, False]

@auth.route ('/setRadioStatus')
def setRadio():
    global Radio
    Radio = random.choice(radiosetting)
    return {"radio": Radio}

@auth.route ('/getRadioStatus')
def getRadio():
    return {"radio": Radio}
