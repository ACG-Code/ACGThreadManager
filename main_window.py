import pandas as pd
from PyQt5 import QtCore, QtGui, QtWidgets
from TM1py import TM1Service
from PyQt5.QtCore import Qt, QAbstractTableModel
import resources_rc
from about_window import Ui_about_window
from create_window import Ui_create_window
from edit_window import Ui_edit_window
from utilities import get_sections, retrieve_tm1_config
# This line is to force the retaining of the resources_rc import
var = resources_rc


class pandasModel(QAbstractTableModel):

    def __init__(self, data):
        QAbstractTableModel.__init__(self)
        self._data = data

    def rowCount(self, parent=None):
        return self._data.shape[0]

    def columnCount(self, parent=None):
        return self._data.shape[1]

    def data(self, index, role=Qt.DisplayRole):
        if index.isValid():
            if role == Qt.DisplayRole:
                return str(self._data.iloc[index.row(), index.column()])
        return None

    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self._data.columns[col]
        return None


class Ui_MainWindow(object):

    def __init__(self):
        self._config = {}

    def open_about(self) -> None:
        self.window = QtWidgets.QDialog()
        self.ui = Ui_about_window()
        self.ui.setupUi(self.window)
        self.window.show()

    def open_setup(self) -> None:
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_create_window()
        self.ui.setupUi(self.window)
        self.window.show()

    def open_edit(self) -> None:
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_edit_window()
        self.ui.setupUi(self.window)
        self.window.show()

    def get_config(self) -> None:
        self.cmbConfig.clear()
        sections = get_sections()
        self.cmbConfig.addItems(sections)

    def get_threads(self) -> None:
        _instance = self.cmbConfig.currentText()
        self._config = retrieve_tm1_config(_instance)
        _user = self.lnUser.text()
        _password = self.lnPassword.text()
        thread_list = []
        self._config['user'] = _user
        self._config['password'] = _password
        with TM1Service(**self._config) as tm1:
            threads = tm1.monitoring.get_threads()
            for thread in threads:
                thread_list.append(thread)
        df = pd.DataFrame(thread_list)
        self.model = pandasModel(df)
        self.tblThreads.setModel(self.model)

    def cancel_thread(self) -> None:
        row_data = self.get_selected_row()
        if row_data:
            self.kill_selected_threads(selection="thread", thread=row_data[0][0])
            self.statusbar.showMessage("Thread cancelled")
        self.get_threads()
        self.statusbar.showMessage("Ready")

    def get_selected_row(self) -> list or None:
        rows = {index.row() for index in self.tblThreads.selectionModel().selectedIndexes()}
        if rows:
            output = []
            for row in rows:
                row_data = []
                for column in range(self.tblThreads.model().columnCount()):
                    index = self.tblThreads.model().index(row, column)
                    row_data.append(index.data())
                output.append(row_data)
            return output
        else:
            return None

    def user_kill(self) -> None:
        row_data = self.get_selected_row()
        if row_data:
            self.kill_selected_threads(selection='user', thread=row_data[0][2])
            self.statusbar.showMessage("Thread cancelled")
        self.get_threads()
        self.statusbar.showMessage("Ready")

    def kill_selected_threads(self, selection: str, thread: str):
        with TM1Service(**self._config) as tm1:
            all_threads = tm1.monitoring.get_threads()
            for _thread in all_threads:
                if selection == 'user':
                    if _thread['Name'] == thread:
                        tm1.monitoring.cancel_thread(_thread['ID'])
                elif selection == 'thread':
                    if _thread['ID'] == int(thread):
                        tm1.monitoring.cancel_thread(_thread['ID'])

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
        self.btnThreadKill = QtWidgets.QPushButton(self.groupBox)
        self.btnThreadKill.setGeometry(QtCore.QRect(20, 80, 151, 31))
        self.btnThreadKill.setObjectName("btnThreadKill")
        self.btnUserKill = QtWidgets.QPushButton(self.groupBox)
        self.btnUserKill.setGeometry(QtCore.QRect(620, 80, 151, 31))
        self.btnUserKill.setObjectName("btnUserKill")
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
        self.actionAbout.triggered.connect(self.open_about)
        self.actionConfiguration.triggered.connect(self.open_setup)
        self.actionEdit_Configuration.triggered.connect(self.open_edit)
        self.btnUpdate.clicked.connect(self.get_threads)
        self.btnThreadKill.clicked.connect(self.cancel_thread)
        self.btnUserKill.clicked.connect(self.user_kill)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.statusbar.showMessage("Ready")
        self.get_config()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ACG Thread Manager"))
        self.label.setText(_translate("MainWindow", "Choose Configuration"))
        self.label_2.setText(_translate("MainWindow", "Username"))
        self.label_3.setText(_translate("MainWindow", "Password"))
        self.btnUpdate.setText(_translate("MainWindow", "Update Threads"))
        self.groupBox.setTitle(_translate("MainWindow", "Threads"))
        self.label_4.setText(_translate("MainWindow", "Thread ID"))
        self.label_5.setText(_translate("MainWindow", "User ID"))
        self.btnThreadKill.setText(_translate("MainWindow", "Cancel Thread"))
        self.btnUserKill.setText(_translate("MainWindow", "Cancel User Threads"))
        self.menuSetup.setTitle(_translate("MainWindow", "Setup"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionConfiguration.setText(_translate("MainWindow", "Create Configuration"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionEdit_Configuration.setText(_translate("MainWindow", "Edit Configuration"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
