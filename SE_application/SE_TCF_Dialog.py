from PyQt5 import QtCore, QtGui, QtWidgets
import decimal


class Ui_Dialog(object):
    def __init__(self):
        self.result = 5.3

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(769, 523)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(270, 420, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayoutWidget = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 20, 741, 368))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.gridLayoutWidget.setFont(font)
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_21 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.label_21.setFont(font)
        self.label_21.setAlignment(QtCore.Qt.AlignCenter)
        self.label_21.setObjectName("label_21")
        self.gridLayout.addWidget(self.label_21, 4, 0, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.label_22.setFont(font)
        self.label_22.setAlignment(QtCore.Qt.AlignCenter)
        self.label_22.setObjectName("label_22")
        self.gridLayout.addWidget(self.label_22, 5, 0, 1, 1)
        self.label_46 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.label_46.setFont(font)
        self.label_46.setAlignment(QtCore.Qt.AlignCenter)
        self.label_46.setObjectName("label_46")
        self.gridLayout.addWidget(self.label_46, 8, 1, 1, 1)
        self.label_47 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.label_47.setFont(font)
        self.label_47.setAlignment(QtCore.Qt.AlignCenter)
        self.label_47.setObjectName("label_47")
        self.gridLayout.addWidget(self.label_47, 9, 1, 1, 1)
        self.label_24 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.label_24.setFont(font)
        self.label_24.setAlignment(QtCore.Qt.AlignCenter)
        self.label_24.setObjectName("label_24")
        self.gridLayout.addWidget(self.label_24, 7, 0, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.label_20.setFont(font)
        self.label_20.setAlignment(QtCore.Qt.AlignCenter)
        self.label_20.setObjectName("label_20")
        self.gridLayout.addWidget(self.label_20, 3, 0, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.label_23.setFont(font)
        self.label_23.setAlignment(QtCore.Qt.AlignCenter)
        self.label_23.setObjectName("label_23")
        self.gridLayout.addWidget(self.label_23, 6, 0, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.label_19.setFont(font)
        self.label_19.setAlignment(QtCore.Qt.AlignCenter)
        self.label_19.setObjectName("label_19")
        self.gridLayout.addWidget(self.label_19, 2, 0, 1, 1)
        self.label_41 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.label_41.setFont(font)
        self.label_41.setAlignment(QtCore.Qt.AlignCenter)
        self.label_41.setObjectName("label_41")
        self.gridLayout.addWidget(self.label_41, 10, 0, 1, 1)
        self.label_43 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.label_43.setFont(font)
        self.label_43.setAlignment(QtCore.Qt.AlignCenter)
        self.label_43.setObjectName("label_43")
        self.gridLayout.addWidget(self.label_43, 9, 0, 1, 1)
        self.label_45 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.label_45.setFont(font)
        self.label_45.setAlignment(QtCore.Qt.AlignCenter)
        self.label_45.setObjectName("label_45")
        self.gridLayout.addWidget(self.label_45, 12, 0, 1, 1)
        self.label_44 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.label_44.setFont(font)
        self.label_44.setAlignment(QtCore.Qt.AlignCenter)
        self.label_44.setObjectName("label_44")
        self.gridLayout.addWidget(self.label_44, 11, 0, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.label_18.setFont(font)
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName("label_18")
        self.gridLayout.addWidget(self.label_18, 7, 1, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.label_14.setFont(font)
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 3, 1, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.label_17.setFont(font)
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.gridLayout.addWidget(self.label_17, 6, 1, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.label_16.setFont(font)
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.gridLayout.addWidget(self.label_16, 4, 1, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.label_15.setFont(font)
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.gridLayout.addWidget(self.label_15, 5, 1, 1, 1)
        self.label_50 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.label_50.setFont(font)
        self.label_50.setAlignment(QtCore.Qt.AlignCenter)
        self.label_50.setObjectName("label_50")
        self.gridLayout.addWidget(self.label_50, 12, 1, 1, 1)
        self.label_49 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.label_49.setFont(font)
        self.label_49.setAlignment(QtCore.Qt.AlignCenter)
        self.label_49.setObjectName("label_49")
        self.gridLayout.addWidget(self.label_49, 11, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_42 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.label_42.setFont(font)
        self.label_42.setAlignment(QtCore.Qt.AlignCenter)
        self.label_42.setObjectName("label_42")
        self.gridLayout.addWidget(self.label_42, 8, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 0, 2, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 0, 4, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 0, 3, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 2, 1, 1, 1)
        self.label_48 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.label_48.setFont(font)
        self.label_48.setAlignment(QtCore.Qt.AlignCenter)
        self.label_48.setObjectName("label_48")
        self.gridLayout.addWidget(self.label_48, 10, 1, 1, 1)
        self.label_66 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.label_66.setFont(font)
        self.label_66.setAlignment(QtCore.Qt.AlignCenter)
        self.label_66.setObjectName("label_66")
        self.gridLayout.addWidget(self.label_66, 13, 1, 1, 1)
        self.label_67 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.label_67.setFont(font)
        self.label_67.setAlignment(QtCore.Qt.AlignCenter)
        self.label_67.setObjectName("label_67")
        self.gridLayout.addWidget(self.label_67, 13, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_2.setMaximumSize(QtCore.QSize(100, 16777215))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 1, 2, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_3.setMaximumSize(QtCore.QSize(100, 16777215))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 1, 3, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_4.setMaximumSize(QtCore.QSize(100, 16777215))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout.addWidget(self.lineEdit_4, 1, 4, 1, 1)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_5.setMaximumSize(QtCore.QSize(100, 16777215))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout.addWidget(self.lineEdit_5, 2, 2, 1, 1)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_6.setMaximumSize(QtCore.QSize(100, 16777215))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.gridLayout.addWidget(self.lineEdit_6, 2, 3, 1, 1)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_7.setMaximumSize(QtCore.QSize(100, 16777215))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.gridLayout.addWidget(self.lineEdit_7, 2, 4, 1, 1)
        self.lineEdit_10 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_10.setMaximumSize(QtCore.QSize(100, 16777215))
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.gridLayout.addWidget(self.lineEdit_10, 3, 2, 1, 1)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_8.setMaximumSize(QtCore.QSize(100, 16777215))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.gridLayout.addWidget(self.lineEdit_8, 3, 3, 1, 1)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_9.setMaximumSize(QtCore.QSize(100, 16777215))
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.gridLayout.addWidget(self.lineEdit_9, 3, 4, 1, 1)
        self.lineEdit_13 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_13.setMaximumSize(QtCore.QSize(100, 16777215))
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.gridLayout.addWidget(self.lineEdit_13, 4, 2, 1, 1)
        self.lineEdit_11 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_11.setMaximumSize(QtCore.QSize(100, 16777215))
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.gridLayout.addWidget(self.lineEdit_11, 4, 3, 1, 1)
        self.lineEdit_12 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_12.setMaximumSize(QtCore.QSize(100, 16777215))
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.gridLayout.addWidget(self.lineEdit_12, 4, 4, 1, 1)
        self.lineEdit_16 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_16.setMaximumSize(QtCore.QSize(100, 16777215))
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.gridLayout.addWidget(self.lineEdit_16, 5, 2, 1, 1)
        self.lineEdit_15 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_15.setMaximumSize(QtCore.QSize(100, 16777215))
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.gridLayout.addWidget(self.lineEdit_15, 5, 3, 1, 1)
        self.lineEdit_14 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_14.setMaximumSize(QtCore.QSize(100, 16777215))
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.gridLayout.addWidget(self.lineEdit_14, 5, 4, 1, 1)
        self.lineEdit_19 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_19.setMaximumSize(QtCore.QSize(100, 16777215))
        self.lineEdit_19.setObjectName("lineEdit_19")
        self.gridLayout.addWidget(self.lineEdit_19, 6, 2, 1, 1)
        self.lineEdit_18 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_18.setMaximumSize(QtCore.QSize(100, 16777215))
        self.lineEdit_18.setObjectName("lineEdit_18")
        self.gridLayout.addWidget(self.lineEdit_18, 6, 3, 1, 1)
        self.lineEdit_17 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_17.setMaximumSize(QtCore.QSize(100, 16777215))
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.gridLayout.addWidget(self.lineEdit_17, 6, 4, 1, 1)
        self.lineEdit_22 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_22.setMaximumSize(QtCore.QSize(100, 16777215))
        self.lineEdit_22.setObjectName("lineEdit_22")
        self.gridLayout.addWidget(self.lineEdit_22, 7, 2, 1, 1)
        self.lineEdit_21 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_21.setMaximumSize(QtCore.QSize(100, 16777215))
        self.lineEdit_21.setObjectName("lineEdit_21")
        self.gridLayout.addWidget(self.lineEdit_21, 7, 3, 1, 1)
        self.lineEdit_20 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_20.setMaximumSize(QtCore.QSize(100, 16777215))
        self.lineEdit_20.setObjectName("lineEdit_20")
        self.gridLayout.addWidget(self.lineEdit_20, 7, 4, 1, 1)
        self.lineEdit_25 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_25.setMaximumSize(QtCore.QSize(100, 16777215))
        self.lineEdit_25.setObjectName("lineEdit_25")
        self.gridLayout.addWidget(self.lineEdit_25, 8, 2, 1, 1)
        self.lineEdit_24 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_24.setMaximumSize(QtCore.QSize(100, 16777215))
        self.lineEdit_24.setObjectName("lineEdit_24")
        self.gridLayout.addWidget(self.lineEdit_24, 8, 3, 1, 1)
        self.lineEdit_23 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_23.setMaximumSize(QtCore.QSize(100, 16777215))
        self.lineEdit_23.setObjectName("lineEdit_23")
        self.gridLayout.addWidget(self.lineEdit_23, 8, 4, 1, 1)
        self.lineEdit_28 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_28.setMaximumSize(QtCore.QSize(100, 16777215))
        self.lineEdit_28.setObjectName("lineEdit_28")
        self.gridLayout.addWidget(self.lineEdit_28, 9, 2, 1, 1)
        self.lineEdit_26 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_26.setMaximumSize(QtCore.QSize(100, 16777215))
        self.lineEdit_26.setObjectName("lineEdit_26")
        self.gridLayout.addWidget(self.lineEdit_26, 9, 3, 1, 1)
        self.lineEdit_27 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_27.setMaximumSize(QtCore.QSize(100, 16777215))
        self.lineEdit_27.setObjectName("lineEdit_27")
        self.gridLayout.addWidget(self.lineEdit_27, 9, 4, 1, 1)
        self.lineEdit_31 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_31.setMaximumSize(QtCore.QSize(100, 16777215))
        self.lineEdit_31.setObjectName("lineEdit_31")
        self.gridLayout.addWidget(self.lineEdit_31, 10, 2, 1, 1)
        self.lineEdit_29 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_29.setMaximumSize(QtCore.QSize(100, 16777215))
        self.lineEdit_29.setObjectName("lineEdit_29")
        self.gridLayout.addWidget(self.lineEdit_29, 10, 3, 1, 1)
        self.lineEdit_30 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_30.setMaximumSize(QtCore.QSize(100, 16777215))
        self.lineEdit_30.setObjectName("lineEdit_30")
        self.gridLayout.addWidget(self.lineEdit_30, 10, 4, 1, 1)
        self.lineEdit_34 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_34.setMaximumSize(QtCore.QSize(100, 16777215))
        self.lineEdit_34.setObjectName("lineEdit_34")
        self.gridLayout.addWidget(self.lineEdit_34, 11, 2, 1, 1)
        self.lineEdit_32 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_32.setMaximumSize(QtCore.QSize(100, 16777215))
        self.lineEdit_32.setObjectName("lineEdit_32")
        self.gridLayout.addWidget(self.lineEdit_32, 11, 3, 1, 1)
        self.lineEdit_33 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_33.setMaximumSize(QtCore.QSize(100, 16777215))
        self.lineEdit_33.setObjectName("lineEdit_33")
        self.gridLayout.addWidget(self.lineEdit_33, 11, 4, 1, 1)
        self.lineEdit_37 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_37.setMaximumSize(QtCore.QSize(100, 16777215))
        self.lineEdit_37.setObjectName("lineEdit_37")
        self.gridLayout.addWidget(self.lineEdit_37, 12, 2, 1, 1)
        self.lineEdit_36 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_36.setMaximumSize(QtCore.QSize(100, 16777215))
        self.lineEdit_36.setObjectName("lineEdit_36")
        self.gridLayout.addWidget(self.lineEdit_36, 12, 3, 1, 1)
        self.lineEdit_35 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_35.setMaximumSize(QtCore.QSize(100, 16777215))
        self.lineEdit_35.setObjectName("lineEdit_35")
        self.gridLayout.addWidget(self.lineEdit_35, 12, 4, 1, 1)
        self.lineEdit_40 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_40.setMaximumSize(QtCore.QSize(100, 16777215))
        self.lineEdit_40.setObjectName("lineEdit_40")
        self.gridLayout.addWidget(self.lineEdit_40, 13, 2, 1, 1)
        self.lineEdit_38 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_38.setMaximumSize(QtCore.QSize(100, 16777215))
        self.lineEdit_38.setObjectName("lineEdit_38")
        self.gridLayout.addWidget(self.lineEdit_38, 13, 3, 1, 1)
        self.lineEdit_39 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_39.setMaximumSize(QtCore.QSize(100, 16777215))
        self.lineEdit_39.setObjectName("lineEdit_39")
        self.gridLayout.addWidget(self.lineEdit_39, 13, 4, 1, 1)
        self.label_68 = QtWidgets.QLabel(Dialog)
        self.label_68.setGeometry(QtCore.QRect(20, 410, 143, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.label_68.setFont(font)
        self.label_68.setObjectName("label_68")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(150, 410, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label_69 = QtWidgets.QLabel(Dialog)
        self.label_69.setGeometry(QtCore.QRect(20, 450, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_69.setFont(font)
        self.label_69.setObjectName("label_69")
        self.lineEdit_41 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_41.setGeometry(QtCore.QRect(150, 450, 113, 20))
        self.lineEdit_41.setObjectName("lineEdit_41")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def calc_TCF(self):
        self.total_TCF = self.T1 = self.T2 = self.T3 = self.T4 = self.T5 = self.T6 = self.T7 = self.T8 = self.T9 = self.T10 = self.T11 = self.T12 = self.T13 = 0
        self.T1 += (float(self.lineEdit_2.text()) * float(self.lineEdit_3.text()))
        self.lineEdit_4.setText(str(self.T1))
        self.T2 += (float(self.lineEdit_5.text()) * float(self.lineEdit_6.text()))
        self.lineEdit_7.setText(str(self.T2))
        self.T3 += (float(self.lineEdit_10.text()) * float(self.lineEdit_8.text()))
        self.lineEdit_9.setText(str(self.T3))
        self.T4 += (float(self.lineEdit_13.text()) * float(self.lineEdit_11.text()))
        self.lineEdit_12.setText(str(self.T4))
        self.T5 += (float(self.lineEdit_16.text()) * float(self.lineEdit_15.text()))
        self.lineEdit_14.setText(str(self.T5))
        self.T6 += (float(self.lineEdit_19.text()) * float(self.lineEdit_18.text()))
        self.lineEdit_17.setText(str(self.T6))
        self.T7 += (float(self.lineEdit_22.text()) * float(self.lineEdit_21.text()))
        self.lineEdit_20.setText(str(self.T7))
        self.T8 += (float(self.lineEdit_25.text()) * float(self.lineEdit_24.text()))
        self.lineEdit_23.setText(str(self.T8))
        self.T9 += (float(self.lineEdit_26.text()) * float(self.lineEdit_28.text()))
        self.lineEdit_27.setText(str(self.T9))
        self.T10 += (float(self.lineEdit_29.text()) * float(self.lineEdit_31.text()))
        self.lineEdit_30.setText(str(self.T10))
        self.T11 += (float(self.lineEdit_34.text()) * float(self.lineEdit_32.text()))
        self.lineEdit_33.setText(str(self.T11))
        self.T12 += (float(self.lineEdit_37.text()) * float(self.lineEdit_36.text()))
        self.lineEdit_35.setText(str(self.T12))
        self.T13 += (float(self.lineEdit_40.text()) * float(self.lineEdit_38.text()))
        self.lineEdit_39.setText(str(self.T13))

        self.total_TCF = self.T1 + self.T2 + self.T3 + self.T4 + self.T5 + self.T6 + self.T7 + self.T8 + self.T9 + self.T10 + self.T11 + self.T12 + self.T13
        self.lineEdit.setText(str(self.total_TCF))
        # self.TCF = 0.6 + (0.1 * self.total_TCF)
        self.TCF = round(decimal.Decimal(str(0.6 + (0.1 * self.total_TCF))), 2)
        self.lineEdit_41.setText(str(self.TCF))
        self.set_tcf_value(self.TCF)

    def set_tcf_value(self, value):
            self.result = value

    def get_tcf_value(self):
            return self.result

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_21.setText(_translate("Dialog", "T4"))
        self.label_22.setText(_translate("Dialog", "T5"))
        self.label_46.setText(_translate("Dialog", "Portable"))
        self.label_47.setText(_translate("Dialog", "Easy to change"))
        self.label_24.setText(_translate("Dialog", "T7"))
        self.label_20.setText(_translate("Dialog", "T3"))
        self.label_23.setText(_translate("Dialog", "T6"))
        self.label_19.setText(_translate("Dialog", "T2"))
        self.label_41.setText(_translate("Dialog", "T10"))
        self.label_43.setText(_translate("Dialog", "T9"))
        self.label_45.setText(_translate("Dialog", "T12"))
        self.label_44.setText(_translate("Dialog", "T11"))
        self.label_18.setText(_translate("Dialog", "Easy to Use"))
        self.label_14.setText(_translate("Dialog", "End User Efficiency"))
        self.label_17.setText(_translate("Dialog", "Easy to Install"))
        self.label_16.setText(_translate("Dialog", "Complex Internal Processing"))
        self.label_15.setText(_translate("Dialog", "Reusability"))
        self.label_50.setText(_translate("Dialog", "Provide direct access for external data"))
        self.label_49.setText(_translate("Dialog", "Special Security Features"))
        self.label.setText(_translate("Dialog", "Factor"))
        self.label_42.setText(_translate("Dialog", "T8"))
        self.label_10.setText(_translate("Dialog", "Weight"))
        self.label_12.setText(_translate("Dialog", "Impact"))
        self.label_11.setText(_translate("Dialog", "Rated Value"))
        self.label_8.setText(_translate("Dialog", "Description"))
        self.label_2.setText(_translate("Dialog", "T1"))
        self.label_3.setText(_translate("Dialog", "Distributed System"))
        self.label_7.setText(_translate("Dialog", "Performance"))
        self.label_48.setText(_translate("Dialog", "Concurrent"))
        self.label_66.setText(_translate("Dialog", "Special user training facilities are required"))
        self.label_67.setText(_translate("Dialog", "T13"))
        self.lineEdit_2.setText(_translate("Dialog", "2"))
        self.lineEdit_3.setText(_translate("Dialog", "5"))
        self.lineEdit_4.setText(_translate("Dialog", "10"))
        self.lineEdit_5.setText(_translate("Dialog", "1"))
        self.lineEdit_6.setText(_translate("Dialog", "4"))
        self.lineEdit_7.setText(_translate("Dialog", "4"))
        self.lineEdit_10.setText(_translate("Dialog", "1"))
        self.lineEdit_8.setText(_translate("Dialog", "2"))
        self.lineEdit_9.setText(_translate("Dialog", "2"))
        self.lineEdit_13.setText(_translate("Dialog", "1"))
        self.lineEdit_11.setText(_translate("Dialog", "4"))
        self.lineEdit_12.setText(_translate("Dialog", "4"))
        self.lineEdit_16.setText(_translate("Dialog", "1"))
        self.lineEdit_15.setText(_translate("Dialog", "2"))
        self.lineEdit_14.setText(_translate("Dialog", "2"))
        self.lineEdit_19.setText(_translate("Dialog", "0.5"))
        self.lineEdit_18.setText(_translate("Dialog", "5"))
        self.lineEdit_17.setText(_translate("Dialog", "2.5"))
        self.lineEdit_22.setText(_translate("Dialog", "0.5"))
        self.lineEdit_21.setText(_translate("Dialog", "3"))
        self.lineEdit_20.setText(_translate("Dialog", "1.5"))
        self.lineEdit_25.setText(_translate("Dialog", "2"))
        self.lineEdit_24.setText(_translate("Dialog", "3"))
        self.lineEdit_23.setText(_translate("Dialog", "6"))
        self.lineEdit_28.setText(_translate("Dialog", "1"))
        self.lineEdit_26.setText(_translate("Dialog", "3"))
        self.lineEdit_27.setText(_translate("Dialog", "3"))
        self.lineEdit_31.setText(_translate("Dialog", "1"))
        self.lineEdit_29.setText(_translate("Dialog", "2"))
        self.lineEdit_30.setText(_translate("Dialog", "2"))
        self.lineEdit_34.setText(_translate("Dialog", "1"))
        self.lineEdit_32.setText(_translate("Dialog", "2"))
        self.lineEdit_33.setText(_translate("Dialog", "2"))
        self.lineEdit_37.setText(_translate("Dialog", "1"))
        self.lineEdit_36.setText(_translate("Dialog", "5"))
        self.lineEdit_35.setText(_translate("Dialog", "5"))
        self.lineEdit_40.setText(_translate("Dialog", "1"))
        self.lineEdit_38.setText(_translate("Dialog", "3"))
        self.lineEdit_39.setText(_translate("Dialog", "3"))
        self.label_68.setText(_translate("Dialog", "Total Technical Factor:"))
        self.lineEdit.setText(_translate("Dialog", "47"))
        self.label_69.setText(_translate("Dialog", "TCF:"))
        self.lineEdit_41.setText(_translate("Dialog", "5.3"))
        self.lineEdit_2.textChanged.connect(self.calc_TCF)
        self.lineEdit_3.textChanged.connect(self.calc_TCF)
        self.lineEdit_5.textChanged.connect(self.calc_TCF)
        self.lineEdit_6.textChanged.connect(self.calc_TCF)
        self.lineEdit_10.textChanged.connect(self.calc_TCF)
        self.lineEdit_8.textChanged.connect(self.calc_TCF)
        self.lineEdit_13.textChanged.connect(self.calc_TCF)
        self.lineEdit_11.textChanged.connect(self.calc_TCF)
        self.lineEdit_16.textChanged.connect(self.calc_TCF)
        self.lineEdit_15.textChanged.connect(self.calc_TCF)
        self.lineEdit_18.textChanged.connect(self.calc_TCF)
        self.lineEdit_19.textChanged.connect(self.calc_TCF)
        self.lineEdit_21.textChanged.connect(self.calc_TCF)
        self.lineEdit_22.textChanged.connect(self.calc_TCF)
        self.lineEdit_24.textChanged.connect(self.calc_TCF)
        self.lineEdit_25.textChanged.connect(self.calc_TCF)
        self.lineEdit_26.textChanged.connect(self.calc_TCF)
        self.lineEdit_28.textChanged.connect(self.calc_TCF)
        self.lineEdit_29.textChanged.connect(self.calc_TCF)
        self.lineEdit_31.textChanged.connect(self.calc_TCF)
        self.lineEdit_32.textChanged.connect(self.calc_TCF)
        self.lineEdit_34.textChanged.connect(self.calc_TCF)
        self.lineEdit_36.textChanged.connect(self.calc_TCF)
        self.lineEdit_37.textChanged.connect(self.calc_TCF)
        self.lineEdit_38.textChanged.connect(self.calc_TCF)
        self.lineEdit_40.textChanged.connect(self.calc_TCF)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())