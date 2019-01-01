from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QPushButton, QWidget, QTextEdit

style = open('StyleSheet.qss', "r")
app = QApplication([])
app.setStyleSheet(style.read())
app.setStyle('Fusion')
window = QWidget()
layout = QVBoxLayout()
text = QTextEdit()

label = QLabel('Hello World!')
layout.addWidget(label)
layout.addWidget(QPushButton('Top'))
layout.addWidget(QPushButton('Bottom'))
layout.addWidget(text)
window.setLayout(layout)
window.show()
app.exec_()
