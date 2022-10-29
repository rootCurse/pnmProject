from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QMessageBox
from PyQt5.QtGui import QPixmap, QImage
import sys
import pnm as p





class ImageConverter(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.img = p.pnmImage()
        self.layout = QtWidgets.QGridLayout(self)

        openBtn = QtWidgets.QPushButton('Open')
        self.layout.addWidget(openBtn, 0, 0)
        openBtn.clicked.connect(self.openFile)

        self.saveBtn = QtWidgets.QPushButton('Save')
        self.layout.addWidget(self.saveBtn, 1, 0)
        self.saveBtn.clicked.connect(self.saveFile)
        self.saveBtn.setEnabled(False)

        self.original = QtWidgets.QLabel()
        self.layout.addWidget(self.original, 2, 0)
        self.original.adjustSize()

    def openFile(self):
        path, filter = QtWidgets.QFileDialog.getOpenFileName(
            self, 'Select image', '')
        message = self.img.open(path)
        pixmap = QPixmap(path)
        if (not pixmap.isNull()) and message == "Success":
            self.original.setPixmap(pixmap)
            self.saveBtn.setEnabled(True)
        if message != "Success":
            QMessageBox.about(self, "Exception", message)
        if pixmap.isNull():
            QMessageBox.about(self, "Exception", "The File is damaged")

    def saveFile(self):
        path = QtWidgets.QFileDialog.getExistingDirectory(self, 'Select path save', '')
        text, ok = QtWidgets.QInputDialog.getText(self, 'File Name', 'Enter file name:')
        if ok:
            self.img.save(path + "/" + text + ".pnm")


app = QtWidgets.QApplication(sys.argv)
window = ImageConverter()
window.show()
sys.exit(app.exec())
