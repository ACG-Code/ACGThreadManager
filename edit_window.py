from PyQt5 import QtCore, QtGui, QtWidgets
from configparser import ConfigParser
import os
from baseSettings import application_path
from utilities import get_tm1_config, str_to_bool

FILE = os.path.join(application_path, 'config.ini')


class Ui_edit_window(object):

    def __init__(self):
        self.config = {}
        self.conf = ConfigParser()

    def update_config_list(self) -> None:
        self.cmbConfig.clear()
        conf_list = ['']
        confg = ConfigParser()
        confg.read(FILE)
        for section in confg.sections():
            conf_list.append(section)
        self.cmbConfig.addItems(conf_list)

    def retrieve_config(self) -> None:
        self.statusbar.showMessage("Save Configuration to apply changes")
        _instance = self.cmbConfig.currentText()
        _dict = get_tm1_config(_instance)
        _cloud = str_to_bool(_dict['cloud'])
        if _cloud:
            self.cmbCloud.setCurrentText('True')
            self.lnAddress.setText(str(_dict['address']))
            self.lnServer.setText(str(_dict['server']))
        else:
            self.cmbCloud.setCurrentText(_dict['cloud'])
            self.lnAddress.setText(str(_dict['address']))
            self.lnPort.setText(str(_dict['port']))
            self.lnServer.setText(str(_dict['server']))
            self.cmbSSL.setCurrentText(_dict['ssl'])
            self.lnGateway.setText(str(_dict['gateway']))
            self.lnNamespace.setText(str(_dict['namespace']))

    def save_config(self) -> None:
        self.statusbar.showMessage("Save Clicked")

    def setupUi(self, edit_window):
        edit_window.setObjectName("edit_window")
        edit_window.resize(800, 520)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/ACG.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        edit_window.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(edit_window)
        self.centralwidget.setObjectName("centralwidget")
        self.cmbCloud = QtWidgets.QComboBox(self.centralwidget)
        self.cmbCloud.setGeometry(QtCore.QRect(20, 130, 181, 22))
        self.cmbCloud.setObjectName("cmbCloud")
        self.lnAddress = QtWidgets.QLineEdit(self.centralwidget)
        self.lnAddress.setGeometry(QtCore.QRect(432, 130, 341, 20))
        self.lnAddress.setObjectName("lnAddress")
        self.lnPort = QtWidgets.QLineEdit(self.centralwidget)
        self.lnPort.setGeometry(QtCore.QRect(20, 230, 181, 20))
        self.lnPort.setObjectName("lnPort")
        self.lnServer = QtWidgets.QLineEdit(self.centralwidget)
        self.lnServer.setGeometry(QtCore.QRect(280, 230, 171, 20))
        self.lnServer.setObjectName("lnServer")
        self.cmbSSL = QtWidgets.QComboBox(self.centralwidget)
        self.cmbSSL.setGeometry(QtCore.QRect(530, 230, 151, 22))
        self.cmbSSL.setObjectName("cmbSSL")
        self.lnGateway = QtWidgets.QLineEdit(self.centralwidget)
        self.lnGateway.setGeometry(QtCore.QRect(430, 330, 341, 20))
        self.lnGateway.setObjectName("lnGateway")
        self.lnNamespace = QtWidgets.QLineEdit(self.centralwidget)
        self.lnNamespace.setGeometry(QtCore.QRect(20, 330, 341, 20))
        self.lnNamespace.setObjectName("lnNamespace")
        self.btnSave = QtWidgets.QPushButton(self.centralwidget)
        self.btnSave.setGeometry(QtCore.QRect(330, 400, 111, 41))
        self.btnSave.setObjectName("btnSave")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 100, 181, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(430, 100, 341, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 200, 181, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(280, 200, 171, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(530, 200, 151, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(20, 300, 341, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(430, 300, 341, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.cmbConfig = QtWidgets.QComboBox(self.centralwidget)
        self.cmbConfig.setGeometry(QtCore.QRect(290, 40, 181, 22))
        self.cmbConfig.setObjectName("cmbConfig")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(290, 10, 181, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        edit_window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(edit_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        edit_window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(edit_window)
        self.statusbar.setObjectName("statusbar")
        edit_window.setStatusBar(self.statusbar)

        self.retranslateUi(edit_window)
        QtCore.QMetaObject.connectSlotsByName(edit_window)
        edit_window.setTabOrder(self.cmbConfig, self.cmbCloud)
        edit_window.setTabOrder(self.cmbCloud, self.lnAddress)
        edit_window.setTabOrder(self.lnAddress, self.lnPort)
        edit_window.setTabOrder(self.lnPort, self.lnServer)
        edit_window.setTabOrder(self.lnServer, self.cmbSSL)
        edit_window.setTabOrder(self.cmbSSL, self.lnNamespace)
        edit_window.setTabOrder(self.lnNamespace, self.lnGateway)
        edit_window.setTabOrder(self.lnGateway, self.btnSave)
        bools = ['', 'True', 'False']
        self.cmbCloud.addItems(bools)
        self.cmbSSL.addItems(bools)
        self.statusbar.showMessage("Ready")
        self.update_config_list()
        self.cmbConfig.currentTextChanged.connect(self.retrieve_config)
        self.btnSave.clicked.connect(self.save_config)

    def retranslateUi(self, edit_window):
        _translate = QtCore.QCoreApplication.translate
        edit_window.setWindowTitle(_translate("edit_window", "ACG Thread Manager - Setup Connection"))
        self.btnSave.setText(_translate("edit_window", "Save Configuration"))
        self.label.setText(_translate("edit_window", "IBM Cloud"))
        self.label_2.setText(_translate("edit_window", "Address"))
        self.label_3.setText(_translate("edit_window", "HTTP Port Number"))
        self.label_4.setText(_translate("edit_window", "Instance Name"))
        self.label_5.setText(_translate("edit_window", "Use SSL"))
        self.label_6.setText(_translate("edit_window", "CAM Namespace ID"))
        self.label_7.setText(_translate("edit_window", "SSO Gateway"))
        self.label_8.setText(_translate("edit_window", "Choose Existing Configuration"))
import resources_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    edit_window = QtWidgets.QMainWindow()
    ui = Ui_edit_window()
    ui.setupUi(edit_window)
    edit_window.show()
    sys.exit(app.exec_())
