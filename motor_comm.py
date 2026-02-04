import serial

# Functions for motor updates
# Group 7 Mechatronic Design

def SetGUIMode(serial=None):
    if serial:
        serial.write(b"M1\n")

def SetSensorMode(serial=None):
    if serial:
        serial.write(b"M0\n")

# Update functions
def UpdateRCServo(angle, serial=None):
    # strip string and convert to int
    angle = angle[0]
    format_ang = ''.join(c for c in angle if c.isdigit())
    format_ang = int(format_ang)
    
    print("ANGLE", format_ang)
    
    # add S to string for RC
    if serial:
        serial.write(f"S{format_ang}\n".encode())
        
def UpdateDCMotor(speed, serial=None):
    speed = speed[0]
    format_sp = int(speed)
    print("SPEED", format_sp)
    
    # use D for DC motor
    if serial:
        serial.write(f"D{format_sp}\n".encode())

def UpdateStepper(steps, serial=None):
    steps = steps[0]
    format_steps = int(steps)
    print("STEPS", format_steps)
    
    if serial:
        serial.write(f"T{format_steps}\n".encode())

# Reset Functions
def ResetDCMotor():
    print("Resetting DC Motor")
    pass

