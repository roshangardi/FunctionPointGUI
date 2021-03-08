from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def __init__(self):
        self.project_name = ""

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(653, 568)
        font = QtGui.QFont()
        font.setPointSize(10)
        Dialog.setFont(font)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(-140, 510, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(190, 40, 301, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(50, 150, 121, 81))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.projectname_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.projectname_label.setFont(font)
        self.projectname_label.setObjectName("projectname_label")
        self.verticalLayout.addWidget(self.projectname_label)
        self.productname_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.productname_label.setFont(font)
        self.productname_label.setObjectName("productname_label")
        self.verticalLayout.addWidget(self.productname_label)
        self.creator_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.creator_label.setFont(font)
        self.creator_label.setObjectName("creator_label")
        self.verticalLayout.addWidget(self.creator_label)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(230, 150, 160, 80))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.projectname_lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.projectname_lineEdit.setObjectName("projectname_lineEdit")
        self.projectname_lineEdit.setFocus()
        self.verticalLayout_2.addWidget(self.projectname_lineEdit)
        self.productname_lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.productname_lineEdit.setObjectName("productname_lineEdit")
        self.verticalLayout_2.addWidget(self.productname_lineEdit)
        self.creator_lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.creator_lineEdit.setObjectName("creator_lineEdit")
        self.verticalLayout_2.addWidget(self.creator_lineEdit)
        self.comments_label = QtWidgets.QLabel(Dialog)
        self.comments_label.setGeometry(QtCore.QRect(50, 270, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comments_label.setFont(font)
        self.comments_label.setObjectName("comments_label")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(50, 300, 591, 191))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.comments_textEdit = QtWidgets.QTextEdit(self.horizontalLayoutWidget)
        self.comments_textEdit.setObjectName("comments_textEdit")
        self.horizontalLayout.addWidget(self.comments_textEdit)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        # Comment Start
        self.projectname_lineEdit.textChanged.connect(self.setproject_name)
        # Comment End

    def setproject_name(self):
        self.project_name = self.projectname_lineEdit.text()

    def getproject_name(self):
        return self.project_name

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "New Project"))
        Dialog.setWindowIcon(QtGui.QIcon(r"C:\Users\rosha\PycharmProjects\FunctionPointGUIprogram\Static"
                                             r"\metrics.png"))
        self.label.setText(_translate("Dialog", "CECS 543 Metrics Suite New Project"))
        self.projectname_label.setText(_translate("Dialog", "Project Name"))
        self.productname_label.setText(_translate("Dialog", "Product Name"))
        self.creator_label.setText(_translate("Dialog", "Creator"))
        self.comments_label.setText(_translate("Dialog", "Comments:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
