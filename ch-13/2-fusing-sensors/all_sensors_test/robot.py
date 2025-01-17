import board
import pwmio
import pio_encoder
import busio
import adafruit_vl53l1x
import adafruit_bno055


motor_A1 = pwmio.PWMOut(board.GP17)
motor_A2 = pwmio.PWMOut(board.GP16)
motor_B1 = pwmio.PWMOut(board.GP18)
motor_B2 = pwmio.PWMOut(board.GP19)

right_motor = motor_A1, motor_A2
left_motor = motor_B1, motor_B2

right_encoder = pio_encoder.QuadratureEncoder(board.GP20, board.GP21, reversed=True)
left_encoder = pio_encoder.QuadratureEncoder(board.GP26, board.GP27)

i2c0 = busio.I2C(sda=board.GP0, scl=board.GP1)
# i2c1 = busio.I2C(sda=board.GP2, scl=board.GP3)

# right_distance = adafruit_vl53l1x.VL53L1X(i2c0)
# left_distance = adafruit_vl53l1x.VL53L1X(i2c1)

imu = adafruit_bno055.BNO055_I2C(i2c0)

def stop():
    motor_A1.duty_cycle = 0
    motor_A2.duty_cycle = 0
    motor_B1.duty_cycle = 0
    motor_B2.duty_cycle = 0


def set_speed(motor, speed):
    # Swap motor pins if we reverse the speed
    if speed < 0:
        direction = motor[1], motor[0]
        speed = -speed
    else:
        direction = motor
    speed = min(speed, 1)  # limit to 1.0
    max_speed = 2 ** 16 - 1

    direction[0].duty_cycle = int(max_speed * speed)
    direction[1].duty_cycle = 0


def set_left(speed):
    set_speed(left_motor, speed)


def set_right(speed):
    set_speed(right_motor, speed)
