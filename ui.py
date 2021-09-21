from main import *

globalState = 0

class UIFunction(MainWindow):
    def maximize_restore(self):
        global globalState
        status = globalState

        if status == 0:
            self.showMaximized()

            globalState = 1
            self.ui.WinFrameLayout.setSpacing(0)
            self.ui.WinFrameLayout.setContentsMargins(0,0,0,0)
            self.ui.WinFrame.setStyleSheet("background-color: rgba(0,0,0,0);")
            self.ui.btnMaxmize.setToolTip("Restore")
            self.ui.titleLabel.setStyleSheet("background-color:rgba(221, 200, 219, 180);border-radius:0px;")
            self.ui.titleBtns.setStyleSheet("background-color:rgba(221, 200, 219, 180);border-radius:0px;")
            self.ui.horizontalLayout.setStretch(0, 10)
            self.ui.horizontalLayout.setStretch(1, 1)
            self.ui.horizontalLayout.setSpacing(0)
            self.ui.frame.setStyleSheet("background-color: rgb(170, 170, 255);border-radius:4px;")
        else:
            self.ui.WinFrameLayout.setSpacing(7)
            globalState = 0
            self.showNormal()
            self.resize(self.width() + 1, self.height() + 1)
            self.ui.WinFrameLayout.setContentsMargins(10,10,10,10)
            self.ui.WinFrame.setStyleSheet("background-color: rgba(0,0,0,0);")          
            self.ui.titleBtns.setStyleSheet("background-color:rgba(221, 200, 219, 180);border-radius:10px;")    
            self.ui.titleLabel.setStyleSheet("background-color:rgba(221, 200, 219, 180);border-radius:10px;")
            self.ui.horizontalLayout.setStretch(0, 10)
            self.ui.horizontalLayout.setStretch(1, 2)
            self.ui.btnMaxmize.setToolTip("Maximize")
            self.ui.horizontalLayout.setSpacing(6)
            self.ui.frame.setStyleSheet("background-color: rgb(170, 170, 255);border-radius:0px;")


    def UIFeature(self):
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.ui.btnMaxmize.clicked.connect(lambda: UIFunction.maximize_restore(self))
        self.ui.btnMinimize.clicked.connect(lambda: self.showMinimized())
        self.ui.btnClose.clicked.connect(lambda: self.close())

    def restoreStatus(self):
        return globalState
