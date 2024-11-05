from PyQt6 import QtCore, QtGui, QtWidgets
import json

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(847, 540)
        self.label = QtWidgets.QLabel(parent=Form)
        self.label.setGeometry(QtCore.QRect(310, 10, 231, 31))
        self.label.setStyleSheet("font: 16pt \"Times New Roman\";")
        self.label.setObjectName("label")
        self.btnAtualizaTabelas = QtWidgets.QPushButton(parent=Form)
        self.btnAtualizaTabelas.setGeometry(QtCore.QRect(650, 30, 171, 31))
        self.btnAtualizaTabelas.setObjectName("btnAtualizaTabelas")

        #chama a função que exibe os estado dos relatório dos produtos 
        self.btnAtualizaTabelas.clicked.connect(self.listaRelatorio)


        self.layoutWidget = QtWidgets.QWidget(parent=Form)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 290, 811, 22))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.labelEstMinimo = QtWidgets.QLabel(parent=self.layoutWidget)
        self.labelEstMinimo.setStyleSheet("font: 12pt \"Times New Roman\";")
        self.labelEstMinimo.setObjectName("labelEstMinimo")
        self.horizontalLayout.addWidget(self.labelEstMinimo)
        self.labelEstMax = QtWidgets.QLabel(parent=self.layoutWidget)
        self.labelEstMax.setStyleSheet("font: 12pt \"Times New Roman\";")
        self.labelEstMax.setObjectName("labelEstMax")
        self.horizontalLayout.addWidget(self.labelEstMax)
        self.layoutWidget1 = QtWidgets.QWidget(parent=Form)
        self.layoutWidget1.setGeometry(QtCore.QRect(20, 320, 801, 194))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.TableEstMin = QtWidgets.QTreeWidget(parent=self.layoutWidget1)
        self.TableEstMin.setObjectName("TableEstMin")

        self.horizontalLayout_2.addWidget(self.TableEstMin)
        self.TableEstMax = QtWidgets.QTreeWidget(parent=self.layoutWidget1)
        self.TableEstMax.setObjectName("TableEstMax")

        self.horizontalLayout_2.addWidget(self.TableEstMax)
        self.layoutWidget2 = QtWidgets.QWidget(parent=Form)
        self.layoutWidget2.setGeometry(QtCore.QRect(20, 60, 801, 219))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.labelEstNormal = QtWidgets.QLabel(parent=self.layoutWidget2)
        self.labelEstNormal.setStyleSheet("font: 12pt \"Times New Roman\";")
        self.labelEstNormal.setObjectName("labelEstNormal")
        self.verticalLayout.addWidget(self.labelEstNormal)
        self.TableEstNormal = QtWidgets.QTreeWidget(parent=self.layoutWidget2)
        self.TableEstNormal.setObjectName("TableEstNormal")

        self.verticalLayout.addWidget(self.TableEstNormal)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Relatório de Estoque"))
        self.label.setText(_translate("Form", "<html><head/><body><p align=\"center\">Relatórios de estoque </p><p align=\"center\"><br/></p></body></html>"))
        self.btnAtualizaTabelas.setText(_translate("Form", "Atualizar Listas"))
        self.labelEstMinimo.setText(_translate("Form", "<html><head/><body><p>Produtos com estoque <span style=\" color:#ff0000;\">menor </span>que o estoque minímo </p></body></html>"))
        self.labelEstMax.setText(_translate("Form", "<html><head/><body><p>Produtos com estoque <span style=\" color:#ff0000;\">maior</span> que o estoque máximo</p></body></html>"))
        self.TableEstMin.headerItem().setText(0, _translate("Form", "Descrição"))
        self.TableEstMin.headerItem().setText(1, _translate("Form", "Estoque "))
        self.TableEstMin.headerItem().setText(2, _translate("Form", "Estoque minímo"))
        self.TableEstMin.headerItem().setText(3, _translate("Form", "Estoque máximo"))
        self.TableEstMin.headerItem().setText(4, _translate("Form", "Valor"))
        __sortingEnabled = self.TableEstMin.isSortingEnabled()
        self.TableEstMin.setSortingEnabled(False)

        self.TableEstMin.setSortingEnabled(__sortingEnabled)
        self.TableEstMax.headerItem().setText(0, _translate("Form", "Descrição "))
        self.TableEstMax.headerItem().setText(1, _translate("Form", "Estoque "))
        self.TableEstMax.headerItem().setText(2, _translate("Form", "Estoque minímo"))
        self.TableEstMax.headerItem().setText(3, _translate("Form", "Estoque máximo"))
        self.TableEstMax.headerItem().setText(4, _translate("Form", "Valor"))
        __sortingEnabled = self.TableEstMax.isSortingEnabled()
        self.TableEstMax.setSortingEnabled(False)

        self.TableEstMax.setSortingEnabled(__sortingEnabled)
        self.labelEstNormal.setText(_translate("Form", "<html><head/><body><p>Produtos com estoque <span style=\" color:#ff0000;\">normal</span></p></body></html>"))
        self.TableEstNormal.headerItem().setText(0, _translate("Form", "Descrição "))
        self.TableEstNormal.headerItem().setText(1, _translate("Form", "Estoque "))
        self.TableEstNormal.headerItem().setText(2, _translate("Form", "Estoque minímo "))
        self.TableEstNormal.headerItem().setText(3, _translate("Form", "Estoque máximo"))
        self.TableEstNormal.headerItem().setText(4, _translate("Form", "valor"))
        __sortingEnabled = self.TableEstNormal.isSortingEnabled()
        self.TableEstNormal.setSortingEnabled(False)

        self.TableEstNormal.setSortingEnabled(__sortingEnabled)
   
    #função relatórios
    def listaRelatorio(self):
        import pymysql
        timeout = 10
        self.connection = pymysql.connect(
        charset="utf8mb4",
        connect_timeout=timeout,
        cursorclass=pymysql.cursors.DictCursor,
        db="ADS2024BRYANMANOEL", # Nome do banco de dados
        host="ads2024bryanmanoel-bryansistemascp-9c0b.i.aivencloud.com", # Host do seu banco
        password="AVNS_uNo_3DU544sdjE2VZxo", # Senha que você revelou no Aiven
        read_timeout=timeout,
        port=22405, # Porta do banco
        user="avnadmin", # Usuário que você viu no Aiven
        write_timeout=timeout,
        )

        _translate = QtCore.QCoreApplication.translate

        try:
            
            cursor = self.connection.cursor()
            #estoque normal
            #Insere dados na tabela
            cursor.execute("SELECT * FROM produtos WHERE estoque > estoque_min and estoque < estoque_max ") # Lê os dados
            
            # print(cursor.fetchall()) # Mostra os dados lidos
            strjson = json.loads(json.dumps(cursor.fetchall()))
            count = 0

            #ESTOQUE MINIMO
            cursor.execute("SELECT * FROM produtos WHERE estoque <= estoque_min")
            minStrJson = json.loads(json.dumps(cursor.fetchall()))
            count2 = 0

                        #ESTOQUE MINIMO
            cursor.execute("SELECT * FROM produtos WHERE estoque >= estoque_max")
            maxStrJson = json.loads(json.dumps(cursor.fetchall()))
            count3 = 0

            for chave in strjson:
                estoque = chave["estoque"]
                estoqueMin = chave["estoque_min"]
                estoqueMax = chave["estoque_max"]
               
                print(chave["id"], chave["descricao"], chave["categoria"], chave["preco"], chave["localizacao"], chave["estoque"], chave["estoque_min"], chave["estoque_max"])
        
                #estoque normal
                item_0 = QtWidgets.QTreeWidgetItem(self.TableEstNormal)
                # item_0 = QtWidgets.QTreeWidgetItem(self.TableEstNormal)
                # item_0 = QtWidgets.QTreeWidgetItem(self.TableEstNormal)

                self.TableEstNormal.topLevelItem(count).setText(0, _translate("Form", chave["descricao"]))
                self.TableEstNormal.topLevelItem(count).setText(1, _translate("Form", str(chave["estoque"])))
                self.TableEstNormal.topLevelItem(count).setText(2, _translate("Form", str(chave["estoque_min"])))
                self.TableEstNormal.topLevelItem(count).setText(3, _translate("Form", str(chave["estoque_max"])))
                self.TableEstNormal.topLevelItem(count).setText(4, _translate("Form", str(chave["preco"])))
                count = count + 1

            for chave in  minStrJson:
                estoque = chave["estoque"]
                estoqueMin = chave["estoque_min"]
                estoqueMax = chave["estoque_max"]
               
                print(chave["id"], chave["descricao"], chave["categoria"], chave["preco"], chave["localizacao"], chave["estoque"], chave["estoque_min"], chave["estoque_max"])
                
                #estoque minimo
                item_0 = QtWidgets.QTreeWidgetItem(self.TableEstMin)
                item_0 = QtWidgets.QTreeWidgetItem(self.TableEstMin)
                item_0 = QtWidgets.QTreeWidgetItem(self.TableEstMin)

                self.TableEstMin.topLevelItem(count2).setText(0, _translate("Form", chave["descricao"]))
                self.TableEstMin.topLevelItem(count2).setText(1, _translate("Form", str(chave["estoque"])))
                self.TableEstMin.topLevelItem(count2).setText(2, _translate("Form", str(chave["estoque_min"])))
                self.TableEstMin.topLevelItem(count2).setText(3, _translate("Form", str(chave["estoque_max"])))
                self.TableEstMin.topLevelItem(count2).setText(4, _translate("Form", str(chave["preco"])))

                count2 = count2 + 1

            for chave in maxStrJson:
                estoque = chave["estoque"]
                estoqueMin = chave["estoque_min"]
                estoqueMax = chave["estoque_max"]
               
                print(chave["id"], chave["descricao"], chave["categoria"], chave["preco"], chave["localizacao"], chave["estoque"], chave["estoque_min"], chave["estoque_max"])
            
                #estoque maximo
                item_0 = QtWidgets.QTreeWidgetItem(self.TableEstMax)

                self.TableEstMax.topLevelItem(count3).setText(0, _translate("Form", chave["descricao"]))
                self.TableEstMax.topLevelItem(count3).setText(1, _translate("Form", str(chave["estoque"])))
                self.TableEstMax.topLevelItem(count3).setText(2, _translate("Form", str(chave["estoque_min"])))
                self.TableEstMax.topLevelItem(count3).setText(3, _translate("Form", str(chave["estoque_max"])))
                self.TableEstMax.topLevelItem(count3).setText(4, _translate("Form", str(chave["preco"])))

                count3 = count3 + 1
       
        finally:
            self.connection.close()
    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
