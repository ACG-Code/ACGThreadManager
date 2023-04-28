from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/ACG.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.cmbConfig = QtWidgets.QComboBox(self.centralwidget)
        self.cmbConfig.setGeometry(QtCore.QRect(290, 40, 181, 22))
        self.cmbConfig.setObjectName("cmbConfig")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(290, 10, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.lnUser = QtWidgets.QLineEdit(self.centralwidget)
        self.lnUser.setGeometry(QtCore.QRect(30, 130, 191, 31))
        self.lnUser.setObjectName("lnUser")
        self.lnPassword = QtWidgets.QLineEdit(self.centralwidget)
        self.lnPassword.setGeometry(QtCore.QRect(570, 130, 191, 31))
        self.lnPassword.setInputMask("")
        self.lnPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lnPassword.setObjectName("lnPassword")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 100, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(570, 100, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.btnUpdate = QtWidgets.QPushButton(self.centralwidget)
        self.btnUpdate.setGeometry(QtCore.QRect(310, 180, 151, 31))
        self.btnUpdate.setObjectName("btnUpdate")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(0, 220, 791, 331))
        self.groupBox.setObjectName("groupBox")
        self.tblThreads = QtWidgets.QTableView(self.groupBox)
        self.tblThreads.setGeometry(QtCore.QRect(10, 130, 771, 192))
        self.tblThreads.setObjectName("tblThreads")
        self.lnThreadID = QtWidgets.QLineEdit(self.groupBox)
        self.lnThreadID.setGeometry(QtCore.QRect(10, 80, 151, 31))
        self.lnThreadID.setObjectName("lnThreadID")
        self.lnUserID = QtWidgets.QLineEdit(self.groupBox)
        self.lnUserID.setGeometry(QtCore.QRect(630, 80, 151, 31))
        self.lnUserID.setObjectName("lnUserID")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(10, 50, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(630, 50, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(310, 80, 151, 31))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuSetup = QtWidgets.QMenu(self.menubar)
        self.menuSetup.setObjectName("menuSetup")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionConfiguration = QtWidgets.QAction(MainWindow)
        self.actionConfiguration.setObjectName("actionConfiguration")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionEdit_Configuration = QtWidgets.QAction(MainWindow)
        self.actionEdit_Configuration.setObjectName("actionEdit_Configuration")
        self.menuSetup.addAction(self.actionConfiguration)
        self.menuSetup.addAction(self.actionEdit_Configuration)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuSetup.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ACG Thread Manager"))
        self.label.setText(_translate("MainWindow", "Choose Configuration"))
        self.label_2.setText(_translate("MainWindow", "Username"))
        self.label_3.setText(_translate("MainWindow", "Passsword"))
        self.btnUpdate.setText(_translate("MainWindow", "Update Threads"))
        self.groupBox.setTitle(_translate("MainWindow", "Threads"))
        self.label_4.setText(_translate("MainWindow", "Thread ID"))
        self.label_5.setText(_translate("MainWindow", "User ID"))
        self.pushButton.setText(_translate("MainWindow", "Cancel Threads"))
        self.menuSetup.setTitle(_translate("MainWindow", "Setup"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionConfiguration.setText(_translate("MainWindow", "Create Configuration"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionEdit_Configuration.setText(_translate("MainWindow", "Edit Configuration"))
import resources_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())