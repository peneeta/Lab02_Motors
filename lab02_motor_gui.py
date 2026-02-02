import serial
from PyQt6.QtCore import Qt, QSize, QTimer
from PyQt6.QtWidgets import QWidget, QApplication, QMainWindow, QPushButton, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit
from PyQt6.QtGui import QIntValidator
import sys

# Lab 2: Motors - Mechatronic Design (Spring 2026)

# arduino = serial.Serial(port="/dev/cu.usbmodem1101", baudrate=9600, timeout=0.05)

class UpdateButton(QPushButton):
    def __init__(self):
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
    
        
    def OnClick(self):
        
        # TODO send to corresponding motor
        print('Button clicked!')

class ResetButton(QPushButton):
    def __init__(self):
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
    
        
    def OnClick(self):
        
        # TODO send to corresponding motor
        print('Reset!')
  
        
class StopAllMotorsButton(QPushButton):
    def __init__(self):
        super().__init__(text="Stop Motors")
        self.clicked.connect(self.OnClick)
        
        self.setStyleSheet("""
            QPushButton {
                background-color: #eb4034;
                color: white;
                border: none;
                padding: 10px 20px;
                font-size: 16px;
                border-radius: 5px;
                max-width: 100px;
            }
            QPushButton:hover {
                background-color: #99221a;
            }
        """)
    
        
    def OnClick(self):
        
        # TODO send to corresponding motor
        print('STOP!')

class RCMotorControls(QWidget):
    def __init__(self):
        super().__init__()
        
        layout = QVBoxLayout()
        btn = UpdateButton()
        
        # Page title
        title = QLabel("RC Motor Controls")
        title.setAlignment(Qt.AlignmentFlag.AlignLeft)
        title.setStyleSheet("font-size: 20px;")
        
        # (From Lab) RC servo motor: Move the motor to either of its extreme limit positions and to any position (in degrees) in between. If you choose to use a continuous rotation RC servo, be able to move the motor at any desired velocity (in RPM, rev/sec, degrees/sec, etc.) within the achievable range in either direction.
        
        graph_placeholder = QLabel("fhdsjkfhjdskhfjdsk")
        graph_placeholder.setAlignment(Qt.AlignmentFlag.AlignLeft)
        graph_placeholder.setStyleSheet("border: 2px dashed gray; background-color: #000000")
        graph_placeholder.setMinimumSize(400, 250)
        
        layout.addWidget(title)
        layout.addWidget(graph_placeholder)
        layout.addWidget(btn)
        layout.addStretch()
        
        self.setLayout(layout)
        
class DCMotorControls(QWidget):
    def __init__(self):
        super().__init__()
        
        layout = QVBoxLayout()
        btn = UpdateButton()
        
        # Page title
        title = QLabel("DC Motor Controls")
        title.setAlignment(Qt.AlignmentFlag.AlignLeft)
        title.setStyleSheet("font-size: 20px;")
        
        # DC motor: Using an encoder for position feedback and PID control, move the motor a user-selectable a) number of degrees from an initial position and b) desired velocity in either direction.
        graph_placeholder = QLabel("fhdsjkfhjdskhfjdsk")
        graph_placeholder.setAlignment(Qt.AlignmentFlag.AlignLeft)
        graph_placeholder.setStyleSheet("border: 2px dashed gray; background-color: #ffe6e6;")
        graph_placeholder.setMinimumSize(400, 250)
        
        layout.addWidget(title)
        layout.addWidget(graph_placeholder)
        layout.addWidget(btn)
        layout.addStretch()
        
        self.setLayout(layout)
        
class StepperControls(QWidget):
    def __init__(self):
        super().__init__()
        
        layout = QVBoxLayout()
        btn = UpdateButton()
        reset_btn = ResetButton()
        
        # Page title
        title = QLabel("Stepper Motor Controls")
        title.setAlignment(Qt.AlignmentFlag.AlignLeft)
        title.setStyleSheet("font-size: 20px;")
        
        # Stepper motor: Move the motor a user-selectable number of degrees from an initial position in either direction.
        
        # Layout for CONTROLS
        controls = QVBoxLayout()
        
        ###### ANGLE SELECT ######
        angle_select_lbl = QLabel("Select Angle (0° to 360°)")
        angle_select_lbl.setAlignment(Qt.AlignmentFlag.AlignLeft)
        angle_select_lbl.setMinimumWidth(400) # keep this constant for all
        
        angle_input = QLineEdit()
        validator = QIntValidator(0, 360)  # Min 0, Max 360
        angle_input.setValidator(validator)
        angle_input.setPlaceholderText("Enter angle in degrees")
        

        # fill controls
        controls.addWidget(angle_select_lbl)
        controls.addWidget(angle_input)
        
        layout.addWidget(title)
        layout.addLayout(controls)
        layout.addWidget(btn)
        layout.addWidget(reset_btn)
        layout.addStretch()
        
        self.setLayout(layout)

        
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
        
        # define global controls
        stop_btn = StopAllMotorsButton()
        
        # set central widget and layout
        central_widget = QWidget()
        main_layout = QVBoxLayout()
        
        main_layout.addWidget(global_title)
        main_layout.addWidget(stop_btn)
        
        main_layout.addLayout(motors_layout)
        main_layout.addStretch()
        
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)
        
        # self.serial_timer = QTimer(self)
        # self.serial_timer.setInterval(50)
        # self.serial_timer.timeout.connect(self.poll_serial)
        # self.serial_timer.start()

    # def poll_serial(self):
    #     try:
    #         line = arduino.readline().decode("utf-8", errors="ignore").strip()
    #     except serial.SerialException:
    #         return

    #     if not line:
    #         return

    #     # arduino outputs (distance,humidity,temperature,light)
    #     parts = [p.strip() for p in line.split(",")]
    #     if len(parts) < 4:
    #         return

    #     distance, humidity, temperature, light = parts[0], parts[1], parts[2], parts[3]
    #     self.s1_page.update_value(distance)
    #     self.s2_page.update_value(temperature, humidity)
    #     self.s3_page.update_value(light)
        

# run the app
if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainInterface()
    window.show()

    app.exec()


        
        
        
        
        
        
        
