from PyQt5 import QtCore, QtGui, QtWidgets
from baseSettings import APP_VERSION


class Ui_about_window(object):
    def setupUi(self, about_window):
        about_window.setObjectName("about_window")
        about_window.resize(400, 300)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/ACG.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        about_window.setWindowIcon(icon)
        self.label = QtWidgets.QLabel(about_window)
        self.label.setGeometry(QtCore.QRect(10, 10, 381, 271))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(about_window)
        QtCore.QMetaObject.connectSlotsByName(about_window)

    def retranslateUi(self, about_window):
        _translate = QtCore.QCoreApplication.translate
        about_window.setWindowTitle(_translate("about_window", "ACG Thread Manager - About"))
        self.label.setText(_translate("about_window", f"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">ACG Thread Manager {APP_VERSION}</span></p><p align=\"center\"><br/></p><p align=\"center\"><span style=\" font-size:12pt;\">© 2023 Application Consulting Group</span></p><p align=\"center\"><br/></p><p align=\"center\"><span style=\" font-size:12pt;\">http://www.acgi.com</span></p></body></html>"))
import resources_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    about_window = QtWidgets.QDialog()
    ui = Ui_about_window()
    ui.setupUi(about_window)
    about_window.show()
    sys.exit(app.exec_())
