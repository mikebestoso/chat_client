import sys
from PyQt5 import QtGui,QtWidgets

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()

window.setGeometry(0, 0, 500, 300)

window.setWindowTitle("Test GUI")
window.setStyleSheet("background-color:blue")
window.show()

sys.exit(app.exec_())


