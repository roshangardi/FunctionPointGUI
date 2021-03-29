from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def __init__(self):
        self.fp_name = "New Tab"

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(390, 158)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(-70, 80, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(60, 20, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.name_of_fp_lineEdit = QtWidgets.QLineEdit(Dialog)
        self.name_of_fp_lineEdit.setGeometry(QtCore.QRect(60, 50, 281, 21))
        self.name_of_fp_lineEdit.setObjectName("name_of_fp_lineEdit")
        self.name_of_fp_lineEdit.setFocus()

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        # Comment Start
        self.name_of_fp_lineEdit.textChanged.connect(self.setpfp_name)
        # Comment End

    def setpfp_name(self):
        self.fp_name = self.name_of_fp_lineEdit.text()

    def getfp_name(self):
        return self.fp_name

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "What do you want to name it?"))
        Dialog.setWindowIcon(QtGui.QIcon(r"/Static/metrics.png"))
        self.label.setText(_translate("Dialog", "Name:"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
