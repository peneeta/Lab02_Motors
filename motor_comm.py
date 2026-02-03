import serial

# DEFINE GLOBAL MOTOR THINGS HERE
rc_serial = "tbd"

# Update functions
def UpdateRCServo(angle, rc_serial=None):
    # strip string and convert to int
    angle = angle[0]
    format_ang = ''.join(c for c in angle if c.isdigit())
    format_ang = int(format_ang)
    
    print("FORMATTED ANGLE", format_ang)
    
    if rc_serial:
        rc_serial.write(f"{format_ang}\n".encode())
        rc_serial.close()
        

def UpdateDCMotor():
    pass

def UpdateStepper():
    pass

# Reset Functions
def RCServoReset():
    angle = 0
    
    # rc_serial.write(f"{angle}\n".encode())
    pass

def DCServoReset():
    pass

def StepperReset():
    pass