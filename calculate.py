# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calculate.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Calculator(object):
    def setupUi(self, Calculator):
        Calculator.setObjectName("Calculator")
        Calculator.resize(241, 378)
        Calculator.setStyleSheet("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../Downloads/bootstrap_stack_FsS_icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Calculator.setWindowIcon(icon)
        Calculator.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(Calculator)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_clearbtn = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_clearbtn.setGeometry(QtCore.QRect(0, 80, 61, 61))
        self.pushButton_clearbtn.setStyleSheet("QPushButton {\n"
"  background-color: rgb(215, 215, 215);\n"
"  border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #BEBEBE, stop: 1 #D7D7D7);}")
        self.pushButton_clearbtn.setAutoRepeatDelay(300)
        self.pushButton_clearbtn.setObjectName("pushButton_clearbtn")
        self.display_box = QtWidgets.QLabel(self.centralwidget)
        self.display_box.setGeometry(QtCore.QRect(0, 0, 241, 81))
        font = QtGui.QFont()
        font.setPointSize(19)
        self.display_box.setFont(font)
        self.display_box.setStyleSheet("QLabel {\n"
"  qproperty-alignment: \'AlignVCenter | AlignRight\';\n"
"  border: 1px solid gray;\n"
"}\n"
"\n"
"background-color : white;")
        self.display_box.setObjectName("display_box")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(60, 140, 61, 61))
        self.pushButton_8.setStyleSheet("QPushButton {\n"
"   border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}")
        self.pushButton_8.setAutoRepeatDelay(300)
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(60, 200, 61, 61))
        self.pushButton_5.setStyleSheet("QPushButton {\n"
"   border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}")
        self.pushButton_5.setAutoRepeatDelay(300)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(60, 260, 61, 61))
        self.pushButton_2.setStyleSheet("QPushButton {\n"
"   border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}")
        self.pushButton_2.setAutoRepeatDelay(300)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(0, 260, 61, 61))
        self.pushButton_1.setStyleSheet("QPushButton {\n"
"   border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}")
        self.pushButton_1.setAutoRepeatDelay(300)
        self.pushButton_1.setObjectName("pushButton_1")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(0, 200, 61, 61))
        self.pushButton_4.setStyleSheet("QPushButton {\n"
"   border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}")
        self.pushButton_4.setAutoRepeatDelay(300)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(0, 140, 61, 61))
        self.pushButton_7.setStyleSheet("QPushButton {\n"
"   border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}")
        self.pushButton_7.setAutoRepeatDelay(300)
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_percentage = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_percentage.setGeometry(QtCore.QRect(120, 80, 61, 61))
        self.pushButton_percentage.setStyleSheet("QPushButton {\n"
"  background-color: rgb(215, 215, 215);\n"
"  border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #BEBEBE, stop: 1 #D7D7D7);}")
        self.pushButton_percentage.setAutoRepeatDelay(300)
        self.pushButton_percentage.setObjectName("pushButton_percentage")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(120, 140, 61, 61))
        self.pushButton_9.setStyleSheet("QPushButton {\n"
"   border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}")
        self.pushButton_9.setAutoRepeatDelay(300)
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(120, 200, 61, 61))
        self.pushButton_6.setStyleSheet("QPushButton {\n"
"   border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}")
        self.pushButton_6.setAutoRepeatDelay(300)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(120, 260, 61, 61))
        self.pushButton_3.setStyleSheet("QPushButton {\n"
"   border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}")
        self.pushButton_3.setAutoRepeatDelay(300)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_plus_minus = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_plus_minus.setGeometry(QtCore.QRect(60, 80, 61, 61))
        self.pushButton_plus_minus.setStyleSheet("QPushButton {\n"
"  background-color: rgb(215, 215, 215);\n"
"  border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #BEBEBE, stop: 1 #D7D7D7);}")
        self.pushButton_plus_minus.setAutoRepeatDelay(300)
        self.pushButton_plus_minus.setObjectName("pushButton_plus_minus")
        self.pushButton_multiply = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_multiply.setGeometry(QtCore.QRect(180, 140, 61, 61))
        self.pushButton_multiply.setStyleSheet("QPushButton {\n"
"  background-color: rgb(255, 151, 57);\n"
"  color: white; \n"
"  border: 1px solid gray;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #FF7832, stop: 1 #FF9739);\n"
"}")
        self.pushButton_multiply.setAutoRepeatDelay(300)
        self.pushButton_multiply.setObjectName("pushButton_multiply")
        self.pushButton_divide = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_divide.setGeometry(QtCore.QRect(180, 260, 61, 61))
        self.pushButton_divide.setStyleSheet("QPushButton {\n"
"  background-color: rgb(255, 151, 57);\n"
"  color: white; \n"
"  border: 1px solid gray;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #FF7832, stop: 1 #FF9739);\n"
"}")
        self.pushButton_divide.setAutoRepeatDelay(300)
        self.pushButton_divide.setObjectName("pushButton_divide")
        self.pushButton_minus = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_minus.setGeometry(QtCore.QRect(180, 200, 61, 61))
        self.pushButton_minus.setStyleSheet("QPushButton {\n"
"  background-color: rgb(255, 151, 57);\n"
"  color: white; \n"
"  border: 1px solid gray;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"stop: 0 #FF7832, stop: 1 #FF9739);\n}")
        self.pushButton_minus.setAutoRepeatDelay(300)
        self.pushButton_minus.setObjectName("pushButton_minus")
        self.pushButton_plus = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_plus.setGeometry(QtCore.QRect(180, 80, 61, 61))
        self.pushButton_plus.setStyleSheet("QPushButton {\n"
"  background-color: rgb(255, 151, 57);\n"
"  color: white; \n"
"  border: 1px solid gray;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\nstop: 0 #FF7832, stop: 1 #FF9739);\n"
"}")
        self.pushButton_plus.setAutoRepeatDelay(300)
        self.pushButton_plus.setObjectName("pushButton_plus")
        self.pushButton_equalsign = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_equalsign.setGeometry(QtCore.QRect(180, 320, 61, 61))
        self.pushButton_equalsign.setStyleSheet("QPushButton {\n"
"  background-color: rgb(255, 151, 57);\n"
"  color: white; \n"
"  border: 1px solid gray;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\nstop: 0 #FF7832, stop: 1 #FF9739);\n"
"}")
        self.pushButton_equalsign.setAutoRepeatDelay(300)
        self.pushButton_equalsign.setObjectName("pushButton_equalsign")
        self.pushButton_zero = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_zero.setGeometry(QtCore.QRect(0, 320, 122, 61))
        self.pushButton_zero.setStyleSheet("QPushButton {\n"
"   border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\nstop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}")
        self.pushButton_zero.setAutoRepeatDelay(300)
        self.pushButton_zero.setObjectName("pushButton_zero")
        self.pushButton_decimal = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_decimal.setGeometry(QtCore.QRect(120, 320, 61, 61))
        self.pushButton_decimal.setStyleSheet("QPushButton {\n"
"  background-color: rgb(215, 215, 215);\n"
"  border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\nstop: 0 #BEBEBE, stop: 1 #D7D7D7);}")
        self.pushButton_decimal.setAutoRepeatDelay(300)
        self.pushButton_decimal.setObjectName("pushButton_decimal")
        Calculator.setCentralWidget(self.centralwidget)

        self.retranslateUi(Calculator)
        QtCore.QMetaObject.connectSlotsByName(Calculator)

    def retranslateUi(self, Calculator):
        _translate = QtCore.QCoreApplication.translate
        Calculator.setWindowTitle(_translate("Calculator", "Calculator"))
        self.pushButton_clearbtn.setText(_translate("Calculator", "C"))
        self.display_box.setText(_translate("Calculator", "0"))
        self.pushButton_8.setText(_translate("Calculator", "8"))
        self.pushButton_5.setText(_translate("Calculator", "5"))
        self.pushButton_2.setText(_translate("Calculator", "2"))
        self.pushButton_1.setText(_translate("Calculator", "1"))
        self.pushButton_4.setText(_translate("Calculator", "4"))
        self.pushButton_7.setText(_translate("Calculator", "7"))
        self.pushButton_percentage.setText(_translate("Calculator", "%"))
        self.pushButton_9.setText(_translate("Calculator", "9"))
        self.pushButton_6.setText(_translate("Calculator", "6"))
        self.pushButton_3.setText(_translate("Calculator", "3"))
        self.pushButton_plus_minus.setText(_translate("Calculator", "+/-"))
        self.pushButton_multiply.setText(_translate("Calculator", "x"))
        self.pushButton_divide.setText(_translate("Calculator", "/"))
        self.pushButton_minus.setText(_translate("Calculator", "-"))
        self.pushButton_plus.setText(_translate("Calculator", "+"))
        self.pushButton_equalsign.setText(_translate("Calculator", "="))
        self.pushButton_zero.setText(_translate("Calculator", "0"))
        self.pushButton_decimal.setText(_translate("Calculator", "."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Calculator = QtWidgets.QMainWindow()
    ui = Ui_Calculator()
    ui.setupUi(Calculator)
    Calculator.show()
    sys.exit(app.exec_())

