from PyQt5 import QtCore, QtGui, QtWidgets
from NewprojectPack import SE_newproject
from FP_Dialog import SE_FP_dialog
from TabUI import SE_tab


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(642, 596)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 642, 21))
        self.menubar.setObjectName("menubar")
        self.Menu_file = QtWidgets.QMenu(self.menubar)
        self.Menu_file.setObjectName("Menu_file")
        self.Menu_edit = QtWidgets.QMenu(self.menubar)
        self.Menu_edit.setObjectName("Menu_edit")
        self.Menu_preferences = QtWidgets.QMenu(self.menubar)
        self.Menu_preferences.setObjectName("Menu_preferences")
        self.Menu_metrics = QtWidgets.QMenu(self.menubar)
        self.Menu_metrics.setObjectName("Menu_metrics")
        self.menuFunction_Point = QtWidgets.QMenu(self.Menu_metrics)
        self.menuFunction_Point.setObjectName("menuFunction_Point")
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
        self.Menu_file.addAction(self.File_new)
        self.Menu_file.addAction(self.File_Open)
        self.Menu_file.addAction(self.File_Save)
        self.Menu_file.addAction(self.File_Exit)
        self.menuFunction_Point.addAction(self.actionEnter_FP_Data)
        self.Menu_metrics.addAction(self.menuFunction_Point.menuAction())
        self.menubar.addAction(self.Menu_file.menuAction())
        self.menubar.addAction(self.Menu_edit.menuAction())
        self.menubar.addAction(self.Menu_preferences.menuAction())
        self.menubar.addAction(self.Menu_metrics.menuAction())
        self.menubar.addAction(self.Menu_Project_code.menuAction())
        self.menubar.addAction(self.Menu_Help.menuAction())

        # commentstart

        self.actionEnter_FP_Data.triggered.connect(self.displayfp)
        self.File_new.triggered.connect(lambda: self.newprojdialog())

        # comment end

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def displayfp(self):
        self.Dialog2 = QtWidgets.QDialog()
        self.fpdia = SE_FP_dialog.Ui_Dialog()
        self.fpdia.setupUi(self.Dialog2)
        self.Dialog2.show()
        self.response = self.Dialog2.exec_()

        if self.response == QtWidgets.QDialog.Accepted:
            self.widgetobject = QtWidgets.QWidget()
            self.fp_dialog = self.fpdia.getfp_name()
            self.fpobj = SE_tab.Ui_MainWindow()
            self.fpobj.setupUi(self.widgetobject,self.fp_dialog)


    def newprojdialog(self):
        self.Dialog = QtWidgets.QDialog()
        self.newproj_obj = SE_newproject.Ui_Dialog()
        self.newproj_obj.setupUi(self.Dialog)
        self.Dialog.show()
        self.response = self.Dialog.exec_()

        if self.response == QtWidgets.QDialog.Accepted:
            self.projname_value = self.newproj_obj.getproject_name()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Menu_file.setTitle(_translate("MainWindow", "File"))
        self.Menu_edit.setTitle(_translate("MainWindow", "Edit"))
        self.Menu_preferences.setTitle(_translate("MainWindow", "Preferences"))
        self.Menu_metrics.setTitle(_translate("MainWindow", "Metrics"))
        self.menuFunction_Point.setTitle(_translate("MainWindow", "Function Point"))
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


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
