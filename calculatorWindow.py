from PyQt5 import QtWidgets
from calculate import Ui_Calculator

class Calculator(QtWidgets.QMainWindow, Ui_Calculator):
    FirstNum = None
    UserSecondNumber = False
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
#########################################################################################
        #################### connecting Buttons #####################
#########################################################################################
        self.pushButton_zero.clicked.connect(self.digit_press)
        self.pushButton_1.clicked.connect(self.digit_press)
        self.pushButton_2.clicked.connect(self.digit_press)
        self.pushButton_3.clicked.connect(self.digit_press)
        self.pushButton_4.clicked.connect(self.digit_press)
        self.pushButton_5.clicked.connect(self.digit_press)
        self.pushButton_6.clicked.connect(self.digit_press)
        self.pushButton_7.clicked.connect(self.digit_press)
        self.pushButton_8.clicked.connect(self.digit_press)
        self.pushButton_9.clicked.connect(self.digit_press)
        self.pushButton_decimal.clicked.connect(self.decimal_press)
        self.pushButton_plus_minus.clicked.connect(self.uniaryoperation)
        self.pushButton_percentage.clicked.connect(self.uniaryoperation)

################################################################################################
        ###################  connecting Binary opeartors  #############################
################################################################################################

        self.pushButton_plus.clicked.connect(self.binaryopertion)
        self.pushButton_minus.clicked.connect(self.binaryopertion)
        self.pushButton_multiply.clicked.connect(self.binaryopertion)
        self.pushButton_divide.clicked.connect(self.binaryopertion)
        self.pushButton_equalsign.clicked.connect(self.equalpress)
        self.pushButton_clearbtn.clicked.connect(self.clear_press)
#################################################################################################
        ################## Using Checkables Pyqt5 ###########################
#################################################################################################
        self.pushButton_plus.setCheckable(True)
        self.pushButton_minus.setCheckable(True)
        self.pushButton_multiply.setCheckable(True)
        self.pushButton_divide.setCheckable(True)

##################################################################
############### MAIN FUNCTIONS ###################################
###################################################################

    def digit_press(self):
        button = self.sender()
        if ((self.pushButton_plus.isChecked() or self.pushButton_minus.isChecked() or self.pushButton_multiply.isChecked() or self.pushButton_divide.isChecked()) and (not self.UserSecondNumber)):
            newLabel = format(float(button.text()), '.15g')
            self.UserSecondNumber = True


        else:
            if '.' in self.display_box.text() and button.text() == '0':
                newLabel = format(self.display_box.text() + button.text(), '.15')

            else:
                newLabel = format(float(self.display_box.text() + button.text()), '.15g')

        self.display_box.setText(newLabel)


    def decimal_press(self):
        if '.' not in self.display_box.text():
            self.display_box.setText(self.display_box.text() + '.')

    def uniaryoperation(self):
        button = self.sender()

        labelNumber = float(self.display_box.text())

        if button.text() == '+/-':
            labelNumber = labelNumber * -1

        else: #button text == %
            labelNumber = labelNumber * 0.01

        newlabel = format(labelNumber, '.15g')
        self.display_box.setText(newlabel)


    def binaryopertion(self):
        button = self.sender()

        self.FirstNum =float(self.display_box.text())

        button.setChecked(True)

    def equalpress(self):
        secondNum = float(self.display_box.text())

        if self.pushButton_plus.isChecked():
            labelNumber = self.FirstNum + secondNum
            newLabel = format(labelNumber,'.15g')
            self.display_box.setText(newLabel)
            self.pushButton_plus.setChecked(False)

        elif self.pushButton_minus.isChecked():
            labelNumber = self.FirstNum - secondNum
            newLabel = format(labelNumber,'.15g')
            self.display_box.setText(newLabel)
            self.pushButton_minus.setChecked(False)

        elif self.pushButton_multiply.isChecked():
            labelNumber = self.FirstNum * secondNum
            newLabel = format(labelNumber,'.15g')
            self.display_box.setText(newLabel)
            self.pushButton_multiply.setChecked(False)

        elif self.pushButton_divide.isChecked():
            labelNumber = self.FirstNum / secondNum
            newLabel = format(labelNumber,'.15g')
            self.display_box.setText(newLabel)
            self.pushButton_divide.setChecked(False)

        self.UserSecondNumber = False


    def clear_press(self):
        self.pushButton_plus.setChecked(False)
        self.pushButton_minus.setChecked(False)
        self.pushButton_divide.setChecked(False)
        self.pushButton_multiply.setChecked(False)

        self.UserSecondNumber = False
        self.display_box.setText('0')
