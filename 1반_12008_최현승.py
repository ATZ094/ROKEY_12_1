import sys
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow


class HeartWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt6 하트")
        self.resize(320, 240)

        label = QLabel("❤️", self)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.setFont(QFont("Arial", 72))
        self.setCentralWidget(label)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = HeartWindow()
    window.show()
    sys.exit(app.exec())