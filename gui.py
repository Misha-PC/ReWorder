
import sys, main
from PyQt5.QtWidgets import (QWidget, QPushButton, QLineEdit, QInputDialog, QApplication, QTextEdit)




class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.btn = QPushButton('Dialog', self)
        self.btn.move(20, 20)
        self.btn.clicked.connect(self.showDialog)

        self.le = QTextEdit(self)
        self.le.resize(640, 430)
        self.le.move(20, 60)

        self.setGeometry(300, 300, 700, 500)
        self.setWindowTitle('Input dialog')
        self.show()


    def showDialog(self):

        text, ok = QInputDialog.getText(self, 'Input Dialog','Enter your text:')

        if ok:
            if 'file:' in text:
                    self.le.setText(main.mixText(main.readFile(text.replace('file:', ''))))
            else:
                self.le.setText(main.mixText(str(text)+'.'))


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
