import sys
from PyQt5 import QtCore, QtGui, QtWidgets


def window(message):
    app = QtWidgets.QApplication(sys.argv)
    popup = QtWidgets.QWidget()
    popup.setGeometry(200,200,430,150)
    popup.setWindowTitle("Error")
    popup.setStyleSheet("background-color:#46484c")

    #create a label to show on the setWindowTitle
    messageLabel= QtWidgets.QLabel(popup)
    messageLabel.setText(message)
    messageLabel.setStyleSheet("font:14pt Arial;padding:5px;color:#d4d5d8")
    messageLabel.move(10,40)
    #create a button for the window, the user should only click "OK"
    messageButton = QtWidgets.QPushButton(popup)
    messageButton.setText("OK")
    messageButton.move(310,100)
    messageButton.resize(100,35)
    messageButton.setStyleSheet("border-radius:3px;background-color:#42b6f4;border:2px ")
    messageButton.clicked.connect(lambda: closeApp())

    popup.show()
    sys.exit(app.exec_())

def closeApp():
    sys.exit()
