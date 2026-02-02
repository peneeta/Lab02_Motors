import serial
from PyQt6.QtCore import Qt, QSize, QTimer
from PyQt6.QtWidgets import QWidget, QApplication, QMainWindow, QPushButton, QVBoxLayout, QHBoxLayout, QLabel, QStackedWidget
import sys

# Lab 2: Motors - Mechatronic Design (Spring 2026)

# TODO Update for motors lab

arduino = serial.Serial(port="/dev/cu.usbmodem1101", baudrate=9600, timeout=0.05)

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

# process sensor 1
class Sensor1Page(QWidget):
    def __init__(self):
        super().__init__()
        
        layout = QVBoxLayout()
        
        # Page title
        title = QLabel("Distance")
        title.setAlignment(Qt.AlignmentFlag.AlignLeft)
        title.setStyleSheet("font-size: 20px;")
        
        # Graph placeholder
        graph_placeholder = QLabel("fhdsjkfhjdskhfjdsk")
        graph_placeholder.setAlignment(Qt.AlignmentFlag.AlignLeft)
        graph_placeholder.setStyleSheet("border: 2px dashed gray; background-color: #ffe6e6;")
        graph_placeholder.setMinimumSize(400, 250)

        self.value_label = QLabel("Latest Distance: --")
        self.value_label.setAlignment(Qt.AlignmentFlag.AlignLeft)
        
        layout.addWidget(title)
        layout.addWidget(self.value_label)
        layout.addWidget(graph_placeholder)
        layout.addStretch()
        
        self.setLayout(layout)

    def update_value(self, value):
        self.value_label.setText(f"Latest Distance: {value} cm")

# process sensor 2
class Sensor2Page(QWidget):
    def __init__(self):
        super().__init__()
        
        layout = QVBoxLayout()
        
        # Page title
        title = QLabel("Temperature + Humidity")
        title.setAlignment(Qt.AlignmentFlag.AlignLeft)
        title.setStyleSheet("font-size: 20px;")
        
        # Graph placeholder
        graph_placeholder = QLabel("fjkdsljfkdlajfkdls")
        graph_placeholder.setAlignment(Qt.AlignmentFlag.AlignLeft)
        graph_placeholder.setStyleSheet("border: 2px dashed gray; background-color: #ffe6e6;")
        graph_placeholder.setMinimumSize(400, 250)

        self.value_label = QLabel("Latest Temperature: --\nLatest Humidity: --")
        self.value_label.setAlignment(Qt.AlignmentFlag.AlignLeft)
        
        layout.addWidget(title)
        layout.addWidget(self.value_label)
        layout.addWidget(graph_placeholder)
        layout.addStretch()
        
        self.setLayout(layout)

    def update_value(self, temperature, humidity):
        self.value_label.setText(
            f"Latest Temperature: {temperature} C\nLatest Humidity: {humidity}%"
        )

# process sensor 3
class Sensor3Page(QWidget):
    def __init__(self):
        super().__init__()
        
        layout = QVBoxLayout()
        
        # Page title
        title = QLabel("Light")
        title.setAlignment(Qt.AlignmentFlag.AlignLeft)
        title.setStyleSheet("font-size: 20px;")
        
        # Graph placeholder
        graph_placeholder = QLabel("JSkdfjskfjdsklfds")
        graph_placeholder.setAlignment(Qt.AlignmentFlag.AlignLeft)
        graph_placeholder.setStyleSheet("border: 2px dashed gray; background-color: #ffe6e6;")
        graph_placeholder.setMinimumSize(400, 250)

        self.value_label = QLabel("Latest Light: --")
        self.value_label.setAlignment(Qt.AlignmentFlag.AlignLeft)
        
        layout.addWidget(title)
        layout.addWidget(self.value_label)
        layout.addWidget(graph_placeholder)
        layout.addStretch()
        
        self.setLayout(layout)

    def update_value(self, value):
        self.value_label.setText(f"Latest Light: {value}")
        
# design the main window
class MainInterface(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # global gui things
        self.setMinimumSize(QSize(800, 400))
        self.setWindowTitle("Lab 01 - Sensors")
        
        # init the sidebar, init pages for sensors 
        self.sidebar = Sidebar()
        self.s1_page = Sensor1Page()
        self.s2_page = Sensor2Page()
        self.s3_page = Sensor3Page()
        
        # stacked widget for multiple pages
        self.stacked_widget = QStackedWidget()
        self.stacked_widget.addWidget(self.s1_page)  # Index 0
        self.stacked_widget.addWidget(self.s2_page)  # Index 1
        self.stacked_widget.addWidget(self.s3_page)  # Index 2
        
        # use hbox to put sidebar next to panels
        central_widget = QWidget()
        main_layout = QHBoxLayout()
        
        # add components to main layout
        main_layout.addWidget(self.sidebar)
        main_layout.addWidget(self.stacked_widget)
        
        # set central widget and layout
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)
        
        # toggle on button click
        self.sidebar.s1_btn.clicked.connect(lambda: self.TogglePage(0, self.sidebar.s1_btn))
        self.sidebar.s2_btn.clicked.connect(lambda: self.TogglePage(1, self.sidebar.s2_btn))
        self.sidebar.s3_btn.clicked.connect(lambda: self.TogglePage(2, self.sidebar.s3_btn))
        
        # initial pg
        self.TogglePage(0, self.sidebar.s1_btn)
        
        self.serial_timer = QTimer(self)
        self.serial_timer.setInterval(50)
        self.serial_timer.timeout.connect(self.poll_serial)
        self.serial_timer.start()
    
    # toggle which sensor data is shown
    def TogglePage(self, index, button):
        self.stacked_widget.setCurrentIndex(index)
        # self.sidebar.highlight_button(button) # TODO IF TIME

    def poll_serial(self):
        try:
            line = arduino.readline().decode("utf-8", errors="ignore").strip()
        except serial.SerialException:
            return

        if not line:
            return

        # arduino outputs (distance,humidity,temperature,light)
        parts = [p.strip() for p in line.split(",")]
        if len(parts) < 4:
            return

        distance, humidity, temperature, light = parts[0], parts[1], parts[2], parts[3]
        self.s1_page.update_value(distance)
        self.s2_page.update_value(temperature, humidity)
        self.s3_page.update_value(light)
        

# run the app
if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainInterface()
    window.show() # windows hdiden by default

    app.exec()


        
        
        
        
        
        
        
