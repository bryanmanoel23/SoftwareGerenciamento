# Form implementation generated from reading ui file 'avisoCadastrado.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Sobre(object):
    def setupUi(self, Sobre):
        Sobre.setObjectName("Sobre")
        Sobre.resize(362, 125)
        self.label = QtWidgets.QLabel(parent=Sobre)
        self.label.setGeometry(QtCore.QRect(0, 30, 361, 51))
        self.label.setObjectName("label")

        self.retranslateUi(Sobre)
        QtCore.QMetaObject.connectSlotsByName(Sobre)

    def retranslateUi(self, Sobre):
        _translate = QtCore.QCoreApplication.translate
        Sobre.setWindowTitle(_translate("Sobre", "Form"))
        self.label.setText(_translate("Sobre", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Produto cadastrado com sucesso !</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Sobre = QtWidgets.QWidget()
    ui = Ui_Sobre()
    ui.setupUi(Sobre)
    Sobre.show()
    sys.exit(app.exec())
