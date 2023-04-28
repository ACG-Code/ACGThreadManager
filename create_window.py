from PyQt5 import QtCore, QtGui, QtWidgets
from configparser import ConfigParser
from baseSettings import application_path
import os

FILE = os.path.join(application_path, 'config.ini')


class Ui_create_window(object):
    def __init__(self):
        self.config = {}
        self.conf = ConfigParser()

    def str_to_bool(self, choice: str) -> bool:
        return choice.lower() in ['t', 'true', 'y', 'yes', '1', 'on']

    def save_config(self) -> None:
        self.statusbar.showMessage("")
        _cloud = self.str_to_bool(self.cmbCloud.currentText())
        _instance = self.lnServer.text()
        if _cloud:
            _base = self.lnAddress.text()
            if _base == '':
                self.statusbar.showMessage("Address cannot be blank")
            if _base.endswith('/'):
                _base = _base[:-1]
            _base_url = _base + '/tm1/api/' + self.lnServer.text()
        else:
            _address = self.lnAddress.text()
            _port = self.lnPort.text()
            _ssl = self.str_to_bool(self.cmbSSL.currentText())
            _namespace = self.lnAddress_3.text()
            _gateway = self.lnAddress_2.text()
        if _cloud:
            self.config = {
                'cloud': True,
                'address': _base_url
            }
        else:
            self.config = {
                'cloud': False,
                'address': _address,
                'port': int(_port),
                'ssl': _ssl,
                'gateway': _gateway,
                'namespace': _namespace
            }
        self.conf[_instance] = self.config
        self.conf.write(open(FILE, 'a'))
        self.statusbar.showMessage("Configuration Saved")
        self.cmbCloud.setCurrentText('')
        self.lnAddress.setText('')
        self.lnPort.setText('')
        self.cmbSSL.setCurrentText('')
        self.lnAddress_3.setText('')
        self.lnAddress_2.setText('')

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
        self.lnAddress_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lnAddress_2.setGeometry(QtCore.QRect(430, 240, 341, 20))
        self.lnAddress_2.setObjectName("lnAddress_2")
        self.lnAddress_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lnAddress_3.setGeometry(QtCore.QRect(20, 240, 341, 20))
        self.lnAddress_3.setObjectName("lnAddress_3")
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
import resources_rc


if __name__ == "__main__":
    #TODO Tab Order, change names of Namespace and Gateway
    import sys
    app = QtWidgets.QApplication(sys.argv)
    create_window = QtWidgets.QMainWindow()
    ui = Ui_create_window()
    ui.setupUi(create_window)
    create_window.show()
    sys.exit(app.exec_())
