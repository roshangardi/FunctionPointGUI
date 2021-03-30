from PyQt5 import QtCore, QtGui, QtWidgets
import SE_TCF_Dialog, SE_ECF_Dialog, SE_UUCP


class Ui_Form(object):
    def setupUi(self, Form, ucpname):
        Form.setObjectName("Form")
        Form.resize(767, 607)
        self.horizontalLayoutWidget_6 = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget_6.setGeometry(QtCore.QRect(20, 380, 521, 31))
        self.horizontalLayoutWidget_6.setObjectName("horizontalLayoutWidget_6")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_6)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_14 = QtWidgets.QLabel(self.horizontalLayoutWidget_6)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_6.addWidget(self.label_14)
        self.EO_lineedit_2 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_6)
        self.EO_lineedit_2.setMinimumSize(QtCore.QSize(100, 0))
        self.EO_lineedit_2.setMaximumSize(QtCore.QSize(50, 16777215))
        self.EO_lineedit_2.setObjectName("EO_lineedit_2")
        self.horizontalLayout_6.addWidget(self.EO_lineedit_2)
        self.label_15 = QtWidgets.QLabel(Form)
        self.label_15.setGeometry(QtCore.QRect(320, 10, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.horizontalLayoutWidget_8 = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget_8.setGeometry(QtCore.QRect(20, 430, 521, 31))
        self.horizontalLayoutWidget_8.setObjectName("horizontalLayoutWidget_8")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_8)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_17 = QtWidgets.QLabel(self.horizontalLayoutWidget_8)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_8.addWidget(self.label_17)
        self.EInq_lineedit_2 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_8)
        self.EInq_lineedit_2.setMinimumSize(QtCore.QSize(100, 0))
        self.EInq_lineedit_2.setMaximumSize(QtCore.QSize(50, 16777215))
        self.EInq_lineedit_2.setObjectName("EInq_lineedit_2")
        self.horizontalLayout_8.addWidget(self.EInq_lineedit_2)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(20, 70, 521, 211))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.computefp_btn_2 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.computefp_btn_2.setFont(font)
        self.computefp_btn_2.setObjectName("computefp_btn_2")
        self.horizontalLayout.addWidget(self.computefp_btn_2)
        self.CodeSize_Label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.CodeSize_Label_2.setFont(font)
        self.CodeSize_Label_2.setObjectName("CodeSize_Label_2")
        self.horizontalLayout.addWidget(self.CodeSize_Label_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.vaf_btn_2 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.vaf_btn_2.setFont(font)
        self.vaf_btn_2.setObjectName("vaf_btn_2")
        self.horizontalLayout_2.addWidget(self.vaf_btn_2)
        self.CodeSize_Label_3 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.CodeSize_Label_3.setFont(font)
        self.CodeSize_Label_3.setObjectName("CodeSize_Label_3")
        self.horizontalLayout_2.addWidget(self.CodeSize_Label_3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.codesize_btn_2 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.codesize_btn_2.setFont(font)
        self.codesize_btn_2.setObjectName("codesize_btn_2")
        self.horizontalLayout_3.addWidget(self.codesize_btn_2)
        self.CodeSize_Label_4 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.CodeSize_Label_4.setFont(font)
        self.CodeSize_Label_4.setObjectName("CodeSize_Label_4")
        self.horizontalLayout_3.addWidget(self.CodeSize_Label_4)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.chooselang_btn_2 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.chooselang_btn_2.setFont(font)
        self.chooselang_btn_2.setObjectName("chooselang_btn_2")
        self.horizontalLayout_4.addWidget(self.chooselang_btn_2)
        self.CodeSize_Label_5 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.CodeSize_Label_5.setFont(font)
        self.CodeSize_Label_5.setObjectName("CodeSize_Label_5")
        self.horizontalLayout_4.addWidget(self.CodeSize_Label_5)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayoutWidget_10 = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget_10.setGeometry(QtCore.QRect(20, 330, 521, 31))
        self.horizontalLayoutWidget_10.setObjectName("horizontalLayoutWidget_10")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_10)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_21 = QtWidgets.QLabel(self.horizontalLayoutWidget_10)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.horizontalLayout_10.addWidget(self.label_21)
        self.EI_lineedit_2 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_10)
        self.EI_lineedit_2.setMinimumSize(QtCore.QSize(100, 0))
        self.EI_lineedit_2.setMaximumSize(QtCore.QSize(50, 16777215))
        self.EI_lineedit_2.setObjectName("EI_lineedit_2")
        self.horizontalLayout_10.addWidget(self.EI_lineedit_2)
        self.horizontalLayoutWidget_7 = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget_7.setGeometry(QtCore.QRect(10, 530, 753, 31))
        self.horizontalLayoutWidget_7.setObjectName("horizontalLayoutWidget_7")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_7)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_16 = QtWidgets.QLabel(self.horizontalLayoutWidget_7)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_7.addWidget(self.label_16)
        self.ILF_lineedit_2 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_7)
        self.ILF_lineedit_2.setMinimumSize(QtCore.QSize(100, 0))
        self.ILF_lineedit_2.setMaximumSize(QtCore.QSize(50, 16777215))
        self.ILF_lineedit_2.setObjectName("ILF_lineedit_2")
        self.horizontalLayout_7.addWidget(self.ILF_lineedit_2)
        self.label_18 = QtWidgets.QLabel(self.horizontalLayoutWidget_7)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_7.addWidget(self.label_18)
        self.ILF_lineedit_3 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_7)
        self.ILF_lineedit_3.setMinimumSize(QtCore.QSize(100, 0))
        self.ILF_lineedit_3.setMaximumSize(QtCore.QSize(50, 16777215))
        self.ILF_lineedit_3.setObjectName("ILF_lineedit_3")
        self.horizontalLayout_7.addWidget(self.ILF_lineedit_3)
        self.label_19 = QtWidgets.QLabel(self.horizontalLayoutWidget_7)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.horizontalLayout_7.addWidget(self.label_19)
        self.ILF_lineedit_4 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_7)
        self.ILF_lineedit_4.setMinimumSize(QtCore.QSize(100, 0))
        self.ILF_lineedit_4.setMaximumSize(QtCore.QSize(50, 16777215))
        self.ILF_lineedit_4.setObjectName("ILF_lineedit_4")
        self.horizontalLayout_7.addWidget(self.ILF_lineedit_4)
        self.label_20 = QtWidgets.QLabel(self.horizontalLayoutWidget_7)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.horizontalLayout_7.addWidget(self.label_20)
        self.ILF_lineedit_5 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_7)
        self.ILF_lineedit_5.setMinimumSize(QtCore.QSize(100, 0))
        self.ILF_lineedit_5.setMaximumSize(QtCore.QSize(50, 16777215))
        self.ILF_lineedit_5.setObjectName("ILF_lineedit_5")
        self.horizontalLayout_7.addWidget(self.ILF_lineedit_5)

        ##
        self.computefp_btn_2.clicked.connect(self.tcfdialog)
        self.vaf_btn_2.clicked.connect(self.ecfdialog)
        self.codesize_btn_2.clicked.connect(self.uucp)
        ##

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def tcfdialog(self):
        self.tcf_Dialog = QtWidgets.QDialog()
        self.tcf_obj = SE_TCF_Dialog.Ui_Dialog()
        self.tcf_obj.setupUi(self.tcf_Dialog)
        self.tcf_Dialog.show()
        self.response = self.tcf_Dialog.exec_()

        if self.response == QtWidgets.QDialog.Accepted:
            self.CodeSize_Label_2.setText(str(self.tcf_obj.get_tcf_value()))

    def ecfdialog(self):
        self.ecf_Dialog = QtWidgets.QDialog()
        self.ecf_obj = SE_ECF_Dialog.Ui_Dialog()
        self.ecf_obj.setupUi(self.ecf_Dialog)
        self.ecf_Dialog.show()
        self.response = self.ecf_Dialog.exec_()

        if self.response == QtWidgets.QDialog.Accepted:
            self.CodeSize_Label_3.setText(str(self.ecf_obj.get_ecf_value()))

    def uucp(self):
        self.uucp_Dialog = QtWidgets.QDialog()
        self.uucp_obj = SE_UUCP.Ui_Dialog()
        self.uucp_obj.setupUi(self.uucp_Dialog)
        self.uucp_Dialog.show()
        self.response = self.uucp_Dialog.exec_()

        if self.response == QtWidgets.QDialog.Accepted:
            self.CodeSize_Label_4.setText(str(self.uucp_obj.get_uucp_value()))

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_14.setText(_translate("Form", "LOC per month"))
        self.EO_lineedit_2.setText(_translate("Form", "700"))
        self.label_15.setText(_translate("Form", " Use Case Points "))
        self.label_17.setText(_translate("Form", "LOC per UCP"))
        self.EInq_lineedit_2.setText(_translate("Form", "100"))
        self.computefp_btn_2.setText(_translate("Form", "TCF Calculation"))
        self.CodeSize_Label_2.setText(_translate("Form", "0"))
        self.vaf_btn_2.setText(_translate("Form", "ECF Calculation"))
        self.CodeSize_Label_3.setText(_translate("Form", "0"))
        self.codesize_btn_2.setText(_translate("Form", "UUCP Calculation"))
        self.CodeSize_Label_4.setText(_translate("Form", "0"))
        self.chooselang_btn_2.setText(_translate("Form", "UCP Calculation"))
        self.CodeSize_Label_5.setText(_translate("Form", "0"))
        self.label_21.setText(_translate("Form", "Productivity Factor"))
        self.EI_lineedit_2.setText(_translate("Form", "20"))
        self.label_16.setText(_translate("Form", "Total UCP"))
        self.label_18.setText(_translate("Form", "Estimated Hours"))
        self.label_19.setText(_translate("Form", "Estimated LOC"))
        self.label_20.setText(_translate("Form", "Estimated PM"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
