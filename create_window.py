import os
from configparser import ConfigParser

from PyQt5 import QtCore, QtGui, QtWidgets

import resources_rc
from baseSettings import application_path
from utilities import str_to_bool

FILE = os.path.join(application_path, 'config.ini')
# This line is to force the retaining of the resources_rc import
var = resources_rc


class Ui_create_window(object):

    def __init__(self):
        self.config = {}
        self.conf = ConfigParser()

    def save_config(self) -> None:
        self.statusbar.showMessage("")
        _cloud = str_to_bool(self.cmbCloud.currentText())
        _instance = self.lnServer.text()
        if _cloud:
            _base = self.lnAddress.text()
            if _base == '':
                self.statusbar.showMessage("Address field cannot be blank")
            if _base.endswith('/'):
                _base = _base[:-1]
            _base_url = _base + r'/tm1/api' + _instance
        else:
            address = self.lnAddress.text()
            port = int(self.lnPort.text())
            ssl = self.cmbSSL.currentText()
            gateway = self.lnGateway.text()
            namespace = self.lnNamespcae.text()
        if _cloud:
            self.config = {
                'cloud': True,
                'address': _base_url
            }
        else:
            self.config = {
                'cloud': False,
                'address': address,
                'port': port,
                'ssl': ssl,
                'gateway': gateway,
                'namespace': namespace
            }
        self.conf[_instance] = self.config
        self.conf.write(open(FILE, 'a'))
        self.statusbar.showMessage("Configuration Saved")
        self.cmbCloud.currentText('')
        self.lnAddress.setText('')
        self.lnPort.setText('')
        self.lnServer.setText('')
        self.cmbSSL.currentText('')
        self.lnGateway.setText('')
        self.lnNamespcae.setText('')

    def setupUi(self, create_window):
        create_window.setObjectName("create_window")
        create_window.resize(800, 436)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/ACG.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        create_window.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(create_window)
        self.centralwidget.setObjectName("centralwidget")
        self.cmbCloud = QtWidgets.QComboBox(self.centralwidget)
        self.cmbCloud.setGeometry(QtCore.QRect(20, 40, 181, 22))
        self.cmbCloud.setObjectName("cmbCloud")
        self.lnAddress = QtWidgets.QLineEdit(self.centralwidget)
        self.lnAddress.setGeometry(QtCore.QRect(432, 40, 341, 20))
        self.lnAddress.setObjectName("lnAddress")
        self.lnPort = QtWidgets.QLineEdit(self.centralwidget)
        self.lnPort.setGeometry(QtCore.QRect(20, 140, 181, 20))
        self.lnPort.setObjectName("lnPort")
        self.lnServer = QtWidgets.QLineEdit(self.centralwidget)
        self.lnServer.setGeometry(QtCore.QRect(280, 140, 171, 20))
        self.lnServer.setObjectName("lnServer")
        self.cmbSSL = QtWidgets.QComboBox(self.centralwidget)
        self.cmbSSL.setGeometry(QtCore.QRect(530, 140, 151, 22))
        self.cmbSSL.setObjectName("cmbSSL")
        self.lnGateway = QtWidgets.QLineEdit(self.centralwidget)
        self.lnGateway.setGeometry(QtCore.QRect(430, 240, 341, 20))
        self.lnGateway.setObjectName("lnGateway")
        self.lnNamespcae = QtWidgets.QLineEdit(self.centralwidget)
        self.lnNamespcae.setGeometry(QtCore.QRect(20, 240, 341, 20))
        self.lnNamespcae.setObjectName("lnNamespcae")
        self.btnSave = QtWidgets.QPushButton(self.centralwidget)
        self.btnSave.setGeometry(QtCore.QRect(330, 310, 111, 41))
        self.btnSave.setObjectName("btnSave")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 181, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(430, 10, 341, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 110, 181, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(280, 110, 171, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(530, 110, 151, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(20, 210, 341, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(430, 210, 341, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        create_window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(create_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        create_window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(create_window)
        self.statusbar.setObjectName("statusbar")
        create_window.setStatusBar(self.statusbar)

        self.retranslateUi(create_window)
        QtCore.QMetaObject.connectSlotsByName(create_window)
        create_window.setTabOrder(self.cmbCloud, self.lnAddress)
        create_window.setTabOrder(self.lnAddress, self.lnPort)
        create_window.setTabOrder(self.lnPort, self.lnServer)
        create_window.setTabOrder(self.lnServer, self.cmbSSL)
        create_window.setTabOrder(self.cmbSSL, self.lnNamespcae)
        create_window.setTabOrder(self.lnNamespcae, self.lnGateway)
        create_window.setTabOrder(self.lnGateway, self.btnSave)
        bools = ['', 'True', 'False']
        self.cmbCloud.addItems(bools)
        self.cmbSSL.addItems(bools)
        self.statusbar.showMessage("Ready")
        self.btnSave.clicked.connect(self.save_config)

    def retranslateUi(self, create_window):
        _translate = QtCore.QCoreApplication.translate
        create_window.setWindowTitle(_translate("create_window", "ACG Thread Manager - Setup Connection"))
        self.btnSave.setText(_translate("create_window", "Save Configuration"))
        self.label.setText(_translate("create_window", "IBM Cloud"))
        self.label_2.setText(_translate("create_window", "Address"))
        self.label_3.setText(_translate("create_window", "HTTP Port Number"))
        self.label_4.setText(_translate("create_window", "Instance Name"))
        self.label_5.setText(_translate("create_window", "Use SSL"))
        self.label_6.setText(_translate("create_window", "CAM Namespace ID"))
        self.label_7.setText(_translate("create_window", "SSO Gateway"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    create_window = QtWidgets.QMainWindow()
    ui = Ui_create_window()
    ui.setupUi(create_window)
    create_window.show()
    sys.exit(app.exec_())
