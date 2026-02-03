import serial
from PyQt5.QtCore import Qt, QSize, QTimer
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QPushButton, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QSpinBox, QFrame
from qtwidgets import AnimatedToggle
from PyQt5.QtGui import QIntValidator
import sys

# motor specific functions
from motor_comm import UpdateRCServo

# Lab 2: Motors - Mechatronic Design (Spring 2026)

# TODO
# need to pass the arduino in as an argument perhaps

# GLOBALS
BAUD_RATE = 9600
TIMEOUT = 0.05
arduino = serial.Serial(port="/dev/cu.usbmodem1101", baudrate=BAUD_RATE, timeout=TIMEOUT)

#### BUTTON CLASSES ####
class UpdateButton(QPushButton):
    def __init__(self, input_widgets = None, send_to_motor_fn = None):
        '''
        UpdateButton initialization
        
        :param input_widgets: list of widgets to read text from
        :param send_to_motor_fn: function that sends data to the motor (define separate functions for each motor and then pass them into this update function)
        '''
        
        super().__init__(text="Update Motor")
        self.clicked.connect(self.OnClick)
        
        self.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border: 1px solid white;
                padding: 10px 20px;
                font-size: 16px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """)
        
        self.inputWidgets = input_widgets or []
        self.send_to_motor_fn = send_to_motor_fn
    
    def OnClick(self):
        update_values = []
        
        # iterate over input widgets
        for widget in self.inputWidgets:
            value = widget.text()
            
            # remove special chars from value
            print(f"Input value: {value}")
            update_values.append(value)
        
        # send to corresponding motor
        if self.send_to_motor_fn:
            self.send_to_motor_fn(update_values)

        return update_values

class ResetButton(QPushButton):
    def __init__(self, reset_fn = None):
        # define a reset function per motor to make things easier (see motor_comm.py)
        
        super().__init__(text="Reset Motor")
        self.clicked.connect(self.OnClick)
        
        self.setStyleSheet("""
            QPushButton {
                background-color: #292929;
                color: white;
                border: 1px solid white;
                padding: 10px 20px;
                font-size: 16px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #171717;
            }
        """)
        
        self.Reset = reset_fn
    
        
    def OnClick(self, Reset):

        if Reset:
            Reset()
            
        print('Reset!')

class SensorToggle(AnimatedToggle):
    def __init__(self):
        super().__init__(checked_color="#FFB000",
            pulse_checked_color="#44FFB000")
        self.setFixedWidth(70)

# extra line
def AddSep():
    line = QFrame()
    line.setFrameShape(QFrame.HLine)
    return line

#### WIDGET CLASSES ####
class RCMotorControls(QWidget):
    # Servo - SG92R TowerPro Micro servo
    
    def __init__(self):
        super().__init__()
        
        layout = QVBoxLayout()
        
        # Page title
        title = QLabel("RC Servo Motor")
        title.setAlignment(Qt.AlignmentFlag.AlignLeft)
        title.setStyleSheet("font-size: 30px;")
        
        # Sensor controls (FOR DISPLAYING SENSOR DATA)
        sensor_layout = QVBoxLayout()
        select_lbl = QLabel("Activate Sensor Controls")
        select_lbl.setAlignment(Qt.AlignmentFlag.AlignLeft)
        select_lbl.setStyleSheet("font-size: 18px;")
        
        toggle = SensorToggle()
        sensor_title = QLabel("Potentiometer Data:")
        self.sensor_value = QLabel("No Reading Detected") # add data from the sensor
        
        sensor_layout.addWidget(select_lbl)
        sensor_layout.addWidget(toggle)
        sensor_layout.addWidget(sensor_title)
        sensor_layout.addWidget(self.sensor_value)
        sensor_layout.setContentsMargins(0, 20, 0, 20) 
        
        # (From Lab) RC servo motor: Move the motor to either of its extreme limit positions and to any position (in degrees) in between. If you choose to use a continuous rotation RC servo, be able to move the motor at any desired velocity (in RPM, rev/sec, degrees/sec, etc.) within the achievable range in either direction.
        
        # Layout for CONTROLS
        controls = QVBoxLayout()
        
        controls_lbl = QLabel("User Controls")
        controls_lbl.setAlignment(Qt.AlignmentFlag.AlignLeft)
        controls_lbl.setStyleSheet("font-size: 18px;")
        
        # GUI Controls
        
        ###### ANGLE SELECT ######
        angle_select_lbl = QLabel("Select Angle (0° to 180°)")
        angle_select_lbl.setAlignment(Qt.AlignmentFlag.AlignLeft)
        angle_select_lbl.setMinimumWidth(400) # keep this constant for all
        
        # spinbox for servo angle
        angle_input = QSpinBox()
        angle_input.setMinimum(0)
        angle_input.setMaximum(180)
        angle_input.setValue(0)
        angle_input.setSuffix('°')
        
        # fill controls
        controls.addWidget(controls_lbl)
        controls.addWidget(angle_select_lbl)
        controls.addWidget(angle_input)
        controls.setContentsMargins(0, 20, 0, 20) 
        
        # add button functionality
        inputs_to_read = [angle_input]
        btn = UpdateButton(inputs_to_read, UpdateRCServo)
        reset_btn = ResetButton()
        
        layout.addWidget(title)
        
        layout.addLayout(sensor_layout)
        layout.addWidget(AddSep())
        layout.addLayout(controls)
        
        layout.addWidget(btn)
        layout.addWidget(reset_btn)
        layout.addStretch()
        
        self.setLayout(layout)
        
    def UpdateValue(self, value):
        self.value_label.setText(f"Latest NNN: {value}")
 
class DCMotorControls(QWidget):
    # mrosnail 280 DC Motor
    
    def __init__(self):
        super().__init__()
        
        layout = QVBoxLayout()
        
        # Page title
        title = QLabel("DC Motor Controls")
        title.setAlignment(Qt.AlignmentFlag.AlignLeft)
        title.setStyleSheet("font-size: 30px;")
        
        # Sensor controls (FOR DISPLAYING SENSOR DATA)
        sensor_layout = QVBoxLayout()
        select_lbl = QLabel("Activate Sensor Controls")
        select_lbl.setAlignment(Qt.AlignmentFlag.AlignLeft)
        select_lbl.setStyleSheet("font-size: 18px;")
        
        toggle = SensorToggle()
        sensor_title = QLabel("Sensor Data:")
        self.sensor_value = QLabel("No Reading Detected") # add data from the sensor
        
        sensor_layout.addWidget(select_lbl)
        sensor_layout.addWidget(toggle)
        sensor_layout.addWidget(sensor_title)
        sensor_layout.addWidget(self.sensor_value)
        sensor_layout.setContentsMargins(0, 20, 0, 20) 
        
        # DC motor: Using an encoder for position feedback and PID control, move the motor a user-selectable a) number of degrees from an initial position and b) desired velocity in either direction.
        
        # Layout for CONTROLS
        controls = QVBoxLayout()
        controls_lbl = QLabel("User Controls")
        controls_lbl.setAlignment(Qt.AlignmentFlag.AlignLeft)
        controls_lbl.setStyleSheet("font-size: 18px;")
        
        ###### SPEED SELECT ######
        speed_select_lbl = QLabel("Select Speed (1-20 rpm)")
        speed_select_lbl.setAlignment(Qt.AlignmentFlag.AlignLeft)
        speed_select_lbl.setMinimumWidth(400) # keep this constant for all
        
        speed_input = QSpinBox()
        speed_input.setMinimum(0)
        speed_input.setMaximum(5)
        speed_input.setValue(0)
        
        # fill controls widget
        controls.addWidget(controls_lbl)
        controls.addWidget(speed_select_lbl)
        controls.addWidget(speed_input)
        controls.setContentsMargins(0, 20, 0, 20)
        
        # add button functionality
        inputs_to_read = [speed_input]
        btn = UpdateButton(inputs_to_read)
        reset_btn = ResetButton()
        
        layout.addWidget(title)
        
        layout.addLayout(sensor_layout)
        layout.addWidget(AddSep())
        layout.addLayout(controls)
        
        layout.addWidget(btn)
        layout.addWidget(reset_btn)
        layout.addStretch()
        
        self.setLayout(layout)
    
    def UpdateValue(self, value):
        self.value_label.setText(f"Latest NNN: {value}")
 
class StepperControls(QWidget):
    # ROHS Step Motor
    # 28BYJ-48 (5V DC)
    def __init__(self):
        super().__init__()
        
        layout = QVBoxLayout()
        
        # Page title
        title = QLabel("Stepper Motor Controls")
        title.setAlignment(Qt.AlignmentFlag.AlignLeft)
        title.setStyleSheet("font-size: 30px;")
        
        # Sensor controls (FOR DISPLAYING SENSOR DATA)
        sensor_layout = QVBoxLayout()
        select_lbl = QLabel("Activate Sensor Controls")
        select_lbl.setAlignment(Qt.AlignmentFlag.AlignLeft)
        select_lbl.setStyleSheet("font-size: 18px;")
        
        toggle = SensorToggle()
        sensor_title = QLabel("Sensor Data:")
        self.sensor_value = QLabel("No Reading Detected") # add data from the sensor
        
        sensor_layout.addWidget(select_lbl)
        sensor_layout.addWidget(toggle)
        sensor_layout.addWidget(sensor_title)
        sensor_layout.addWidget(self.sensor_value)
        sensor_layout.setContentsMargins(0, 20, 0, 20) 
        
        # Stepper motor: Move the motor a user-selectable number of degrees from an initial position in either direction.
        
        # Layout for CONTROLS
        controls = QVBoxLayout()
        controls_lbl = QLabel("User Controls")
        controls_lbl.setAlignment(Qt.AlignmentFlag.AlignLeft)
        controls_lbl.setStyleSheet("font-size: 18px;")
        
        ###### ANGLE SELECT ######
        angle_select_lbl = QLabel("Select Angle")
        angle_select_lbl.setAlignment(Qt.AlignmentFlag.AlignLeft)
        angle_select_lbl.setMinimumWidth(400) # keep this constant for all
        
        # spinbox for servo angle
        angle_input = QSpinBox()
        angle_input.setMinimum(-360)
        angle_input.setMaximum(360)
        angle_input.setValue(0)
        angle_input.setSuffix('°')
        
        # fill controls
        controls.addWidget(controls_lbl)
        controls.addWidget(angle_select_lbl)
        controls.addWidget(angle_input)
        controls.setContentsMargins(0, 20, 0, 20) 
        
        # add button functionality
        inputs = [angle_input]
        btn = UpdateButton(inputs)
        reset_btn = ResetButton()
        
        # add all items to layout
        layout.addWidget(title)
        
        layout.addLayout(sensor_layout)
        layout.addWidget(AddSep())
        layout.addLayout(controls)
        
        layout.addWidget(btn)
        layout.addWidget(reset_btn)
        layout.addStretch()
        
        self.setLayout(layout)
        
    def UpdateValue(self, value):
        self.value_label.setText(f"Latest NNN: {value}")
       
# design the main window
class MainInterface(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # global gui things
        self.setMinimumSize(QSize(800, 800))
        self.setWindowTitle("Lab 02 - Motors")
        global_title = QLabel("Lab 2 Sensors (Group 7)")
        global_title.setStyleSheet("font-size: 30px;")
        
        # define widgets
        self.rc_ctrl = RCMotorControls()
        self.dc_ctrl = DCMotorControls()
        self.stepper_ctrl = StepperControls()
        
        # motor controls
        motors_layout = QHBoxLayout()
        
        # set controllers
        motors_layout.addWidget(self.rc_ctrl)
        motors_layout.addWidget(self.dc_ctrl)
        motors_layout.addWidget(self.stepper_ctrl)
        
        # set central widget and layout
        central_widget = QWidget()
        main_layout = QVBoxLayout()
        
        main_layout.addWidget(global_title)
        
        main_layout.addLayout(motors_layout)
        main_layout.addStretch()
        
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)
        
        # poll sensor readings
        self.serial_timer = QTimer(self)
        self.serial_timer.setInterval(50)
        self.serial_timer.timeout.connect(self.PollSensors)
        self.serial_timer.start()

    def PollSensors(self):
        # string parsing to get sensor data
        try:
            line = arduino.readline().decode("utf-8", errors="ignore").strip()
        except serial.SerialException:
            return

        if not line:
            return

        # arduino outputs (distance,humidity,temperature,light)
        parts = [p.strip() for p in line.split(",")]

        # parse the string
        potent, light, dist = parts[0], parts[1], parts[2]
        
        # update sensor values
        self.rc_ctrl.UpdateValue(potent)
        self.dc_ctrl.UpdateValue(light)
        self.stepper_ctrl.UpdateValue(dist)
        
# run the app
if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainInterface()
    window.show()

    app.exec()


        
        
        
        
        
        
        
