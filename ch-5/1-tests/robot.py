# Write your code here :-)
import board
import digitalio

motor_A1 = digitalio.DigitalInOut(board.GP17)
motor_A2 = digitalio.DigitalInOut(board.GP16)
motor_B1 = digitalio.DigitalInOut(board.GP18)
motor_B2 = digitalio.DigitalInOut(board.GP19)

motor_A1.direction = digitalio.Direction.OUTPUT
motor_A2.direction = digitalio.Direction.OUTPUT
motor_B1.direction = digitalio.Direction.OUTPUT
motor_B2.direction = digitalio.Direction.OUTPUT

def stop():
    motor_A1.value = False
    motor_A2.value = False
    motor_B1.value = False
    motor_B2.value = False
