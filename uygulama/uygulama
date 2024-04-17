import sys
from PyQt6 import QtWidgets
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication,QMainWindow
from PyQt6.QtGui import QIcon



"""


def windows():
    app = QApplication(sys.argv)
    win = QMainWindow()

    win.setWindowTitle("Siber Vatan")
    win.setGeometry(700,500,368,498)
    win.setWindowIcon(QIcon("download.jpg"))

    labe_name = QtWidgets.QLabel(win)
    labe_name.setText("adınız: ")
    labe_name.move(50,30)

    labe_surname = QtWidgets.QLabel(win)
    labe_surname.setText("soyadınız: ")
    labe_surname.move(50,60)

    text_name = QtWidgets.QLineEdit(win)
    text_name.move(150,30)

    text_sname = QtWidgets.QLineEdit(win)
    text_sname.move(150,60)

    save = QtWidgets.QPushButton(win)
    save.setText("arşiv")
    save.move(150,150)
    def clicked():
        print("ad: "+ text_name.text()+ "\nsoyad: " + text_sname.text())
    save.clicked.connect(clicked)
#bir şeyler denedim
    #--kandımce bir şeyler
    #cubuk = QtWidgets.QScrollBar(win)
    #cubuk.setWindowIconText
    #cubuk.move(20,50)

    win.show()
    sys.exit(app.exec())
windows()
"""

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow,self).__init__()
        self.setWindowTitle("siber Vatan")
        self.setGeometry(750,750,500,500)
        self.setWindowIcon(QIcon("dowlond.jpg"))
        self.initUI()
    def initUI(self):
        self.label_name = QtWidgets.QLabel(self)
        self.label_name.setText("adınız:  ")
        self.label_name.move(50,30)
        
        self.label_sname = QtWidgets.QLabel(self)
        self.label_sname.setText("soyadınız: ")
        self.label_sname.move(150,60)
        
        self.label_name = QtWidgets.QLineEdit(self)
        self.label_name.move(150,30)

        self.txt_sname = QtWidgets.QLineEdit(self)
        self.txt_sname.move(150,70)

        self.label_result = QtWidgets.QLabel(self)
        self.label_result.setText("sonuc: ")
        self.label_result.resize(200,200)
        self.label_result.move(150,170)

        self.save = QtWidgets.QPushButton(self)
        self.save.setText("kaydet: ")
        self.save.move(150,170)
        self.save.clicked.connect(self.clicked)

    def clicked(self):
        self.label_result.setText("ad: " + self.txt_name.text() + "soyad: " + self.txt_sname.text())



def window():
        app = QApplication(sys.argv)
        win = MyWindow()

        win.show()
        sys.exit(app.exec())
        
window()
