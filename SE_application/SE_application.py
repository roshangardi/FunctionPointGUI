from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QFont
import SE_newproject, SE_common_dialog, SE_functionPoint, SE_UCP, SE_OpenProj_Dialog
from PyQt5.QtWidgets import QFileDialog, QToolTip
import inspect, pickle


class Ui_MainWindow(object):

    def __init__(self):
        self.projname_value = "CECS 543 Metrics Suite"
        self.displaylang_result = 50
        self.lang = "Visual Basic"
        self.tabs_list = []
        self.saveresults = {}
        self.savedvalue = {}
        self.class_names_arr =[]
        QToolTip.setFont(QFont('SansSerif', 10))

    def save_file(self):
        # global self.savedvalue
        saveDialog = QFileDialog()
        saveDialog.setWindowTitle("Save File")
        saveDialog.setAcceptMode(QFileDialog.AcceptSave)
        saveDialog.setNameFilter('MS Files (*.ms)')
        saveDialog.setDefaultSuffix('ms')

        for obj in self.tabs_list:
            self.tab_array.append(obj.save())
        for obj in self.tabs_list:
            self.class_names_arr.append(obj.__class__.__name__)
        self.tab_array.append(self.class_names_arr)

        if saveDialog.exec_() == QFileDialog.Accepted:
            file_name = saveDialog.selectedFiles()
            with open(file_name[0], 'wb') as file:
                pickle.dump(self.tab_array, file)
            file.close()

    def open_file(self):
            openDialog = QFileDialog()
            openDialog.setWindowTitle("Open File")
            openDialog.setAcceptMode(QFileDialog.AcceptOpen)
            openDialog.setNameFilter('MS File (*.ms)')

            if openDialog.exec() == QFileDialog.Accepted:
                file_name = openDialog.selectedFiles()[0]
                with open(file_name, 'rb') as file:
                    self.arr_saveresults = pickle.load(file)
                    classname = self.arr_saveresults[len(self.arr_saveresults)-1]
                    for i in range(len(self.arr_saveresults)-1):
                        if classname[i] == "UCP_Ui_Form":
                            self.saveresults = self.arr_saveresults[i]
                            self.displayUCP()
                            self.ucpobj.restore_data()
                        else:
                            self.saveresults = self.arr_saveresults[i]
                            self.displayfp()
                            self.fpobj.restore_data()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 650)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)

        self.menubar.setGeometry(QtCore.QRect(0, 0, 642, 21))
        self.menubar.setObjectName("menubar")
        self.Menu_file = QtWidgets.QMenu(self.menubar)
        self.Menu_file.setObjectName("Menu_file")
        self.Menu_file.setToolTipsVisible(True)
        self.Menu_edit = QtWidgets.QMenu(self.menubar)
        self.Menu_edit.setObjectName("Menu_edit")
        self.Menu_preferences = QtWidgets.QMenu(self.menubar)
        self.Menu_preferences.setObjectName("Menu_preferences")
        self.Menu_metrics = QtWidgets.QMenu(self.menubar)
        self.Menu_metrics.setObjectName("Menu_metrics")
        self.menuFunction_Point = QtWidgets.QMenu(self.Menu_metrics)
        self.menuFunction_Point.setObjectName("menuFunction_Point")
        self.menuFunction_Point.setToolTipsVisible(True)

        self.menuUCP_Point = QtWidgets.QMenu(self.Menu_metrics)
        self.menuUCP_Point.setObjectName("menuUCP_Point")
        self.menuUCP_Point.setToolTipsVisible(True)

        self.Menu_Project_code = QtWidgets.QMenu(self.menubar)
        self.Menu_Project_code.setObjectName("Menu_Project_code")
        self.Menu_Help = QtWidgets.QMenu(self.menubar)
        self.Menu_Help.setObjectName("Menu_Help")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.File_new = QtWidgets.QAction(MainWindow)
        self.File_new.setObjectName("File_new")
        self.File_Open = QtWidgets.QAction(MainWindow)
        self.File_Open.setObjectName("File_Open")
        self.File_Save = QtWidgets.QAction(MainWindow)
        self.File_Save.setObjectName("File_Save")
        self.File_Exit = QtWidgets.QAction(MainWindow)
        self.File_Exit.setObjectName("File_Exit")
        self.actionEnter_FP_Data = QtWidgets.QAction(MainWindow)
        self.actionEnter_FP_Data.setObjectName("actionEnter_FP_Data")
        self.actionEnter_FP_Data.setEnabled(False)

        self.UCP_action = QtWidgets.QAction(MainWindow)
        self.UCP_action.setObjectName("UCP_action")
        # self.UCP_action.setEnabled(False)

        self.File_Save.setEnabled(False)
        self.Menu_file.addAction(self.File_new)
        self.Menu_file.addAction(self.File_Open)
        self.Menu_file.addAction(self.File_Save)
        self.Menu_file.addAction(self.File_Exit)
        self.menuFunction_Point.addAction(self.actionEnter_FP_Data)
        self.Menu_metrics.addAction(self.menuFunction_Point.menuAction())

        self.menuUCP_Point.addAction(self.UCP_action)
        self.Menu_metrics.addAction(self.menuUCP_Point.menuAction())

        self.menubar.addAction(self.Menu_file.menuAction())
        self.menubar.addAction(self.Menu_edit.menuAction())
        self.menubar.addAction(self.Menu_preferences.menuAction())
        self.menubar.addAction(self.Menu_metrics.menuAction())
        self.menubar.addAction(self.Menu_Project_code.menuAction())
        self.menubar.addAction(self.Menu_Help.menuAction())
        self.File_Exit.triggered.connect(lambda: self.exiter())

        # commentstart
        font = QtGui.QFont()
        font.setPointSize(8)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 900, 641))
        self.tabWidget.setFont(font)
        self.tabWidget.setMouseTracking(False)
        self.tabWidget.setAutoFillBackground(True)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(True)
        self.tabWidget.setMovable(True)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tab_array = []
        self.actionEnter_FP_Data.triggered.connect(self.displayfp)

        self.UCP_action.triggered.connect(self.displayUCP)

        self.actionEnter_FP_Data.setToolTip("This is a widget")
        self.File_new.setToolTip("Tooltip message")
        self.File_new.triggered.connect(lambda: self.newprojdialog(MainWindow))
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget.tabCloseRequested.connect(self.tab_closer)
        self.File_Save.triggered.connect(lambda: self.save_file())
        self.File_Save.setToolTip("Create New project to save")
        self.File_Open.triggered.connect(lambda: self.open_file())
        self.actionEnter_FP_Data.setToolTip("Create project before FP")
        # comment end

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def tab_closer(self, index):
        self.tabWidget.removeTab(index)

    def exiter(self):
        print("Good Bye")
        sys.exit()

    def displayUCP(self):
        Dialog3 = QtWidgets.QDialog()
        self.uc_dialog = SE_common_dialog.Ui_Dialog()
        self.uc_dialog.setupUi(Dialog3)
        Dialog3.show()
        self.response = Dialog3.exec_()

        if self.response == QtWidgets.QDialog.Accepted:
            self.widgetobject = QtWidgets.QWidget()
            self.u_dialog = self.uc_dialog.getfp_name()
            Form = QtWidgets.QWidget()
            # SE_UCP.UCP_Ui_Form()
            self.ucpobj = SE_UCP.UCP_Ui_Form(self.saveresults)
            self.ucpobj.setupUi(Form, self.u_dialog)
            self.tabs_list.append(self.ucpobj)
            self.tabWidget.addTab(Form, self.u_dialog)
            self.tabWidget.setCurrentIndex(self.tabWidget.count() - 1)
            self.File_Save.setEnabled(True)

    def displayfp(self):
        self.Dialog2 = QtWidgets.QDialog()
        self.fpdia = SE_common_dialog.Ui_Dialog()
        self.fpdia.setupUi(self.Dialog2)
        self.Dialog2.show()
        self.response = self.Dialog2.exec_()

        if self.response == QtWidgets.QDialog.Accepted:
            self.widgetobject = QtWidgets.QWidget()
            self.fp_dialog = self.fpdia.getfp_name()
            Form = QtWidgets.QWidget()
            self.fpobj = SE_functionPoint.Ui_Form(self.saveresults)
            self.fpobj.setupUi(Form, self.fp_dialog)
            self.tabs_list.append(self.fpobj)
            self.tabWidget.addTab(Form, self.fp_dialog)
            self.tabWidget.setCurrentIndex(self.tabWidget.count() - 1)
            self.File_Save.setEnabled(True)

    def newprojdialog(self, MainWindow):
        self.Dialog = QtWidgets.QDialog()
        self.newproj_obj = SE_newproject.Ui_Dialog()
        self.newproj_obj.setupUi(self.Dialog)
        self.Dialog.show()
        self.response = self.Dialog.exec_()

        if self.response == QtWidgets.QDialog.Accepted:
            self.actionEnter_FP_Data.setEnabled(True)
            self.projname_value = self.newproj_obj.getproject_name()
            _translate = QtCore.QCoreApplication.translate
            MainWindow.setWindowTitle(_translate("MainWindow", "CECS 543 Metrics Suite - " + self.projname_value))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowIcon(QtGui.QIcon("metrics.png"))
        self.Menu_file.setTitle(_translate("MainWindow", "File"))
        self.Menu_edit.setTitle(_translate("MainWindow", "Edit"))
        self.Menu_preferences.setTitle(_translate("MainWindow", "Preferences"))
        self.Menu_metrics.setTitle(_translate("MainWindow", "Metrics"))
        self.menuFunction_Point.setTitle(_translate("MainWindow", "Function Point"))
        self.menuUCP_Point.setTitle(_translate("MainWindow", "UCP Point"))
        self.Menu_Project_code.setTitle(_translate("MainWindow", "Project code"))
        self.Menu_Help.setTitle(_translate("MainWindow", "Help"))
        self.File_new.setText(_translate("MainWindow", "New"))
        self.File_new.setStatusTip(_translate("MainWindow", "Create a new file"))
        self.File_new.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.File_Open.setText(_translate("MainWindow", "Open"))
        self.File_Save.setText(_translate("MainWindow", "Save"))
        self.File_Save.setStatusTip(_translate("MainWindow", "Save the file"))
        self.File_Save.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.File_Exit.setText(_translate("MainWindow", "Exit"))
        self.actionEnter_FP_Data.setText(_translate("MainWindow", "Enter FP Data"))
        self.actionEnter_FP_Data.setShortcut(_translate("MainWindow", "Ctrl+F"))

        self.UCP_action.setText(_translate("MainWindow", "Calculate UCP"))
        self.UCP_action.setShortcut(_translate("MainWindow", "Ctrl+P"))
        ##
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Tab 1"))


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

    def closeEvent(self, event):
        super().closeEvent(event)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    QtCore.QCoreApplication.setOrganizationName("Roshan")
    QtCore.QCoreApplication.setApplicationName("CECS 543 Metrics Suite")
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
