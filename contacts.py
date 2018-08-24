import json
import sys
from PyQt5 import QtCore, QtGui, QtWidgets




application = QtWidgets.QApplication(sys.argv)
mainwindow = QtWidgets.QWidget()
mainwindow.setWindowTitle("Contacts")
mainwindow.setGeometry(40,40,500,400)


#add a QLabel
label =QtWidgets.QLabel(mainwindow)
label.setText("testing")
label.move(20,50)

#add a QPushButton
button = QtWidgets.QPushButton(mainwindow)
button.setText("Push Me")
button.clicked.connect(lambda: action("cool"))








def action(arg):
    label.move(50,70)

mainwindow.show()
sys.exit(application.exec_())
