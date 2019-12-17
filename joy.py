import pygame
import serial

def quad2omni(vel):
    m1 = -vel[0]
    m2 = (vel[0]*0.5 + vel[1]*0.8660254038)
    m3 = (vel[0]*0.5 - vel[1]*0.8660254038)
    mx = max([abs(v) for v in [m1,m2,m3]])
    out = []
    if mx > 1:
        out = [int(v/mx*127+128) for v in [m1,m2,m3]]
    else :
        out = [int(v*127+128) for v in [m1,m2,m3]]
    print(out)
    return bytearray(out)
def drone_transmit(j):
    return bytearray([int(-j*255)])

pygame.init()

ser = serial.Serial(port = 'COM13',baudrate =57600,timeout = 100)

clock = pygame.time.Clock()

pygame.joystick.init()

while True:
    pygame.event.get()

    joystick = pygame.joystick.Joystick(0)
    joystick.init()

    ser.write(drone_transmit(joystick.get_axis(2)))
##    vel = [joystick.get_axis(4),joystick.get_axis(3)]
##    ser.write(quad2omni(vel))
    clock.tick(60)

pygame.quit()
