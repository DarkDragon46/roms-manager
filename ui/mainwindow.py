# Form implementation generated from reading ui file '.\ui\mainwindow.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1218, 744)
        MainWindow.setAutoFillBackground(True)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(310, 460, 881, 181))
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(parent=self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 30, 47, 13))
        self.label.setObjectName("label")
        self.lcdNumber = QtWidgets.QLCDNumber(parent=self.groupBox)
        self.lcdNumber.setGeometry(QtCore.QRect(50, 30, 64, 23))
        self.lcdNumber.setObjectName("lcdNumber")
        self.label_4 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(10, 70, 91, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(110, 70, 81, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(10, 90, 81, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(110, 90, 71, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(10, 110, 81, 16))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_9.setGeometry(QtCore.QRect(110, 110, 71, 16))
        self.label_9.setObjectName("label_9")
        self.tableView = QtWidgets.QTableView(parent=self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(310, 90, 881, 351))
        self.tableView.setObjectName("tableView")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(110, 260, 47, 13))
        self.label_2.setObjectName("label_2")
        self.comboBox = QtWidgets.QComboBox(parent=self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(100, 10, 151, 22))
        self.comboBox.setObjectName("comboBox")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 91, 16))
        self.label_3.setObjectName("label_3")
        self.testButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.testButton.setGeometry(QtCore.QRect(380, 30, 75, 23))
        self.testButton.setObjectName("testButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1218, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(parent=self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuOptions = QtWidgets.QMenu(parent=self.menubar)
        self.menuOptions.setObjectName("menuOptions")
        self.menuHelp = QtWidgets.QMenu(parent=self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(parent=MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.ToolBarArea.TopToolBarArea, self.toolBar)
        self.actionFormat = QtGui.QAction(parent=MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(".\\ui\\../src/icons/16x16/actions/flag.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionFormat.setIcon(icon)
        self.actionFormat.setObjectName("actionFormat")
        self.actionArchive_Drive = QtGui.QAction(parent=MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(".\\ui\\../src/icons/16x16/places/folder-documents.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionArchive_Drive.setIcon(icon1)
        self.actionArchive_Drive.setObjectName("actionArchive_Drive")
        self.actionCalculate_hash = QtGui.QAction(parent=MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(".\\ui\\../src/icons/16x16/apps/kformula.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionCalculate_hash.setIcon(icon2)
        self.actionCalculate_hash.setObjectName("actionCalculate_hash")
        self.actionDelete_game = QtGui.QAction(parent=MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(".\\ui\\../src/icons/16x16/actions/cancel.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionDelete_game.setIcon(icon3)
        self.actionDelete_game.setObjectName("actionDelete_game")
        self.actionAbout = QtGui.QAction(parent=MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(".\\ui\\../src/icons/16x16/status/dialog-information.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionAbout.setIcon(icon4)
        self.actionAbout.setObjectName("actionAbout")
        self.actionMount_Drive = QtGui.QAction(parent=MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(".\\ui\\../src/icons/16x16/devices/cd-r_mount.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionMount_Drive.setIcon(icon5)
        self.actionMount_Drive.setObjectName("actionMount_Drive")
        self.actionExit_app = QtGui.QAction(parent=MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(".\\ui\\../src/icons/16x16/actions/go-home.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionExit_app.setIcon(icon6)
        self.actionExit_app.setObjectName("actionExit_app")
        self.actionAdd_Game = QtGui.QAction(parent=MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(".\\ui\\../src/icons/16x16/actions/add.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionAdd_Game.setIcon(icon7)
        self.actionAdd_Game.setObjectName("actionAdd_Game")
        self.menuFile.addAction(self.actionAdd_Game)
        self.menuFile.addAction(self.actionCalculate_hash)
        self.menuFile.addAction(self.actionExit_app)
        self.menuOptions.addAction(self.actionFormat)
        self.menuOptions.addAction(self.actionArchive_Drive)
        self.menuOptions.addAction(self.actionMount_Drive)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuOptions.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.toolBar.addAction(self.actionAdd_Game)
        self.toolBar.addAction(self.actionDelete_game)
        self.toolBar.addAction(self.actionCalculate_hash)
        self.toolBar.addAction(self.actionFormat)
        self.toolBar.addAction(self.actionArchive_Drive)
        self.toolBar.addAction(self.actionMount_Drive)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Stats"))
        self.label.setText(_translate("MainWindow", "Games:"))
        self.label_4.setText(_translate("MainWindow", "Total Diskspace:"))
        self.label_5.setText(_translate("MainWindow", "totalDiskSpace"))
        self.label_6.setText(_translate("MainWindow", "Used Diskspace:"))
        self.label_7.setText(_translate("MainWindow", "usedDiskSpace"))
        self.label_8.setText(_translate("MainWindow", "Free Diskspace:"))
        self.label_9.setText(_translate("MainWindow", "freeDiskSpace"))
        self.label_2.setText(_translate("MainWindow", "Cover Art"))
        self.label_3.setText(_translate("MainWindow", "Mounted Drive:"))
        self.testButton.setText(_translate("MainWindow", "testing"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuOptions.setTitle(_translate("MainWindow", "Options"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionFormat.setText(_translate("MainWindow", "Format Drive"))
        self.actionArchive_Drive.setText(_translate("MainWindow", "Archive Drive"))
        self.actionCalculate_hash.setText(_translate("MainWindow", "Calculate hash"))
        self.actionDelete_game.setText(_translate("MainWindow", "Delete game"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionMount_Drive.setText(_translate("MainWindow", "Mount Drive"))
        self.actionExit_app.setText(_translate("MainWindow", "Exit app"))
        self.actionAdd_Game.setText(_translate("MainWindow", "Add Game"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
