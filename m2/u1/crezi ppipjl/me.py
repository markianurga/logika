from random import randint
from random import randint
from PyQt5.Qt import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
app = QApplication([])
main_window = QWidget()

text = QLabel('натисніть кнопку шоб дізнайтися перемошца')
winner = QLabel('?')
butto = QPushButton('знеругувати')

line = QVBoxLayout()
line.addWidget(text, alignment=Qt.AlignCenter)
line.addWidget(winner, alignment=Qt.AlignCenter)
line.addWidget(butto, alignment=Qt.AlignCenter)

def win():
    ran = randint(1, 100)
    winner.setText(str(ran)) 
    
butto.clicked.connect(win)

main_window.setLayout(line)
main_window.show()

app.exec_()