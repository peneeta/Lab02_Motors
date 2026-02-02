import serial
from PyQt6.QtCore import Qt, QSize, QTimer
from PyQt6.QtWidgets import QWidget, QApplication, QMainWindow, QPushButton, QVBoxLayout, QHBoxLayout, QLabel, QStackedWidget
import sys

# Lab 2: Motors - Mechatronic Design (Spring 2026)

# arduino = serial.Serial(port="/dev/cu.usbmodem1101", baudrate=9600, timeout=0.05)

class UpdateButton(QPushButton):
    def __init__(self):
        super().__init__(text="Update Motor")
        self.clicked.connect(self.OnClick)
    
        
    def OnClick(self):
        
        # TODO send to corresponding motor
        print('Button clicked!')


class RCMotorControls(QWidget):
    def __init__(self):
        super().__init__()
        
        layout = QVBoxLayout()
        btn = UpdateButton()
        
        # Page title
        title = QLabel("RC Motor Controls")
        title.setAlignment(Qt.AlignmentFlag.AlignLeft)
        title.setStyleSheet("font-size: 20px;")
        
        # Graph placeholder
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
        
        # Graph placeholder
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
        layout.addWidget(btn)
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
    window.show()

    app.exec()


        
        
        
        
        
        
        
