import serial
from PyQt6.QtCore import Qt, QSize, QTimer
from PyQt6.QtWidgets import QWidget, QApplication, QMainWindow, QPushButton, QVBoxLayout, QHBoxLayout, QLabel, QStackedWidget
import sys

# Lab 2: Motors - Mechatronic Design (Spring 2026)

# TODO Update for motors lab

# arduino = serial.Serial(port="/dev/cu.usbmodem1101", baudrate=9600, timeout=0.05)

# design the sidebar to pick sensors
class Sidebar(QWidget):
    def __init__(self):
        super().__init__()
        
        # use vbox for stacked buttons
        layout = QVBoxLayout()
        
        # define buttons
        self.s1_btn = QPushButton("Sensor X Data")
        self.s2_btn = QPushButton("Sensor Y Data")
        self.s3_btn = QPushButton("Sensor Z Data")
        
        # put in a list
        self.btns = [self.s1_btn, self.s2_btn, self.s3_btn]
        
        # add buttons to button layout
        layout.addWidget(self.s1_btn)
        layout.addWidget(self.s2_btn)
        layout.addWidget(self.s3_btn)
        layout.addStretch() # ensure buttons are at the top
        
        self.setLayout(layout)
        self.setFixedWidth(180) # fixed width sidebar

class RCMotorControls(QWidget):
    def __init__(self):
        super().__init__()
        
        layout = QVBoxLayout()
        
        # Page title
        title = QLabel("RC Motor Controls")
        title.setAlignment(Qt.AlignmentFlag.AlignLeft)
        title.setStyleSheet("font-size: 20px;")
        
        # Graph placeholder
        graph_placeholder = QLabel("fhdsjkfhjdskhfjdsk")
        graph_placeholder.setAlignment(Qt.AlignmentFlag.AlignLeft)
        graph_placeholder.setStyleSheet("border: 2px dashed gray; background-color: #ffe6e6;")
        graph_placeholder.setMinimumSize(400, 250)
        
        layout.addWidget(title)
        layout.addWidget(graph_placeholder)
        layout.addStretch()
        
        self.setLayout(layout)
        
class DCMotorControls(QWidget):
    def __init__(self):
        super().__init__()
        
        layout = QVBoxLayout()
        
        # Page title
        title = QLabel("DC Motor Controls")
        title.setAlignment(Qt.AlignmentFlag.AlignLeft)
        title.setStyleSheet("font-size: 20px;")
        
        # Graph placeholder
        graph_placeholder = QLabel("fhdsjkfhjdskhfjdsk")
        graph_placeholder.setAlignment(Qt.AlignmentFlag.AlignLeft)
        graph_placeholder.setStyleSheet("border: 2px dashed gray; background-color: #ffe6e6;")
        graph_placeholder.setMinimumSize(400, 250)
        
        layout.addWidget(title)
        layout.addWidget(graph_placeholder)
        layout.addStretch()
        
        self.setLayout(layout)
        
class StepperControls(QWidget):
    def __init__(self):
        super().__init__()
        
        layout = QVBoxLayout()
        
        # Page title
        title = QLabel("Stepper Motor Controls")
        title.setAlignment(Qt.AlignmentFlag.AlignLeft)
        title.setStyleSheet("font-size: 20px;")
        
        # Graph placeholder
        graph_placeholder = QLabel("fhdsjkfhjdskhfjdsk")
        graph_placeholder.setAlignment(Qt.AlignmentFlag.AlignLeft)
        graph_placeholder.setStyleSheet("border: 2px dashed gray; background-color: #ffe6e6;")
        graph_placeholder.setMinimumSize(400, 250)
        
        layout.addWidget(title)
        layout.addWidget(graph_placeholder)
        layout.addStretch()
        
        self.setLayout(layout)

        
# design the main window
class MainInterface(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # global gui things
        self.setMinimumSize(QSize(800, 400))
        self.setWindowTitle("Lab 02 - Motors")
        
        # define widgets
        self.rc_ctrl = RCMotorControls()
        self.dc_ctrl = DCMotorControls()
        self.stepper_ctrl = StepperControls()
        
        # use hbox to put sidebar next to panels
        central_widget = QWidget()
        main_layout = QHBoxLayout()
        
        # set controllers
        main_layout.addWidget(self.rc_ctrl)
        main_layout.addWidget(self.dc_ctrl)
        main_layout.addWidget(self.stepper_ctrl)
        
        # set central widget and layout
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
    window.show() # windows hdiden by default

    app.exec()


        
        
        
        
        
        
        
