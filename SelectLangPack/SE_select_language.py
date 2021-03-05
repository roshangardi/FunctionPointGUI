from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def __init__(self):
        self.result = 0

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(498, 515)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(-140, 440, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(40, 50, 160, 381))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.verticalLayoutWidget.setFont(font)
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.assembler_radio_btn = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.assembler_radio_btn.setObjectName("assembler_radio_btn")
        self.verticalLayout.addWidget(self.assembler_radio_btn)
        self.ada_radio_btn = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.ada_radio_btn.setObjectName("ada_radio_btn")
        self.verticalLayout.addWidget(self.ada_radio_btn)
        self.c_radio_btn = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.c_radio_btn.setObjectName("c_radio_btn")
        self.verticalLayout.addWidget(self.c_radio_btn)
        self.cplus_radio_btn = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.cplus_radio_btn.setObjectName("cplus_radio_btn")
        self.verticalLayout.addWidget(self.cplus_radio_btn)
        self.csharp_radio_btn = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.csharp_radio_btn.setObjectName("csharp_radio_btn")
        self.verticalLayout.addWidget(self.csharp_radio_btn)
        self.cobol_radio_btn = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.cobol_radio_btn.setObjectName("cobol_radio_btn")
        self.verticalLayout.addWidget(self.cobol_radio_btn)
        self.fortran_radio_btn = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.fortran_radio_btn.setObjectName("fortran_radio_btn")
        self.verticalLayout.addWidget(self.fortran_radio_btn)
        self.html_radio_btn = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.html_radio_btn.setObjectName("html_radio_btn")
        self.verticalLayout.addWidget(self.html_radio_btn)
        self.java_radio_btn = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.java_radio_btn.setObjectName("java_radio_btn")
        self.verticalLayout.addWidget(self.java_radio_btn)
        self.javascript_radio_btn = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.javascript_radio_btn.setObjectName("javascript_radio_btn")
        self.verticalLayout.addWidget(self.javascript_radio_btn)
        self.vbscript_radio_btn = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.vbscript_radio_btn.setObjectName("vbscript_radio_btn")
        self.verticalLayout.addWidget(self.vbscript_radio_btn)
        self.visualB_radio_btn = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.visualB_radio_btn.setObjectName("visualB_radio_btn")
        self.verticalLayout.addWidget(self.visualB_radio_btn)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(40, 20, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def calculate_lang(self):
        if self.assembler_radio_btn.isChecked():
            self.result = (337, "Assembler")
        elif self.ada_radio_btn.isChecked():
            self.result = (154, "ADA")
        elif self.c_radio_btn.isChecked():
            self.result = (148,"C")
        elif self.cplus_radio_btn.isChecked():
            self.result = (59, "C++")
        elif self.csharp_radio_btn.isChecked():
            self.result = (58, "C#")
        elif self.cobol_radio_btn.isChecked():
            self.result = (80, "COBOL")
        elif self.fortran_radio_btn.isChecked():
            self.result = (90, "FORTRAN")
        elif self.html_radio_btn.isChecked():
            self.result = (43, "HTML")
        elif self.java_radio_btn.isChecked():
            self.result = (55, "Java")
        elif self.javascript_radio_btn.isChecked():
            self.result = (54, "JavaScript")
        elif self.vbscript_radio_btn.isChecked():
            self.result = (38, "VB Script")
        elif self.visualB_radio_btn.isChecked():
            self.result = (50, "Visual Basic")

        self.setvalue(self.result)

    def setvalue(self,value):
        self.result = value

    def getvalue(self):
        return self.result

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Language Selector"))
        Dialog.setWindowIcon(QtGui.QIcon(r"C:\Users\rosha\PycharmProjects\FunctionPointGUIprogram\Static"
                                             r"\metrics.png"))
        self.assembler_radio_btn.setText(_translate("Dialog", "Assembler"))
        self.assembler_radio_btn.toggled.connect(lambda: self.calculate_lang())
        self.ada_radio_btn.setText(_translate("Dialog", "Ada 95"))
        self.ada_radio_btn.toggled.connect(lambda: self.calculate_lang())
        self.c_radio_btn.setText(_translate("Dialog", "C"))
        self.c_radio_btn.toggled.connect(lambda: self.calculate_lang())
        self.cplus_radio_btn.setText(_translate("Dialog", "C++"))
        self.cplus_radio_btn.toggled.connect(lambda: self.calculate_lang())
        self.csharp_radio_btn.setText(_translate("Dialog", "C#"))
        self.csharp_radio_btn.toggled.connect(lambda: self.calculate_lang())
        self.cobol_radio_btn.setText(_translate("Dialog", "COBOL"))
        self.cobol_radio_btn.toggled.connect(lambda: self.calculate_lang())
        self.fortran_radio_btn.setText(_translate("Dialog", "FORTRAN"))
        self.fortran_radio_btn.toggled.connect(lambda: self.calculate_lang())
        self.html_radio_btn.setText(_translate("Dialog", "HTML"))
        self.html_radio_btn.toggled.connect(lambda: self.calculate_lang())
        self.java_radio_btn.setText(_translate("Dialog", "Java"))
        self.java_radio_btn.toggled.connect(lambda: self.calculate_lang())
        self.javascript_radio_btn.setText(_translate("Dialog", "JavaScript"))
        self.javascript_radio_btn.toggled.connect(lambda: self.calculate_lang())
        self.vbscript_radio_btn.setText(_translate("Dialog", "VBScript"))
        self.vbscript_radio_btn.toggled.connect(lambda: self.calculate_lang())
        self.visualB_radio_btn.setText(_translate("Dialog", "Visual Basic"))
        self.visualB_radio_btn.toggled.connect(lambda: self.calculate_lang())
        self.label.setText(_translate("Dialog", "Select One Language"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
