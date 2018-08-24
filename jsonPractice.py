import json
import sys
from PyQt5 import QtCore, QtGui, QtWidgets

#data = json.load(open("jsonFile.json"))

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.b=QtWidgets.QPushButton("Hold")
        self.label=QtWidgets.QLabel("this is cool")
        self.lineEdit=QtWidgets.QLineEdit()
        self.b.clicked.connect(self.saysomething)

        #set up the layout
        horizontal =QtWidgets.QHBoxLayout()
        horizontal.addStretch()
        horizontal.addWidget(self.label)
        horizontal.addStretch()

        vertical=QtWidgets.QVBoxLayout()
        vertical.addWidget(self.b)
        vertical.addWidget(self.lineEdit)
        vertical.addLayout(horizontal)

        self.setLayout(vertical)
        self.setWindowTitle("My Contact List")

        self.show()

    def saysomething(self):
        self.label.setText("I was clicked")

application=QtWidgets.QApplication(sys.argv)
session =Window()
sys.exit(application.exec_())


#for the application when you click on the contacts, use a sender

#example
#self.sender() -this gets the object that sent the signal,add this to avariable
#sender.text() - this gets the text that the object(button) holds

#you can also print out the text of a specific button by doing: button.text()

#to clear a line lineEdit#
#self.<objectName>.clear()
