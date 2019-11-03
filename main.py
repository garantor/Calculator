import sys
from PyQt5.QtWidgets import QApplication
from calculatorWindow import Calculator

app = QApplication(sys.argv)
calculator = Calculator()

sys.exit(app.exec())