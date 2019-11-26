import sys
from numpy import arange,sign
import matplotlib.pyplot as plt
from random import random


class Vehicle_Dynamics:
    def __init__(self):
        self.error_accum = 0
        self.previous_error = 0

    def vehicle_motion(self, position, velocity, dt, desired, kp, kd, ki, noise_mag):
        global error_accum,previous_error,previous_t
        m = 1000 # mass of car in kg
        mu = 0.2 # friction coefficient for tires
        g = 9.8 # gravity
        area = 2 # cross-sectional area of car
        c = .2 # drag coefficient
        rho = 1.3 # air density

        x = position
        xd = velocity

        error = desired - x
        self.error_accum += error*dt
        integral = self.error_accum

        if dt != 0:
            derivative = (error - self.previous_error)/dt
        else:
            derivative = 0.0
        derivative = max(min(derivative,10.0),-10.0)
        self.previous_error = error

        control = kp*error + kd*derivative + ki*integral # acceleration from engine

        control = max(min(control,10.0),-10.0)

        print("Error =",error)

        # a = engine acceleration - friction - drag
        xdd = control - sign(xd)*(mu*g + (c*rho*area*xd*xd)/(2*m)) + noise_mag*random()

        return xdd


if __name__ == "__main__":
    velocity = 0.0
    position = 0.0
    dt = 0.001
    noise_mag = 0.0

    desired = 30
    kp = 1.0
    kd = 0.0
    ki = 0.0

    total_time = 100.0


    for a in sys.argv[1:]:
        if "kp" in a:
            kp = float(a.split('=')[1])
        elif "kd" in a:
            kd = float(a.split('=')[1])
        elif "ki" in a:
            ki = float(a.split('=')[1])
        elif "time" in a:
            total_time = float(a.split('=')[1])
        elif "desired" in a:
            desired = float(a.split('=')[1])
        elif "p0" in a:
            position = float(a.split('=')[1])
        elif "v0" in a:
            velocity = float(a.split('=')[1])
        elif "noise" in a:
            noise_mag = float(a.split('=')[1])
        else:
            print("Usage: %s <options>" % sys.argv[0])
            print("Options:")
            print("    kp=1.0 - set kp")
            print("    kd=0.0 - set kd")
            print("    ki=0.0 - set ki")
            print("    time=100.0 - set time for simulation to run")
            print("    desired=30 - set desired position")
            print("    p0=0.0 - set initial position")
            print("    v0=0.0 - set initial velocity")
            print("    noise=0.0 - set the noise multiplier")
            exit()








    time_range = arange(0.0, total_time, dt)


    output = []
    vd = Vehicle_Dynamics()

    for t in time_range:
        output.append([desired,position,velocity])
        velocity += dt*vd.vehicle_motion(position, velocity, dt, desired, kp, kd, ki, noise_mag)
        position += velocity * dt


    plt.plot(time_range, output)
    plt.xlabel('TIME (sec)')
    plt.ylabel('Position m')
    plt.title('Vehicle Motion')
    plt.legend(('$x_d$ (m)', '$x$ (m)', '$\dot{x}$ (m/s)'))
    plt.show()
