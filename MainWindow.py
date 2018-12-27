import sys
from PyQt5 import QtGui,QtWidgets
from interface.Client import ClientCommunicationInterface

#Main GUI Window
app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()

window.setGeometry(0, 0, 1000, 600)

window.setWindowTitle("Test GUI")
window.setStyleSheet("background-color:blue")
window.show()



#Create chat client interface here
chat_client = ClientCommunicationInterface("Default",1)
chat_client.send("This is just a test message")
sys.exit(app.exec_())


