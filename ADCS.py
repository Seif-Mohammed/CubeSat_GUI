import sys
from PyQt6 import QtWidgets , QtCore
from PyQt6.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QLabel, QLineEdit , QTabWidget
from PyQt6.QtGui import QFont, QColor ,QPixmap

class SensorApp(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Sensor Data GUI")
        self.setGeometry(100, 100, 700, 300)
        background_label = QLabel(self)
        pixmap = QPixmap("background.jpg") 
        background_label.setPixmap(pixmap)
        background_label.setGeometry(0, 0, 1920, 1080)  # Set label size to cover the entire window

        # Set a lower stacking order for the background_label
        background_label.lower()

        

        self.setup_ui()

    def setup_ui(self):
        main_layout = QVBoxLayout(self)
        self.tab_widget = QtWidgets.QTabWidget(self)
        self.tab_widget.setMaximumSize(QtCore.QSize(16777215, 50))
        self.tab_widget.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
"font: 20pt \"MS Shell Dlg 2\";")
        self.tab_widget.setIconSize(QtCore.QSize(40, 18))
        self.tab_widget.setObjectName("tab_widget")
        # Create tabs and their corresponding widgets
        tabs = ["MainWindow", "COMM", "EPS", "ADCS", "OBC"]
        for tab_name in tabs:
            self.tab = QWidget()
            self.tab_widget.addTab(self.tab , tab_name)
        self.tab_widget.setCurrentIndex(0)
        main_layout.addWidget(self.tab_widget)
        
        self.setLayout(main_layout)
        categories = [
            ("LDRs", ["Lux 1", "Lux 2", "Lux 3", "Lux 4"]),
            ("Accelerometer", ["Acc X", "Acc Y", "Acc Z"]),
            ("Gyro Sensor", ["Gyro X", "Gyro Y", "Gyro Z"]),
            ("Magnetometer", ["Magn X", "Magn Y", "Magn Z"]),
            ("ADSC Temp", ["ADSC Temp"]),
            ("Kalman Filter", ["Kalman X", "Kalman Y", "Kalman Z"]),
            ("Number of Satellites", ["Number of Satellites"]),
            ("Position Coordinates", ["Longitude", "Latitude", "Altitude"])
        ]

        white_color = QColor('white')

        for i in range(0, len(categories), 3):
            row_layout = QHBoxLayout()

            for category_name, sensors in categories[i:i+3]:
                category_group_box = QGroupBox(category_name)
                category_group_box.setStyleSheet(f'color: {white_color.name()}')
                font = category_group_box.font()
                font.setBold(True)
                font.setPointSize(font.pointSize() + 6)
                category_group_box.setFont(font)
                category_layout = QVBoxLayout(category_group_box)

                for sensor in sensors:
                    label = QLabel(sensor)
                    text_box = QLineEdit()
                    text_box.setReadOnly(True)

                    # Set the font style
                    font = label.font()
                    font.setBold(True)
                    font.setPointSize(font.pointSize() + 4)
                    label.setFont(font)

                    # Set the text color to white
                    label.setStyleSheet(f'color: {white_color.name()}')

                    category_layout.addWidget(label)
                    category_layout.addWidget(text_box)

                row_layout.addWidget(category_group_box)

            main_layout.addLayout(row_layout)


        self.setLayout(main_layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SensorApp()
    window.show()
    sys.exit(app.exec())
