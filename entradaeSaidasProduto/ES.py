from PyQt6 import QtCore, QtGui, QtWidgets
import json

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(817, 503)
        self.gerenciadordenotas = QtWidgets.QTabWidget(parent=Form)
        self.gerenciadordenotas.setGeometry(QtCore.QRect(10, 10, 800, 489))
        self.gerenciadordenotas.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.gerenciadordenotas.setObjectName("gerenciadordenotas")
        self.Saida = QtWidgets.QWidget()
        self.Saida.setObjectName("Saida")
        self.layoutWidget = QtWidgets.QWidget(parent=self.Saida)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 771, 58))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_19 = QtWidgets.QVBoxLayout()
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.labeldescricaoproduto = QtWidgets.QLabel(parent=self.layoutWidget)
        self.labeldescricaoproduto.setObjectName("labeldescricaoproduto")
        self.verticalLayout_19.addWidget(self.labeldescricaoproduto)
        self.linedescricaoproduto = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.linedescricaoproduto.setObjectName("linedescricaoproduto")
        self.verticalLayout_19.addWidget(self.linedescricaoproduto)
        self.horizontalLayout_4.addLayout(self.verticalLayout_19)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.labelquantidade = QtWidgets.QLabel(parent=self.layoutWidget)
        self.labelquantidade.setObjectName("labelquantidade")
        self.verticalLayout_5.addWidget(self.labelquantidade)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.linequantidade = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.linequantidade.setObjectName("linequantidade")
        self.horizontalLayout_3.addWidget(self.linequantidade)
        self.adcionarEntrada = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.adcionarEntrada.setObjectName("adcionarEntrada")
        self.horizontalLayout_3.addWidget(self.adcionarEntrada)

        #chama função adionar ao estoque
        self.adcionarEntrada.clicked.connect(self.entradaProdutos)

        self.verticalLayout_5.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4.addLayout(self.verticalLayout_5)
        self.layoutWidget_2 = QtWidgets.QWidget(parent=self.Saida)
        self.layoutWidget_2.setGeometry(QtCore.QRect(10, 80, 771, 361))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.tabelaEntradas = QtWidgets.QTreeWidget(parent=self.layoutWidget_2)
        self.tabelaEntradas.setObjectName("tabelaEntradas")
        self.horizontalLayout_6.addWidget(self.tabelaEntradas)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.btEntrarEntradas = QtWidgets.QPushButton(parent=self.layoutWidget_2)
        self.btEntrarEntradas.setObjectName("btEntrarEntradas")
        self.verticalLayout_6.addWidget(self.btEntrarEntradas)

        #cahama função que limpa a widgwet
        self.btEntrarEntradas.clicked.connect(self.limpaWidgetE)

        self.btncancelarEntradas = QtWidgets.QPushButton(parent=self.layoutWidget_2)
        self.btncancelarEntradas.setObjectName("btncancelarEntradas")

        #chama a função que limpa a widget ao clicar em cancelar
        self.btncancelarEntradas.clicked.connect(self.limpaWidgetE)

        self.verticalLayout_6.addWidget(self.btncancelarEntradas)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_6.addItem(spacerItem)
        self.horizontalLayout_6.addLayout(self.verticalLayout_6)
        self.gerenciadordenotas.addTab(self.Saida, "")
        self.Entrada = QtWidgets.QWidget()
        self.Entrada.setObjectName("Entrada")
        self.layoutWidget_3 = QtWidgets.QWidget(parent=self.Entrada)
        self.layoutWidget_3.setGeometry(QtCore.QRect(10, 10, 771, 58))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget_3)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.labelDescricaoVendas = QtWidgets.QLabel(parent=self.layoutWidget_3)
        self.labelDescricaoVendas.setObjectName("labelDescricaoVendas")
        self.verticalLayout_4.addWidget(self.labelDescricaoVendas)
        self.lineDescricaoVendas = QtWidgets.QLineEdit(parent=self.layoutWidget_3)
        self.lineDescricaoVendas.setObjectName("lineDescricaoVendas")
        self.verticalLayout_4.addWidget(self.lineDescricaoVendas)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.labelvendas = QtWidgets.QLabel(parent=self.layoutWidget_3)
        self.labelvendas.setObjectName("labelvendas")
        self.verticalLayout.addWidget(self.labelvendas)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineQuantidadeVendas = QtWidgets.QLineEdit(parent=self.layoutWidget_3)
        self.lineQuantidadeVendas.setObjectName("lineQuantidadeVendas")
        self.horizontalLayout.addWidget(self.lineQuantidadeVendas)
        self.btnadiocarVendas = QtWidgets.QPushButton(parent=self.layoutWidget_3)
        self.btnadiocarVendas.setObjectName("btnadiocarVendas")
        self.horizontalLayout.addWidget(self.btnadiocarVendas)

        #chama a função adiona a tabela vendas
        self.btnadiocarVendas.clicked.connect(self.venderProdutos)

        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.layoutWidget_4 = QtWidgets.QWidget(parent=self.Entrada)
        self.layoutWidget_4.setGeometry(QtCore.QRect(10, 80, 771, 361))
        self.layoutWidget_4.setObjectName("layoutWidget_4")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.layoutWidget_4)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.tabelavendas = QtWidgets.QTreeWidget(parent=self.layoutWidget_4)
        self.tabelavendas.setObjectName("tabelavendas")
        self.horizontalLayout_5.addWidget(self.tabelavendas)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.btnvenderVendas = QtWidgets.QPushButton(parent=self.layoutWidget_4)
        self.btnvenderVendas.setObjectName("btnvenderVendas")
        self.verticalLayout_2.addWidget(self.btnvenderVendas)

        #chama função limpa formulário
        self.btnvenderVendas.clicked.connect(self.limpaWidgetS)

        self.btnCancelarVendas = QtWidgets.QPushButton(parent=self.layoutWidget_4)
        self.btnCancelarVendas.setObjectName("btnCancelarVendas")
        self.verticalLayout_2.addWidget(self.btnCancelarVendas)

        #chama a função limpar widget ao clique do botao cancel
        self.btnCancelarVendas.clicked.connect(self.limpaWidgetS)

        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.label_2 = QtWidgets.QLabel(parent=self.layoutWidget_4)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.label = QtWidgets.QLabel(parent=self.layoutWidget_4)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.horizontalLayout_5.addLayout(self.verticalLayout_2)
        self.gerenciadordenotas.addTab(self.Entrada, "")

        self.retranslateUi(Form)
        self.gerenciadordenotas.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.labeldescricaoproduto.setText(_translate("Form", "Descrição ou código do produto"))
        self.labelquantidade.setText(_translate("Form", "Quantidade"))
        self.adcionarEntrada.setText(_translate("Form", "Adicionar"))
        self.tabelaEntradas.headerItem().setText(0, _translate("Form", "Descrição "))
        self.tabelaEntradas.headerItem().setText(1, _translate("Form", "Quantidade"))
        self.btEntrarEntradas.setText(_translate("Form", "Entrar"))
        self.btncancelarEntradas.setText(_translate("Form", "Cancel"))
        self.gerenciadordenotas.setTabText(self.gerenciadordenotas.indexOf(self.Saida), _translate("Form", "Entradas"))
        self.labelDescricaoVendas.setText(_translate("Form", "Descrição ou código do produto"))
        self.labelvendas.setText(_translate("Form", "Quantidade"))
        self.btnadiocarVendas.setText(_translate("Form", "Adicionar"))
        self.tabelavendas.headerItem().setText(0, _translate("Form", "Descrição "))
        self.tabelavendas.headerItem().setText(1, _translate("Form", "Quantidade"))
        self.btnvenderVendas.setText(_translate("Form", "Vender"))
        self.btnCancelarVendas.setText(_translate("Form", "Cancel"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Total</span></p></body></html>"))
        self.label.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" color:#ff0000;\">0,00</span></p></body></html>"))
        self.gerenciadordenotas.setTabText(self.gerenciadordenotas.indexOf(self.Entrada), _translate("Form", "Saídas"))

        self.count = 0
        self.c = 0
        self.valor = [0,00]

    #função entrada de produtos
    def entradaProdutos(self):
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

            descricaoEntrada = self.linedescricaoproduto.text()
            quantidadeEntrada = self.linequantidade.text()
           
            #Insere dados na tabela
            cursor.execute("SELECT * FROM produtos WHERE upper(descricao) LIKE upper('%s')"  %(descricaoEntrada) ) # Lê os dados

            #print(cursor.fetchall()) # Mostra os dados lidos
            strjson = json.loads(json.dumps(cursor.fetchall()))
            
            if strjson == []:
                           
                #Insere dados na tabela
                cursor.execute("SELECT * FROM produtos WHERE id = '%s'" %(descricaoEntrada) ) # Lê os dados

                #print(cursor.fetchall()) # Mostra os dados lidos
                strjson = json.loads(json.dumps(cursor.fetchall()))

            # btn = self.btEntrarEntradas

            for chave in strjson:
               
                print(chave["id"], chave["descricao"], chave["categoria"], chave["preco"], chave["localizacao"], chave["estoque"], chave["estoque_min"], chave["estoque_min"])

                cursor.execute("UPDATE produtos set estoque = estoque + '%s' WHERE id = '%s'" %(quantidadeEntrada,chave["id"]))
                self.connection.commit()
                
                item_0 = QtWidgets.QTreeWidgetItem(self.tabelaEntradas)
                # item_0 = QtWidgets.QTreeWidgetItem(self.tabelaEntradas)
                self.tabelaEntradas.topLevelItem(self.count).setText(0, _translate("Entradasesaidas", chave["descricao"]))
                self.tabelaEntradas.topLevelItem(self.count).setText(1, _translate("Entradasesaidas", quantidadeEntrada))

                self.count = self.count + 1

            self.linedescricaoproduto.setText('')
            self.linequantidade.setText('')
        finally:
            self.connection.close()


    #função saídas
    def venderProdutos(self):        
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

            descricaoEntrada = self.lineDescricaoVendas.text()
            quantidadeEntrada = self.lineQuantidadeVendas.text()
           
            #Insere dados na tabela
            cursor.execute("SELECT * FROM produtos WHERE upper(descricao) LIKE upper('%s')"  %(descricaoEntrada) ) # Lê os dados

            #print(cursor.fetchall()) # Mostra os dados lidos
            strjsonV = json.loads(json.dumps(cursor.fetchall()))
            
            if strjsonV == []:
                           
                #Insere dados na tabela
                cursor.execute("SELECT * FROM produtos WHERE id = '%s'" %(descricaoEntrada) ) # Lê os dados

                #print(cursor.fetchall()) # Mostra os dados lidos
                strjsonV = json.loads(json.dumps(cursor.fetchall()))
            
            for chave in strjsonV:

                estoque = chave["estoque"]
        
                print(chave["id"], chave["descricao"], chave["categoria"], chave["preco"], chave["localizacao"], chave["estoque"], chave["estoque_min"], chave["estoque_min"])
                if int(estoque) > int(quantidadeEntrada):

                    cursor.execute("UPDATE produtos set estoque = estoque - '%s' WHERE id = '%s'" %(quantidadeEntrada,chave["id"]))
                    
                    self.connection.commit()

                    item_0 = QtWidgets.QTreeWidgetItem(self.tabelavendas)
                    # item_0 = QtWidgets.QTreeWidgetItem(self.tabelaEntradas)
                    self.tabelavendas.topLevelItem(self.c).setText(0, _translate("Entradasesaidas", chave["descricao"]))
                    self.tabelavendas.topLevelItem(self.c).setText(1, _translate("Entradasesaidas", quantidadeEntrada))

                    self.c = self.c + 1 
                   
                    preco = float(chave["preco"]) * float(quantidadeEntrada)    
                    self.valor.append(preco)
                    self.label.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" color:#ff0000;\">%s</span></p></body></html>")%(str(sum(self.valor))))   
                else:
                    from entradaeSaidasProduto.avisos.aviso import Ui_Sobre
                    self.window = QtWidgets.QMainWindow()
                    self.aviso = Ui_Sobre()
                    self.aviso.setupUi(self.window)
                    self.window.show()
                   
            self.lineDescricaoVendas.setText('')
            self.lineQuantidadeVendas.setText('')
        finally:
            self.connection.close()   
        
        

#btEntrarEntradas
    def limpaWidgetS(self):
        _translate = QtCore.QCoreApplication.translate
        self.tabelavendas.clear()
        self.c = 0
        self.lineDescricaoVendas.setText('')
        self.lineQuantidadeVendas.setText('')
        self.valor = [0,00]
        self.label.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" color:#ff0000;\">0,00</span></p></body></html>"))
        
    def limpaWidgetE(self):
        self.tabelaEntradas.clear()
        self.count = 0
        self.linedescricaoproduto.setText('')
        self.linequantidade.setText('')

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
