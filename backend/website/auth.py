from flask import Blueprint
import random

auth = Blueprint('auth', __name__)

Speed = 0

@auth.route('/setSpeed')
def setspeed():
    global Speed
    Speed = random.randint(1,10)
    return {"speed": Speed}

@auth.route('/getSpeed')
def getspeed():
    return{"speed": Speed}

Brake = 0

@auth.route('/setBrake')
def setbrake():
    global Brake
    Brake = random.randint(1,10)
    return {"brake": Brake}

@auth.route('/getBrake')
def getbrake():
    return {"brake": Brake}

@auth.route ('/Speed')
def speed():
    setspeed()
    getspeed()
    setbrake()
    getbrake()
    global speedb
    speedb = Speed - Brake
    return {"speed": speedb}

@auth.route ('/S')
def s():
    getspeed()
    getbrake()
    global Sp
    Sp = Speed - Brake
    return {"speed": Sp}

Temperature = 0

@auth.route ('/setTemperature')
def setTemp():
    global Temperature
    Temperature = random.uniform(0,200)
    return {"temperature": Temperature}

@auth.route ('/getTemperature')
def getTemp ():
    return {"temperature": Temperature}

Angle = 0

@auth.route ('/setAngle')
def setAngle ():
    global Angle
    Angle = random.randint(0,180)
    return {"angle": Angle}

@auth.route ('/getAngle')
def getAngle ():
    return {"angle": Angle}

Engspeed = 0

@auth.route ('/setEngspeed')
def setEng ():
    global Engspeed
    Engspeed = random.randint(0,5000)
    return {"engine_speed": Engspeed}

@auth.route ('/getEngspeed')
def getEng ():
    return {"engine_speed": Engspeed}

lightsetting = [True, False]

lightsetting = False

@auth.route ('/setLightStatus')
def setLights():
    global Lights
    Lights = random.choice(lightsetting)
    return {"lights": Lights}

@auth.route ('/getLightStatus')
def getLights():
    return {"lights": Lights}

radiosetting = [True, False]

radiosetting = False

@auth.route ('/setRadioStatus')
def setRadio():
    global Radio
    Radio = random.choice(radiosetting)
    return {"radio": Radio}

@auth.route ('/getRadioStatus')
def getRadio():
    return {"radio": Radio}
