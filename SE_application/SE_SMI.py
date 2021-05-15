import decimal

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem

class SMI_Ui_Form(object):
    def __init__(self, saved_dict):
        self.new_dict = saved_dict
        self.total_modules = 0
        self.add_modules = 0
        self.changed_modules = 0
        self.del_modules = 0
        self.restore_array = saved_dict

    def setupUi(self, Form, sminame):
        Form.setObjectName("Form")
        Form.resize(812, 584)
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.itemSelectionChanged.connect(self.row_calculations)

        self.tableWidget.setGeometry(QtCore.QRect(110, 60, 591, 391))
        self.tableWidget.setAutoFillBackground(False)
        self.tableWidget.setDragEnabled(True)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnWidth(0, 116)
        self.tableWidget.setColumnWidth(1, 116)
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
        self.tableWidget.insertRow(0)
        self.tableWidget.setItem(0, 1, QTableWidgetItem("0"))
        self.pushButton.clicked.connect(self.add_row)
        self.pushButton_2.clicked.connect(self.calculate_smi)
        #

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def row_calculations(self):
        rowPosition = self.tableWidget.rowCount()
        self.set_row_pos(rowPosition)
        if rowPosition == 1:
            newitem = QTableWidgetItem(str(self.tableWidget.item(0, 1).text()))
            self.tableWidget.setItem(0, 4, newitem)

            newitem = QTableWidgetItem(str(0.0))
            self.tableWidget.setItem(rowPosition - 1, 0, newitem)
        else:
            prev_total_modules = int(self.tableWidget.item(rowPosition - 2, 4).text())
            if self.tableWidget.item(rowPosition - 1, 3):
                del_modules = int(self.tableWidget.item(rowPosition - 1, 3).text())
                self.set_del_modules(del_modules)
            else:
                del_modules = 0
                self.set_del_modules(del_modules)

            if self.tableWidget.item(rowPosition - 1, 2):
                changed_modules = int(self.tableWidget.item(rowPosition - 1, 2).text())
                self.set_changed_modules(changed_modules)
            else:
                changed_modules = 0
                self.set_changed_modules(changed_modules)

            if self.tableWidget.item(rowPosition - 1, 1):
                added_modules = int(self.tableWidget.item(rowPosition - 1, 1).text())
                self.set_add_modules(added_modules)
            else:
                added_modules = 0
                self.set_add_modules(added_modules)

            total_modules = prev_total_modules - del_modules + added_modules
            self.set_total_modules(total_modules)

            newitem = QTableWidgetItem(str(total_modules))
            self.tableWidget.setItem(rowPosition - 1, 4, newitem)

    def set_row_pos(self, value):
        self.rowpositon = value

    def set_del_modules(self, value):
        self.del_modules = value

    def set_add_modules(self, value):
        self.add_modules = value

    def set_changed_modules(self, value):
        self.changed_modules = value

    def set_total_modules(self, value):
        self.total_modules = value

    def get_total_modules(self):
        return self.total_modules

    def get_del_modules(self):
        return self.del_modules

    def get_add_modules(self):
        return self.add_modules

    def get_changed_modules(self):
        return self.changed_modules

    def calculate_smi(self):
        if self.rowpositon == 1:
            return
        smi = (self.total_modules - (self.add_modules + self.changed_modules + self.del_modules)) / self.total_modules
        smi = round(decimal.Decimal(str(smi)), 8)
        newitem = QTableWidgetItem(str(smi))
        self.tableWidget.setItem(self.rowpositon - 1, 0, newitem)
        # self.save()

    def add_row(self):
        rowPosition = self.tableWidget.rowCount()
        self.tableWidget.insertRow(rowPosition)

    def save(self):
        self.new_arr = []
        for row in range(self.tableWidget.rowCount()):
            for col in range(self.tableWidget.columnCount()):
                _item = self.tableWidget.item(row, col)
                if _item:
                    item = self.tableWidget.item(row, col).text()
                    self.new_arr.append(item)
                else:
                    item = 0
                    self.new_arr.append(item)
        self.new_arr.append(self.tableWidget.rowCount())
        return self.new_arr

    def restore_data(self):
        rowcount = self.restore_array[len(self.restore_array) - 1]
        for i in range(rowcount - 1):
            self.add_row()

        count = 0
        for row in range(rowcount):
            for col in range(5):
                value = self.restore_array[count]
                count += 1
                newitem = QTableWidgetItem(str(value))
                self.tableWidget.setItem(row, col, newitem)
        self.row_calculations()

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
    rand_dict = {}
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = SMI_Ui_Form(rand_dict)
    ui.setupUi(Form, "abc")
    Form.show()
    sys.exit(app.exec_())
