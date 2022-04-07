import time
import RPi.GPIO as GPIO

in1 = 16
in2 = 18
in3 = 22
in4 = 24
pwm1 = 33
pwm2 = 32

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)
GPIO.setup(in3, GPIO.OUT)
GPIO.setup(in4, GPIO.OUT)
GPIO.setup(pwm1, GPIO.OUT)
GPIO.setup(pwm2, GPIO.OUT)
    
pwm_1 = GPIO.PWM(pwm1, 100)
pwm_2 = GPIO.PWM(pwm2 , 100)

def getting_info():
    motor_num = int(input("1. první motor\n2. druhý motor\nZadejte číslo motoru chcete spustit: "))
    motor_direction = int(input("1. dopředu\n2. dozadu\nZadejte směr vlaku: "))
    motor_intensity = int(input("Zadejte jakou intenzitou motor pojede (v %): "))
    
    if (motor_intensity > 100):
        motor_intensity = 100
    elif (motor_intensity < 0):
        motor_intensity = 0
    
    return motor_num, motor_direction, motor_intensity

def set(motor_num, motor_direction, motor_intensity):
    if (motor_num == 1 and motor_direction == 1):
        GPIO.output(in1, GPIO.LOW)
        GPIO.output(in2, GPIO.HIGH)
        GPIO.output(in3, GPIO.LOW)
        GPIO.output(in4, GPIO.LOW)
    
    elif (motor_num == 1 and motor_direction == 2):
        GPIO.output(in1, GPIO.HIGH)
        GPIO.output(in2, GPIO.LOW)
        GPIO.output(in3, GPIO.LOW)
        GPIO.output(in4, GPIO.LOW)
        
    elif (motor_num == 2 and motor_direction == 1):
        GPIO.output(in1, GPIO.LOW)
        GPIO.output(in2, GPIO.LOW)
        GPIO.output(in3, GPIO.LOW)
        GPIO.output(in4, GPIO.HIGH)
    
    elif (motor_num == 2 and motor_direction == 2):
        GPIO.output(in1, GPIO.LOW)
        GPIO.output(in2, GPIO.LOW)
        GPIO.output(in3, GPIO.HIGH)
        GPIO.output(in4, GPIO.LOW)
        
    else:
        print("Error!")
    
    pwm_1.start(motor_intensity)
    pwm_2.start(motor_intensity)
        
def turn_down():
    GPIO.output(in1, GPIO.LOW)
    GPIO.output(in2, GPIO.LOW)
    GPIO.output(in3, GPIO.LOW)
    GPIO.output(in4, GPIO.LOW)
    

motor_num, motor_direction, motor_intensity = getting_info()
set(motor_num, motor_direction, motor_intensity)

while True:
    x = input("Napište c pro vypnutí motorů: ")
    if x == "c":
        break
    
turn_down()

    
