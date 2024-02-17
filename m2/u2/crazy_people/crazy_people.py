from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout,  QRadioButton, QHBoxLayout


app = QApplication([])
main_win = QWidget()

text = QLabel('який в мене еріст? ')

radio_btn1 = QRadioButton('150')
radio_btn2 = QRadioButton('170')
radio_btn3 = QRadioButton('190')
radio_btn4 = QRadioButton('210')

line = QVBoxLayout()

hline1 = QHBoxLayout()
hline2 = QHBoxLayout()
hline3 = QHBoxLayout()

hline1.addWidget(text, alignment=Qt.AlignCenter)

hline2.addWidget(radio_btn1, alignment=Qt.AlignCenter)
hline2.addWidget(radio_btn2, alignment=Qt.AlignCenter)

hline3.addWidget(radio_btn3, alignment=Qt.AlignCenter)
hline3.addWidget(radio_btn4, alignment=Qt.AlignCenter)

line.addLayout(hline1)
line.addLayout(hline2)
line.addLayout(hline3)

main_win.setLayout(line)
main_win.show()

app.exec_()


a = """
background-color : yellow;
font-size: 20px
"""

#button.setStyleSheet(a)