from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap 

from PIL import Image, ImageFilter

import os

app = QApplication([])
window = QWidget()
window.resize(700, 500)

btn_papka = QPushButton('папка')
btn_vlivo = QPushButton('вліво')
btn_vpravo = QPushButton('вправо')
btn_dzerkalo = QPushButton('дзеркало')
btn_rizkicnm = QPushButton('різкість')
btn_bw = QPushButton('чб')

lst_fils = QListWidget()
lb_pic = QLabel("картина")

leut = QHBoxLayout()
row = QHBoxLayout()

col1 = QVBoxLayout()
col2 = QVBoxLayout()

leut.addLayout(col1, 1)
leut.addLayout(col2, 4)

row.addWidget(btn_vlivo)
row.addWidget(btn_vpravo)
row.addWidget(btn_dzerkalo)
row.addWidget(btn_rizkicnm)
row.addWidget(btn_bw)

col1.addWidget(btn_papka)
col1.addWidget(lst_fils)

col2.addWidget(lb_pic)
col2.addLayout(row)
    
def showfaulneumlest():
    global workdir
    workdir = QFileDialog.getExistingDirectory()
    fals = os.listdir(workdir)
    
    filnemes = filter(fals)
    lst_fils.clear()
    lst_fils.addItems(filnemes)
    
def filter (fals):
    exts = ['jpg', 'png', 'bmp', 'jpeg', 'gif']
    img_file = []
    
    for i in fals:
        if i.split(".")[-1] in exts:
            img_file.append(i)
    return img_file

class ImageProcessor():
    def __init__(self):
        self.original = None
        self.filename = None
        self.save_dir = "Modified/"
    
    def lotimege(self, filename):
        self.filename = filename
        foll_past = os.path.join(workdir, filename)
        self.original = Image.open(foll_past)
        
    def showimeg(self, ful_path):
        lb_pic.hide()
        pixmapimage = QPixmap(ful_path)
        w, h = lb_pic.width(),lb_pic.height()
        
        pixmapimage = pixmapimage.scaled(w, h, Qt.KeepAspectRatio)
        
        lb_pic.setPixmap(pixmapimage)
        lb_pic.show()
        
    def saveandshowImege(self):
        path = os.path.join(workdir, self.save_dir)
        if not (os.path.exists(path) or os.path.isdir(path)):
            os.mkdir(path)
        Image_path = os.path.join(path,self.filename)
        self.original.save(Image_path)
        self.showimeg(Image_path)
        
    def do_bw(self):
        self.original = self.original.convert('L')
        self.saveandshowImege()
        
    def do_sharp(self):
        self.original = self.original.filter(ImageFilter.SHARPEN)
        self.saveandshowImege()
    
    def do_left(self):
        self.original = self.original.transpose(Image.ROTATE_90)
        self.saveandshowImege()
    
    def do_right(self):
        self.original = self.original.transpose(Image.ROTATE_270)
        self.saveandshowImege()
    
    def do_flip(self):
        self.original = self.original.transpose(Image.FLIP_LEFT_RIGHT)
        self.saveandshowImege()
    
    
def  showchosenItem():
    filename = lst_fils.currentItem().text()
    workimage.lotimege(filename)
    foll_past = os.path.join(workdir, filename)
    workimage.showimeg(foll_past)

workimage = ImageProcessor()

btn_bw.clicked.connect(workimage.do_bw)
 
btn_vlivo.clicked.connect(workimage.do_left)
 
btn_vpravo.clicked.connect(workimage.do_right)
 
btn_rizkicnm.clicked.connect(workimage.do_sharp)
 
btn_dzerkalo.clicked.connect(workimage.do_flip)
 
lst_fils.itemClicked.connect(showchosenItem)
btn_papka.clicked.connect(showfaulneumlest)

window.setLayout(leut)
window.show()
app.exec_()