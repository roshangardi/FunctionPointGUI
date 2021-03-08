from PyQt5 import QtCore, QtGui, QtWidgets
from NewprojectPack import SE_newproject
from FP_Dialog import SE_FP_dialog
from Duplicate_tab_UI import SE_tab_duplicate
from PyQt5.QtCore import QSettings, QPoint
from PyQt5.QtWidgets import QFileDialog
import inspect


def restore(obje, settings):
    for name, obj in inspect.getmembers(obje):
        if isinstance(obj, QtWidgets.QComboBox):
            index = obj.currentIndex()  # get current region from combobox
            # text   = obj.itemText(index)   # get the text for new selected index
            name = obj.objectName()

            value = settings.value(name)

            if value == "":
                continue

            index = obj.findText(value)  # get the corresponding index for specified string in combobox

            if index == -1:  # add to list if not found
                obj.insertItems(0, [value])
                index = obj.findText(value)
                obj.setCurrentIndex(index)
            else:
                obj.setCurrentIndex(index)  # preselect a combobox value by index

        if isinstance(obj, QtWidgets.QLineEdit):
            name = obj.objectName()
            value = settings.value(name)  # get stored value from registry
            obj.setText(value)  # restore lineEditFile

        if isinstance(obj, QtWidgets.QCheckBox):
            name = obj.objectName()
            value = settings.value(name)  # get stored value from registry
            if value != None:
                obj.setCheckState(value)  # restore checkbox

        # if isinstance(obj, QRadioButton):
    # finfo = QtCore.QFileInfo(settings.fileName())
    # if finfo.exists() and finfo.isFile():
    #     print("Yes, It's a file")
    #     for w in QtWidgets.qApp.allWidgets():
    #         mo = w.metaObject()
    #         if w.objectName() and not w.objectName().startswith("qt_"):
    #             settings.beginGroup(w.objectName())
    #             for i in range(mo.propertyCount(), mo.propertyOffset() - 1, -1):
    #                 prop = mo.property(i)
    #                 if prop.isWritable():
    #                     name = prop.name()
    #                     val = settings.value(name, w.property(name))
    #                     if str(val).isdigit():
    #                         val = int(val)
    #                     w.setProperty(name, val)
    #             settings.endGroup()


def save(obje, settings):
    for name, obj in inspect.getmembers(obje):
        if isinstance(obj, QtWidgets.QComboBox):
            name = obj.objectName()  # get combobox name
            index = obj.currentIndex()  # get current index from combobox
            text = obj.itemText(index)  # get the text for current index
            settings.setValue(name, text)  # save combobox selection to registry

        if isinstance(obj, QtWidgets.QLineEdit):
            name = obj.objectName()
            value = obj.text()
            settings.setValue(name, value)  # save ui values, so they can be restored next time

        if isinstance(obj, QtWidgets.QCheckBox):
            name = obj.objectName()
            state = obj.checkState()
            settings.setValue(name, state)

    # for w in QtWidgets.qApp.allWidgets():
    #     mo = w.metaObject()
    #     if w.objectName() and not w.objectName().startswith("qt_"):
    #         settings.beginGroup(w.objectName())
    #         for i in range(mo.propertyCount()):
    #             prop = mo.property(i)
    #             name = prop.name()
    #             if prop.isWritable():
    #                 settings.setValue(name, w.property(name))
    #         settings.endGroup()


class Ui_MainWindow(object):

    def __init__(self):
        # self.settings = QSettings('Roshan', 'CECS_543')
        self.projname_value = "CECS 543 Metrics Suite"
        self.displaylang_result = 50
        self.lang = "Visual Basic"
        self.tabs_list = []

    def save_file(self):
        option = QFileDialog.Options()
        option |= QFileDialog.DontUseNativeDialog
        file = QFileDialog.getSaveFileName(self.centralwidget, "Save your application status", "default.txt",
                                           "All Files (*)", options=option)
        print(file[0])

    def open_file(self):
        option = QFileDialog.Options()
        option |= QFileDialog.DontUseNativeDialog
        file = QFileDialog.getOpenFileName(self.centralwidget, "Open your application", "Default File", "All Files (*)",
                                           options=option)
        print(file)

    def open_multi_file(self):
        option = QFileDialog.Options()
        option |= QFileDialog.DontUseNativeDialog
        file = QFileDialog.getOpenFileNames(self.centralwidget, "Open your application", "Default File",
                                            "All Files (*)",
                                            options=option)
        print(file)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(680, 650)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        # MainWindow.setStyleSheet(self.stylesheet)
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
        self.actionEnter_FP_Data.setEnabled(False)
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
        self.File_Exit.triggered.connect(lambda: self.exiter())

        # commentstart
        font = QtGui.QFont()
        font.setPointSize(8)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 751, 641))
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
        self.File_new.triggered.connect(lambda: self.newprojdialog(MainWindow))
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget.tabCloseRequested.connect(self.tab_closer)
        self.File_Save.triggered.connect(lambda: self.save_file())
        self.File_Open.triggered.connect(lambda: self.open_multi_file())
        # comment end

        # Saving functionality
        # Saving end

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def tab_closer(self, index):
        self.tabWidget.removeTab(index)

    def exiter(self):
        print("Good Bye")
        sys.exit()

    def displayfp(self):
        self.Dialog2 = QtWidgets.QDialog()
        self.fpdia = SE_FP_dialog.Ui_Dialog()
        self.fpdia.setupUi(self.Dialog2)
        self.Dialog2.show()
        self.response = self.Dialog2.exec_()

        if self.response == QtWidgets.QDialog.Accepted:
            self.widgetobject = QtWidgets.QWidget()
            self.fp_dialog = self.fpdia.getfp_name()
            Form = QtWidgets.QWidget()
            self.fpobj = SE_tab_duplicate.Ui_Form()
            self.fpobj.setupUi(Form, self.fp_dialog)
            self.tabs_list.append(self.fpobj)
            self.tabWidget.addTab(Form, self.fp_dialog)
            self.tabWidget.setCurrentIndex(self.tabWidget.count() - 1)

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
            MainWindow.setWindowTitle(_translate("MainWindow", "CECS 543 Metrics Suite - "+self.projname_value))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        # MainWindow.setWindowTitle(_translate("MainWindow", self.projname_value))
        MainWindow.setWindowIcon(QtGui.QIcon("metrics.png"))
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
        ##
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Tab 1"))


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.settings = QtCore.QSettings()
        restore(self, self.settings)
        print(self.settings.fileName())

    def closeEvent(self, event):
        save(self, self.settings)
        super().closeEvent(event)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    QtCore.QCoreApplication.setOrganizationName("Roshan")
    # QtCore.QCoreApplication.setOrganizationDomain("abc.com")
    QtCore.QCoreApplication.setApplicationName("CECS 543 Metrics Suite")
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
