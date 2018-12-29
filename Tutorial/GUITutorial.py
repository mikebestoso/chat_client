from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QPushButton, QWidget

style = open('StyleSheet.qss', "r")
app = QApplication([])
app.setStyleSheet(style.read())
app.setStyle('Fusion')
window = QWidget()
layout = QVBoxLayout()

label = QLabel('Hello World!')
layout.addWidget(label)
layout.addWidget(QPushButton('Top'))
layout.addWidget(QPushButton('Bottom'))
window.setLayout(layout)
window.show()
app.exec_()
