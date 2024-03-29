from PyQt5 import QtCore, QtGui, QtWidgets
import SE_VAF, SE_select_language
from decimal import Decimal


class Ui_Form(object):
    counter = 0

    def __init__(self, saved_dict):
        self.displaylang_result = 0
        self.lang = "None"
        self.totalcount = 0
        self.vaf_value = 0
        self.fp = 0
        self.new_dict = saved_dict
        # print("Printing saved dict: {}".format(saved_dict))
        Ui_Form.counter += 1

    def setupUi(self, Form, fpname):
        Form.setObjectName("Form")
        Form.resize(717, 603)
        self.label_12 = QtWidgets.QLabel(Form)
        self.label_12.setGeometry(QtCore.QRect(450, 60, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.ILF_Label_2 = QtWidgets.QLabel(Form)
        self.ILF_Label_2.setGeometry(QtCore.QRect(580, 250, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ILF_Label_2.setFont(font)
        self.ILF_Label_2.setObjectName("ILF_Label_2")
        self.label_13 = QtWidgets.QLabel(Form)
        self.label_13.setGeometry(QtCore.QRect(350, 60, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.horizontalLayoutWidget_6 = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget_6.setGeometry(QtCore.QRect(10, 140, 521, 31))
        self.horizontalLayoutWidget_6.setObjectName("horizontalLayoutWidget_6")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_6)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_14 = QtWidgets.QLabel(self.horizontalLayoutWidget_6)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_6.addWidget(self.label_14)
        self.EO_lineedit_2 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_6)
        self.EO_lineedit_2.setMinimumSize(QtCore.QSize(100, 0))
        self.EO_lineedit_2.setMaximumSize(QtCore.QSize(50, 16777215))
        self.EO_lineedit_2.setObjectName("EO_lineedit_2")
        self.horizontalLayout_6.addWidget(self.EO_lineedit_2)
        self.radioButton_16 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_6)
        self.radioButton_16.setObjectName("radioButton_16")
        self.horizontalLayout_6.addWidget(self.radioButton_16)
        self.radioButton_17 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_6)
        self.radioButton_17.setObjectName("radioButton_17")
        self.horizontalLayout_6.addWidget(self.radioButton_17)
        self.radioButton_18 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_6)
        self.radioButton_18.setObjectName("radioButton_18")
        self.horizontalLayout_6.addWidget(self.radioButton_18)
        self.FP_Label_2 = QtWidgets.QLabel(Form)
        self.FP_Label_2.setGeometry(QtCore.QRect(580, 400, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.FP_Label_2.setFont(font)
        self.FP_Label_2.setObjectName("FP_Label_2")
        self.label_15 = QtWidgets.QLabel(Form)
        self.label_15.setGeometry(QtCore.QRect(300, 10, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.EO_Label_2 = QtWidgets.QLabel(Form)
        self.EO_Label_2.setGeometry(QtCore.QRect(580, 150, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.EO_Label_2.setFont(font)
        self.EO_Label_2.setObjectName("EO_Label_2")
        self.EI_Label_2 = QtWidgets.QLabel(Form)
        self.EI_Label_2.setGeometry(QtCore.QRect(580, 100, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.EI_Label_2.setFont(font)
        self.EI_Label_2.setObjectName("EI_Label_2")
        self.Error_Label = QtWidgets.QLabel(Form)
        self.Error_Label.setGeometry(QtCore.QRect(200, 340, 371, 31))
        self.Error_Label.setFont(font)
        self.Error_Label.setObjectName("Error_Label")
        self.Error_Label.setText("")
        self.horizontalLayoutWidget_7 = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget_7.setGeometry(QtCore.QRect(10, 240, 521, 31))
        self.horizontalLayoutWidget_7.setObjectName("horizontalLayoutWidget_7")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_7)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_16 = QtWidgets.QLabel(self.horizontalLayoutWidget_7)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_7.addWidget(self.label_16)
        self.ILF_lineedit_2 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_7)
        self.ILF_lineedit_2.setMinimumSize(QtCore.QSize(100, 0))
        self.ILF_lineedit_2.setMaximumSize(QtCore.QSize(50, 16777215))
        self.ILF_lineedit_2.setObjectName("ILF_lineedit_2")
        self.horizontalLayout_7.addWidget(self.ILF_lineedit_2)
        self.radioButton_19 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_7)
        self.radioButton_19.setObjectName("radioButton_19")
        self.horizontalLayout_7.addWidget(self.radioButton_19)
        self.radioButton_20 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_7)
        self.radioButton_20.setObjectName("radioButton_20")
        self.horizontalLayout_7.addWidget(self.radioButton_20)
        self.radioButton_21 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_7)
        self.radioButton_21.setObjectName("radioButton_21")
        self.horizontalLayout_7.addWidget(self.radioButton_21)
        self.TC_Label_2 = QtWidgets.QLabel(Form)
        self.TC_Label_2.setGeometry(QtCore.QRect(580, 340, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.TC_Label_2.setFont(font)
        self.TC_Label_2.setObjectName("TC_Label_2")
        self.horizontalLayoutWidget_8 = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget_8.setGeometry(QtCore.QRect(10, 190, 521, 31))
        self.horizontalLayoutWidget_8.setObjectName("horizontalLayoutWidget_8")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_8)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_17 = QtWidgets.QLabel(self.horizontalLayoutWidget_8)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_8.addWidget(self.label_17)
        self.EInq_lineedit_2 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_8)
        self.EInq_lineedit_2.setMinimumSize(QtCore.QSize(100, 0))
        self.EInq_lineedit_2.setMaximumSize(QtCore.QSize(50, 16777215))
        self.EInq_lineedit_2.setObjectName("EInq_lineedit_2")
        self.horizontalLayout_8.addWidget(self.EInq_lineedit_2)
        self.radioButton_22 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_8)
        self.radioButton_22.setObjectName("radioButton_22")
        self.horizontalLayout_8.addWidget(self.radioButton_22)
        self.radioButton_23 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_8)
        self.radioButton_23.setObjectName("radioButton_23")
        self.horizontalLayout_8.addWidget(self.radioButton_23)
        self.radioButton_24 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_8)
        self.radioButton_24.setObjectName("radioButton_24")
        self.horizontalLayout_8.addWidget(self.radioButton_24)
        self.Language_Label_2 = QtWidgets.QLabel(Form)
        self.Language_Label_2.setGeometry(QtCore.QRect(440, 500, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Language_Label_2.setFont(font)
        self.Language_Label_2.setObjectName("Language_Label_2")
        self.horizontalLayoutWidget_9 = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget_9.setGeometry(QtCore.QRect(10, 290, 521, 31))
        self.horizontalLayoutWidget_9.setObjectName("horizontalLayoutWidget_9")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_9)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_18 = QtWidgets.QLabel(self.horizontalLayoutWidget_9)
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_9.addWidget(self.label_18)
        self.EIF_lineedit_2 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_9)
        self.EIF_lineedit_2.setMinimumSize(QtCore.QSize(100, 0))
        self.EIF_lineedit_2.setMaximumSize(QtCore.QSize(50, 16777215))
        self.EIF_lineedit_2.setObjectName("EIF_lineedit_2")
        self.horizontalLayout_9.addWidget(self.EIF_lineedit_2)
        self.radioButton_25 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_9)
        self.radioButton_25.setObjectName("radioButton_25")
        self.horizontalLayout_9.addWidget(self.radioButton_25)
        self.radioButton_26 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_9)
        self.radioButton_26.setObjectName("radioButton_26")
        self.horizontalLayout_9.addWidget(self.radioButton_26)
        self.radioButton_27 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_9)
        self.radioButton_27.setObjectName("radioButton_27")
        self.horizontalLayout_9.addWidget(self.radioButton_27)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 380, 201, 201))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.computefp_btn_2 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.computefp_btn_2.setObjectName("computefp_btn_2")
        self.verticalLayout_2.addWidget(self.computefp_btn_2)
        self.vaf_btn_2 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.vaf_btn_2.setObjectName("vaf_btn_2")
        self.verticalLayout_2.addWidget(self.vaf_btn_2)
        self.codesize_btn_2 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.codesize_btn_2.setObjectName("codesize_btn_2")
        self.verticalLayout_2.addWidget(self.codesize_btn_2)
        self.chooselang_btn_2 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.chooselang_btn_2.setObjectName("chooselang_btn_2")
        self.verticalLayout_2.addWidget(self.chooselang_btn_2)
        self.CodeSize_Label_2 = QtWidgets.QLabel(Form)
        self.CodeSize_Label_2.setGeometry(QtCore.QRect(580, 490, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.CodeSize_Label_2.setFont(font)
        self.CodeSize_Label_2.setObjectName("CodeSize_Label_2")
        self.label_19 = QtWidgets.QLabel(Form)
        self.label_19.setGeometry(QtCore.QRect(310, 490, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(Form)
        self.label_20.setGeometry(QtCore.QRect(20, 340, 81, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.VAF_Label_2 = QtWidgets.QLabel(Form)
        self.VAF_Label_2.setGeometry(QtCore.QRect(580, 440, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.VAF_Label_2.setFont(font)
        self.VAF_Label_2.setObjectName("VAF_Label_2")
        self.horizontalLayoutWidget_10 = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget_10.setGeometry(QtCore.QRect(10, 90, 521, 31))
        self.horizontalLayoutWidget_10.setObjectName("horizontalLayoutWidget_10")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_10)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_21 = QtWidgets.QLabel(self.horizontalLayoutWidget_10)
        self.label_21.setObjectName("label_21")
        self.horizontalLayout_10.addWidget(self.label_21)
        self.EI_lineedit_2 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_10)
        self.EI_lineedit_2.setMinimumSize(QtCore.QSize(100, 0))
        self.EI_lineedit_2.setMaximumSize(QtCore.QSize(50, 16777215))
        self.EI_lineedit_2.setObjectName("EI_lineedit_2")
        self.horizontalLayout_10.addWidget(self.EI_lineedit_2)
        self.radioButton_28 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_10)
        self.radioButton_28.setObjectName("radioButton_28")
        self.horizontalLayout_10.addWidget(self.radioButton_28)
        self.radioButton_29 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_10)
        self.radioButton_29.setObjectName("radioButton_29")
        self.horizontalLayout_10.addWidget(self.radioButton_29)
        self.radioButton_30 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_10)
        self.radioButton_30.setObjectName("radioButton_30")
        self.horizontalLayout_10.addWidget(self.radioButton_30)
        self.EInq_Label_2 = QtWidgets.QLabel(Form)
        self.EInq_Label_2.setGeometry(QtCore.QRect(580, 200, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.EInq_Label_2.setFont(font)
        self.EInq_Label_2.setObjectName("EInq_Label_2")
        self.label_22 = QtWidgets.QLabel(Form)
        self.label_22.setGeometry(QtCore.QRect(240, 60, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.EIF_Label_2 = QtWidgets.QLabel(Form)
        self.EIF_Label_2.setGeometry(QtCore.QRect(580, 300, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.EIF_Label_2.setFont(font)
        self.EIF_Label_2.setObjectName("EIF_Label_2")

        # comment start
        self.chooselang_btn_2.clicked.connect(self.displaylang)
        self.vaf_btn_2.clicked.connect(self.vafdialog)
        self.computefp_btn_2.clicked.connect(self.calculatefp)
        self.EI_lineedit_2.setText("0")
        self.EO_lineedit_2.setText("0")
        self.EInq_lineedit_2.setText("0")
        self.ILF_lineedit_2.setText("0")
        self.EIF_lineedit_2.setText("0")
        self.codesize_btn_2.clicked.connect(self.codesize)
        # comment end

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def calculatefp(self):
        self.choice = 0
        try:
            if int(self.EI_lineedit_2.text()) < 0 or int(self.EO_lineedit_2.text()) < 0 or int(
                    self.EInq_lineedit_2.text()) < 0 or int(self.ILF_lineedit_2.text()) < 0 or int(
                self.EIF_lineedit_2.text()) < 0:
                self.Error_Label.setText("Enter positive numbers only!")
                self.Error_Label.setStyleSheet("color: red")
                return
        except:
            self.Error_Label.setText("Enter numbers only!")
            self.Error_Label.setStyleSheet("color: red")
            return

        self.Error_Label.setText("")
        self.ei = int(self.EI_lineedit_2.text())
        if self.radioButton_28.isChecked():
            self.choice = 3
        elif self.radioButton_29.isChecked():
            self.choice = 4
        elif self.radioButton_30.isChecked():
            self.choice = 6
        self.result = self.ei * self.choice
        self.EI_Label_2.setText(str(self.result))

        self.eo = int(self.EO_lineedit_2.text())
        if self.radioButton_16.isChecked():
            self.choice = 4
        elif self.radioButton_17.isChecked():
            self.choice = 5
        elif self.radioButton_18.isChecked():
            self.choice = 7
        self.result = self.eo * self.choice
        self.EO_Label_2.setText(str(self.result))

        self.einq = int(self.EInq_lineedit_2.text())
        if self.radioButton_22.isChecked():
            self.choice = 3
        elif self.radioButton_23.isChecked():
            self.choice = 4
        elif self.radioButton_24.isChecked():
            self.choice = 6
        self.result = self.einq * self.choice
        self.EInq_Label_2.setText(str(self.result))

        self.ilf = int(self.ILF_lineedit_2.text())
        if self.radioButton_19.isChecked():
            self.choice = 7
        elif self.radioButton_20.isChecked():
            self.choice = 10
        elif self.radioButton_21.isChecked():
            self.choice = 15
        self.result = self.ilf * self.choice
        self.ILF_Label_2.setText(str(self.result))

        self.eif = int(self.EIF_lineedit_2.text())
        if self.radioButton_25.isChecked():
            self.choice = 5
        elif self.radioButton_26.isChecked():
            self.choice = 7
        elif self.radioButton_27.isChecked():
            self.choice = 10
        self.result = self.eif * self.choice
        self.EIF_Label_2.setText(str(self.result))

        # ********************
        self.totalcount = int(self.EI_Label_2.text()) + int(self.EO_Label_2.text()) + int(
            self.EInq_Label_2.text()) + int(self.ILF_Label_2.text()) + int(self.EIF_Label_2.text())
        self.TC_Label_2.setText(str(self.totalcount))
        self.vaf_value = int(self.VAF_Label_2.text())
        self.fp = self.totalcount * (Decimal('0.65') + (Decimal('0.01') * Decimal(self.vaf_value)))
        self.FP_Label_2.setText(str(int(self.fp)))
        # *********************

    def displaylang(self):
        self.Dialog_3 = QtWidgets.QDialog()
        self.codesizeobj = SE_select_language.Ui_Dialog()
        self.codesizeobj.setupUi(self.Dialog_3)
        self.Dialog_3.show()
        self.response = self.Dialog_3.exec_()

        if self.response == QtWidgets.QDialog.Accepted:
            self.displaylang_result, self.lang = self.codesizeobj.getvalue()

    def vafdialog(self):
        self.Dialog = QtWidgets.QDialog()
        self.vaf_obj = SE_VAF.Ui_Dialog()
        self.vaf_obj.setupUi(self.Dialog)
        self.Dialog.show()
        self.response = self.Dialog.exec_()

        if self.response == QtWidgets.QDialog.Accepted:
            self.VAF_Label_2.setText(str(self.vaf_obj.get_vaf_value()))

    def codesize(self):
        self.CodeSize_Label_2.setText(str(self.displaylang_result * int(self.fp)))
        self.Language_Label_2.setText(self.lang)

    def save(self):
        # self.new_dict[]
        # print("FP new dict contains {}".format(self.new_dict))
        self.new_dict = {}
        self.new_dict["EI_lineedit"] = self.EI_lineedit_2.text()
        self.new_dict["EO_lineedit"] = self.EO_lineedit_2.text()
        self.new_dict["EInq_lineedit"] = self.EInq_lineedit_2.text()
        self.new_dict["ILF_lineedit"] = self.ILF_lineedit_2.text()
        self.new_dict["EIF_lineedit"] = self.EIF_lineedit_2.text()
        ##
        self.new_dict["EI_Label"] = self.EI_Label_2.text()
        self.new_dict["EO_Label"] = self.EO_Label_2.text()
        self.new_dict["EInq_Label"] = self.EInq_Label_2.text()
        self.new_dict["ILF_Label"] = self.ILF_Label_2.text()
        self.new_dict["EIF_Label"] = self.EIF_Label_2.text()
        self.new_dict["TC_Label"] = self.TC_Label_2.text()
        self.new_dict["FP_Label"] = self.FP_Label_2.text()
        self.new_dict["VAF_Label"] = self.VAF_Label_2.text()
        self.new_dict["CodeSize_Label"] = self.CodeSize_Label_2.text()
        ##
        if self.radioButton_28.isChecked():
            self.new_dict["radioButton_28"] = True
        if self.radioButton_29.isChecked():
            self.new_dict["radioButton_29"] = True
        if self.radioButton_30.isChecked():
            self.new_dict["radioButton_30"] = True
        if self.radioButton_16.isChecked():
            self.new_dict["radioButton_16"] = True
        if self.radioButton_17.isChecked():
            self.new_dict["radioButton_17"] = True
        if self.radioButton_18.isChecked():
            self.new_dict["radioButton_18"] = True
        if self.radioButton_22.isChecked():
            self.new_dict["radioButton_22"] = True
        if self.radioButton_23.isChecked():
            self.new_dict["radioButton_23"] = True
        if self.radioButton_24.isChecked():
            self.new_dict["radioButton_24"] = True
        if self.radioButton_19.isChecked():
            self.new_dict["radioButton_19"] = True
        if self.radioButton_20.isChecked():
            self.new_dict["radioButton_20"] = True
        if self.radioButton_21.isChecked():
            self.new_dict["radioButton_21"] = True
        if self.radioButton_25.isChecked():
            self.new_dict["radioButton_25"] = True
        if self.radioButton_26.isChecked():
            self.new_dict["radioButton_26"] = True
        if self.radioButton_27.isChecked():
            self.new_dict["radioButton_27"] = True
        ##
        self.new_dict["language"] = self.Language_Label_2.text()
        ##
        # print("FP is returning: {}".format(self.new_dict))
        return self.new_dict

    def restore_data(self):
        self.EI_lineedit_2.setText(self.new_dict["EI_lineedit"])
        self.EO_lineedit_2.setText(self.new_dict["EO_lineedit"])
        self.EInq_lineedit_2.setText(self.new_dict["EInq_lineedit"])
        self.ILF_lineedit_2.setText(self.new_dict["ILF_lineedit"])
        self.EIF_lineedit_2.setText(self.new_dict["EIF_lineedit"])
        self.EI_Label_2.setText(str(self.new_dict["EI_Label"]))
        self.EO_Label_2.setText(self.new_dict["EO_Label"])
        self.EInq_Label_2.setText(self.new_dict["EInq_Label"])
        self.ILF_Label_2.setText(self.new_dict["ILF_Label"])
        self.EIF_Label_2.setText(self.new_dict["EIF_Label"])
        self.TC_Label_2.setText(self.new_dict["TC_Label"])
        self.FP_Label_2.setText(self.new_dict["FP_Label"])
        self.VAF_Label_2.setText(self.new_dict["VAF_Label"])
        self.CodeSize_Label_2.setText(self.new_dict["CodeSize_Label"])
        ##
        if "radioButton_28" in self.new_dict:
            self.radioButton_28.setChecked(True)
        if "radioButton_29" in self.new_dict:
            self.radioButton_29.setChecked(True)
        if "radioButton_30" in self.new_dict:
            self.radioButton_30.setChecked(True)
        if "radioButton_16" in self.new_dict:
            self.radioButton_16.setChecked(True)
        if "radioButton_17" in self.new_dict:
            self.radioButton_17.setChecked(True)
        if "radioButton_18" in self.new_dict:
            self.radioButton_18.setChecked(True)
        if "radioButton_22" in self.new_dict:
            self.radioButton_22.setChecked(True)
        if "radioButton_23" in self.new_dict:
            self.radioButton_23.setChecked(True)
        if "radioButton_24" in self.new_dict:
            self.radioButton_24.setChecked(True)
        if "radioButton_19" in self.new_dict:
            self.radioButton_19.setChecked(True)
        if "radioButton_20" in self.new_dict:
            self.radioButton_20.setChecked(True)
        if "radioButton_21" in self.new_dict:
            self.radioButton_21.setChecked(True)
        if "radioButton_25" in self.new_dict:
            self.radioButton_25.setChecked(True)
        if "radioButton_26" in self.new_dict:
            self.radioButton_26.setChecked(True)
        if "radioButton_27" in self.new_dict:
            self.radioButton_27.setChecked(True)
        #
        if self.new_dict["language"] == "Assembler":
            self.displaylang_result, self.lang = (337, "Assembler")
            self.Language_Label_2.setText("Assembler")
        elif self.new_dict["language"] == "ADA":
            self.displaylang_result, self.lang = (154, "ADA")
            self.Language_Label_2.setText("ADA")
        elif self.new_dict["language"] == "C":
            self.displaylang_result, self.lang = (148,"C")
            self.Language_Label_2.setText("C")
        elif self.new_dict["language"] == "C++":
            self.displaylang_result, self.lang = (59, "C++")
            self.Language_Label_2.setText("C++")
        elif self.new_dict["language"] == "C#":
            self.displaylang_result, self.lang = (58, "C#")
            self.Language_Label_2.setText("C#")
        elif self.new_dict["language"] == "COBOL":
            self.displaylang_result, self.lang = (80, "COBOL")
            self.Language_Label_2.setText("COBOL")
        if self.new_dict["language"] == "FORTRAN":
            self.displaylang_result, self.lang = (90, "FORTRAN")
            self.Language_Label_2.setText("FORTRAN")
        elif self.new_dict["language"] == "HTML":
            self.displaylang_result, self.lang = (43, "HTML")
            self.Language_Label_2.setText("HTML")
        elif self.new_dict["language"] == "Java":
            self.displaylang_result, self.lang = (55, "Java")
            self.Language_Label_2.setText("Java")
        elif self.new_dict["language"] == "JavaScript":
            self.displaylang_result, self.lang = (54, "JavaScript")
            self.Language_Label_2.setText("JavaScript")
        elif self.new_dict["language"] == "VB Script":
            self.displaylang_result, self.lang = (38, "VB Script")
            self.Language_Label_2.setText("VB Script")
        elif self.new_dict["language"] == "Visual Basic":
            self.displaylang_result, self.lang = (50, "Visual Basic")
            self.Language_Label_2.setText("Visual Basic")

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_12.setText(_translate("Form", "Complex"))
        self.ILF_Label_2.setText(_translate("Form", "0"))
        self.label_13.setText(_translate("Form", "Average"))
        self.label_14.setText(_translate("Form", "External Outputs"))
        self.radioButton_16.setText(_translate("Form", "4"))
        self.radioButton_17.setText(_translate("Form", "5"))
        self.radioButton_18.setText(_translate("Form", "7"))
        self.FP_Label_2.setText(_translate("Form", "0"))
        self.label_15.setText(_translate("Form", "Weighting Factors"))
        self.EO_Label_2.setText(_translate("Form", "0"))
        self.EI_Label_2.setText(_translate("Form", "0"))
        self.label_16.setText(_translate("Form", "Internal Logic Files"))
        self.radioButton_19.setText(_translate("Form", "7"))
        self.radioButton_20.setText(_translate("Form", "10"))
        self.radioButton_21.setText(_translate("Form", "15"))
        self.TC_Label_2.setText(_translate("Form", "0"))
        self.label_17.setText(_translate("Form", "External Inquiries"))
        self.radioButton_22.setText(_translate("Form", "3"))
        self.radioButton_23.setText(_translate("Form", "4"))
        self.radioButton_24.setText(_translate("Form", "6"))
        self.Language_Label_2.setText(_translate("Form", "None"))
        self.label_18.setText(_translate("Form", "Ext Interface Files"))
        self.radioButton_25.setText(_translate("Form", "5"))
        self.radioButton_26.setText(_translate("Form", "7"))
        self.radioButton_27.setText(_translate("Form", "10"))
        self.computefp_btn_2.setText(_translate("Form", "Compute FP"))
        self.vaf_btn_2.setText(_translate("Form", "Value Adjustments"))
        self.codesize_btn_2.setText(_translate("Form", "Compute Code Size"))
        self.chooselang_btn_2.setText(_translate("Form", "Change Language"))
        self.CodeSize_Label_2.setText(_translate("Form", "0"))
        self.label_19.setText(_translate("Form", "Current Language"))
        self.label_20.setText(_translate("Form", "Total Count"))
        self.VAF_Label_2.setText(_translate("Form", "0"))
        self.label_21.setText(_translate("Form", "External Inputs"))
        self.radioButton_28.setText(_translate("Form", "3"))
        self.radioButton_29.setText(_translate("Form", "4"))
        self.radioButton_30.setText(_translate("Form", "6"))
        self.EInq_Label_2.setText(_translate("Form", "0"))
        self.label_22.setText(_translate("Form", "Simple"))
        self.EIF_Label_2.setText(_translate("Form", "0"))
        self.radioButton_29.setChecked(True)
        self.radioButton_17.setChecked(True)
        self.radioButton_23.setChecked(True)
        self.radioButton_20.setChecked(True)
        self.radioButton_26.setChecked(True)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form, "First")
    Form.show()
    sys.exit(app.exec_())
