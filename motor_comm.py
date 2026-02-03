import pyserial


# servo motor
def UpdateRCServo(angle, rc_serial):
    rc_serial.write(f"{angle}\n".encode())
    rc_serial.close()

def UpdateDCMotor():
    pass

def UpdateStepper():
    pass