from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(812, 584)
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(110, 60, 591, 391))
        self.tableWidget.setAutoFillBackground(False)
        self.tableWidget.setDragEnabled(True)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnWidth(0, 116)
        self.tableWidget.setColumnWidth(1,116)
        self.tableWidget.setColumnWidth(2, 116)
        self.tableWidget.setColumnWidth(3, 116)
        self.tableWidget.setColumnWidth(4, 116)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(300, 20, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(250, 480, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(480, 480, 101, 23))
        self.pushButton_2.setObjectName("pushButton_2")

        #
        self.pushButton.clicked.connect(self.add_row)
        #

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def add_row(self):
        print("Adding a row!")
        rowPosition = self.tableWidget.rowCount()
        self.tableWidget.insertRow(rowPosition)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("SMI", "SMI"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "SMI"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Modules Added"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Modules Changed"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Modules Deleted"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Total Modules"))
        self.label.setText(_translate("Form", "Software Maturity Index"))
        self.pushButton.setText(_translate("Form", "Add row"))
        self.pushButton_2.setText(_translate("Form", "Compute Index"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
