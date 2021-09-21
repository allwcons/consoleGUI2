import sys
import platform
import os
import subprocess

from consoleApi import Console

from command import Command
from entries import entries

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from ui import *
from formWidget import *



from uiBase import Ui_MainWindow
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.oneBitNumber = 0
        self.path = os.getcwd()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.activeBit = None
        self.bits = []
        self.createOneBitArea()
        self.scrollAreaHeight = 0
        self.showNormal()
        self.changePath(os.getcwd())
        UIFunction.maximize_restore(self)
        UIFunction.maximize_restore(self)


        def moveWindow(event):
            if UIFunction.restoreStatus(self) == 1:
                UIFunction.maximize_restore(self)
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        self.ui.titleLabel.mouseMoveEvent = moveWindow

        UIFunction.UIFeature(self)

        self.show()
    def exit(self):
        self.close()

    def frameKeyPressed(self):
        self.runCommand(self.activeBit.commandEntry_2.text())
        self.activeBit.commandEntry_2.setEnabled(False)
        self.activeBit.commandEntry_2.setFocus()
        self.createOneBitArea()
        self.updatePath()




    def clearLayout(self,layout):
        while layout.count() - 1:
            child = layout.takeAt(0)
            if child.widget() is not None:
                child.widget().deleteLater()
        self.oneBitNumber = 0


    def runCommand(self,cmd):
        self.console.takeCommand(cmd)
        
    def showOutput(self,output):
        if output:
            self.activeBit.output_2.setWordWrap(True)
            self.activeBit.output_2.setText(self.activeBit.output_2.text() + "\n" + output)
        else:
            self.activeBit.deleteLater()
    def createOneBitArea(self):
        frame1 = QtWidgets.QWidget()
        uiFrame1 = Ui_Form()
        uiFrame1.setupUi(frame1)
        self.bits.append(uiFrame1)
        self.ui.verticalLayout_61.insertWidget(self.oneBitNumber,frame1)
        self.activeBit = uiFrame1
        self.activeBit.path_2.setTextInteractionFlags(Qt.TextSelectableByMouse)
        self.activeBit.output_2.setTextInteractionFlags(Qt.TextSelectableByMouse)
        self.activeBit.output_2.setText("")
        self.activeBit.commandEntry_2.returnPressed.connect(self.frameKeyPressed)
        
        self.oneBitNumber += 1
        self.activeBit.path_2.setText(self.path)
        self.activeBit.commandEntry_2.setFocus()

    def clear(self):
        self.clearLayout(self.ui.verticalLayout_61)

    def updatePath(self):
        self.changePath(self.path)

    def changePath(self, path):
        self.path = path

    def getPath(self):
        return self.path
    def colorText(self,label,color):
        self.activeBit.output_2.setStyleSheet(f"color:{color}")
        self.showOutput(label)

    def error(self,error):
        r = self.colorText(error,"red")

    def warn(self,warning):
        r = self.colorText(warning,"yellow")

    def simple(self,text):
        r = self.colorText(text,"green")

    def special(self,text):
        r = self.colorText(text,"pink")

    def log(self,text,type="simple"):
        if(type == "simple"):
            self.simple(text)
        elif(type == "error"):
            self.error(text)
        elif(type == "warn"):
            self.warn(text)
        elif(type == "special"):
            self.special(text)

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    def setApiHandler(self, console):
        self.console = console

    def customizeScrollBar(self):
        self.ui.scrollArea.setStyleSheet("QScrollBar:vertical {\n"
"\n"
"   border: none;\n"
"\n"
"    background: rgb(45, 45, 68);\n"
"\n"
"    width: 14px;\n"
"\n"
"    margin: 15px 0 15px 0;\n"
"\n"
"    border-radius: 0px;\n"
"\n"
" }\n"
"\n"
"\n"
"\n"
"QScrollBar::handle:vertical {    \n"
"\n"
"    background-color: rgb(80, 80, 122);\n"
"\n"
"    min-height: 30px;\n"
"\n"
"    border-radius: 7px;\n"
"\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover{    \n"
"\n"
"    background-color:rgb(112, 10, 255);\n"
"\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:pressed {    \n"
"\n"
"    background-color: rgb(112, 10, 205);\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"\n"
"    border: none;\n"
"   background-color: rgb(59, 59, 90);\n"
"   height: 15px;\n"
"\n"
"    border-top-left-radius: 7px;\n"
"\n"
"    border-top-right-radius: 7px;\n"
"\n"
"   subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical:hover {    \n"
"\n"
"    background-color: rgb(255, 50, 10);\n"
"\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical:pressed {    \n"
"\n"
"    background-color:rgb(255, 50, 0);\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"\n"
"    border: none;\n"
"\n"
"    background-color: rgb(59, 59, 90);\n"
"\n"
"    height: 15px;\n"
"\n"
"    border-bottom-left-radius: 7px;\n"
"\n"
"    border-bottom-right-radius: 7px;\n"
"\n"
"    subcontrol-position: bottom;\n"
"\n"
"    subcontrol-origin: margin;\n"
"\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical:hover {    \n"
"\n"
"    background-color: rgb(255, 50, 10);\n"
"\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical:pressed {    \n"
"\n"
"    background-color: rgb(255, 50, 0);\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"\n"
"    background: none;\n"
"\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"\n"
"    background: none;\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"QScrollBar:horizontal {\n"
"\n"
"       border: none;\n"
"\n"
"    background: rgb(45, 45, 68);\n"
"\n"
"    height: 14px;\n"
"\n"
"    margin: 0 15px 0px 15px;\n"
"\n"
"    border-radius: 0px;\n"
"\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"\n"
"    background-color: rgb(80, 80, 122);\n"
"\n"
"    min-width: 30px;\n"
"\n"
"    border-radius: 7px;\n"
"\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"\n"
"    border: none;\n"
"\n"
"    background-color: rgb(59, 59, 90);\n"
"\n"
"    width: 15px;\n"
"\n"
"    border-top-right-radius: 7px;\n"
"\n"
"    border-bottom-right-radius: 7px;\n"
"\n"
"    subcontrol-position: right;\n"
"\n"
"    subcontrol-origin: margin;\n"
"\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"\n"
"    border: none;\n"
"\n"
"    background-color: rgb(59, 59, 90);\n"
"\n"
"    border-top-left-radius: 7px;\n"
"\n"
"    width:15px;\n"
"\n"
"    border-bottom-left-radius: 7px;\n"
"\n"
"    subcontrol-position: left;\n"
"\n"
"    subcontrol-origin: margin;\n"
"\n"
"}\n"
"\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"\n"
"{\n"
"\n"
"background: none;\n"
"\n"
"}\n"
"\n"
"ScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"\n"
"{\n"
"\n"
"background: none;\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"QScrollBar::handle:horizontal:hover{    \n"
"\n"
"   background-color:rgb(112, 10, 255);\n"
"\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal:pressed {    \n"
"\n"
"    background-color: rgb(112, 10, 205);\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"QScrollBar::sub-line:horizontal:hover {    \n"
"\n"
"    background-color: rgb(255, 50, 10);\n"
"\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal:pressed {    \n"
"\n"
"    background-color:rgb(255, 50, 0);\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"QScrollBar::add-line:horizontal:hover {    \n"
"\n"
"    background-color: rgb(255, 50, 10);\n"
"\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal:pressed {    \n"
"\n"
"    background-color: rgb(255, 50, 0);\n"
"\n"
"}")
if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle(QStyleFactory.create('fusion'))
    window = MainWindow()
    c = Console(window)
    cmd = Command(c)


    cmd.addCommands(entries(c,cmd)[0])
    cmd.setDobuleCommandDict(entries(c,cmd)[1])


    c.addCommands(cmd)
    sys.exit(app.exec_())
