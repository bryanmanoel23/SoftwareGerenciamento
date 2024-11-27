from PyQt6 import QtCore, QtGui, QtWidgets
import json

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(854, 527)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.botao_produtos = QtWidgets.QPushButton(parent=self.frame)
        self.botao_produtos.setObjectName("botao_produtos")
        self.horizontalLayout.addWidget(self.botao_produtos)

        #chama tela relatorios
        self.botao_produtos.clicked.connect(self.show_relatorio)


        self.botao_localizarProd = QtWidgets.QPushButton(parent=self.frame)
        self.botao_localizarProd.setObjectName("botao_localizarProd")
        self.horizontalLayout.addWidget(self.botao_localizarProd)

        #chama a função mostrar telas entradas e saídas
        self.botao_localizarProd.clicked.connect(self.show_entradasesaidas)

        self.botao_atuaza = QtWidgets.QPushButton(parent=self.frame)
        self.botao_atuaza.setObjectName("botao_atuaza")
        self.horizontalLayout.addWidget(self.botao_atuaza)

        #chama janela sobre
        self.botao_atuaza.clicked.connect(self.show_sobre)

        self.verticalLayout_2.addWidget(self.frame)
        self.Editaproduto = QtWidgets.QStackedWidget(parent=self.centralwidget)
        self.Editaproduto.setObjectName("Editaproduto")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.page)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.window_produto = QtWidgets.QTabWidget(parent=self.page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.window_produto.sizePolicy().hasHeightForWidth())
        self.window_produto.setSizePolicy(sizePolicy)
        self.window_produto.setObjectName("window_produto")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.labelnomesparaprocurarproduto = QtWidgets.QLabel(parent=self.tab)
        self.labelnomesparaprocurarproduto.setGeometry(QtCore.QRect(10, 10, 191, 16))
        self.labelnomesparaprocurarproduto.setObjectName("labelnomesparaprocurarproduto")
        self.frame_2 = QtWidgets.QFrame(parent=self.tab)
        self.frame_2.setGeometry(QtCore.QRect(520, 30, 95, 101))
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.telaproduto = QtWidgets.QTreeWidget(parent=self.tab)
        self.telaproduto.setGeometry(QtCore.QRect(10, 90, 581, 271))
        self.telaproduto.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.telaproduto.setObjectName("telaproduto")
        # item_0 = QtWidgets.QTreeWidgetItem(self.telaproduto)
        # item_0 = QtWidgets.QTreeWidgetItem(self.telaproduto)
        self.layoutWidget = QtWidgets.QWidget(parent=self.tab)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 40, 501, 25))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.inputparaselecionarproduto = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.inputparaselecionarproduto.setObjectName("inputparaselecionarproduto")
        self.horizontalLayout_2.addWidget(self.inputparaselecionarproduto)
        self.botaoprocurarproduto = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.botaoprocurarproduto.setObjectName("botaoprocurarproduto")

        #chama a função de de busca que adiciona a tabela 
        self.botaoprocurarproduto.clicked.connect(self.localizaProduto)


        self.horizontalLayout_2.addWidget(self.botaoprocurarproduto)
        self.window_produto.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.labeltitulo = QtWidgets.QLabel(parent=self.tab_2)
        self.labeltitulo.setGeometry(QtCore.QRect(310, 10, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.labeltitulo.setFont(font)
        self.labeltitulo.setStyleSheet("font: 14pt \"Times New Roman\";")
        self.labeltitulo.setObjectName("labeltitulo")
        self.comLocalizacao = QtWidgets.QComboBox(parent=self.tab_2)
        self.comLocalizacao.setGeometry(QtCore.QRect(550, 90, 181, 21))
        self.comLocalizacao.setObjectName("comLocalizacao")
        self.comLocalizacao.addItem("")
        self.comLocalizacao.setItemText(0, "")
        self.comLocalizacao.addItem("")
        self.comLocalizacao.addItem("")
        self.comLocalizacao.addItem("")
        self.comLocalizacao.addItem("")
        self.comLocalizacao.addItem("")
        self.comLocalizacao.addItem("")
        self.ComboCategoria = QtWidgets.QComboBox(parent=self.tab_2)
        self.ComboCategoria.setGeometry(QtCore.QRect(550, 140, 181, 21))
        self.ComboCategoria.setObjectName("ComboCategoria")
        self.ComboCategoria.addItem("")
        self.ComboCategoria.setItemText(0, "")
        self.ComboCategoria.addItem("")
        self.ComboCategoria.addItem("")
        self.ComboCategoria.addItem("")
        self.ComboCategoria.addItem("")
        self.ComboCategoria.addItem("")
        self.ComboCategoria.addItem("")
        self.ComboCategoria.addItem("")
        self.labellocalizacao = QtWidgets.QLabel(parent=self.tab_2)
        self.labellocalizacao.setGeometry(QtCore.QRect(553, 73, 71, 16))
        self.labellocalizacao.setObjectName("labellocalizacao")
        self.labelcategoria = QtWidgets.QLabel(parent=self.tab_2)
        self.labelcategoria.setGeometry(QtCore.QRect(550, 120, 61, 20))
        self.labelcategoria.setObjectName("labelcategoria")
        self.layoutWidget1 = QtWidgets.QWidget(parent=self.tab_2)
        self.layoutWidget1.setGeometry(QtCore.QRect(20, 70, 451, 41))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.labeldescricaoProduto = QtWidgets.QLabel(parent=self.layoutWidget1)
        self.labeldescricaoProduto.setObjectName("labeldescricaoProduto")
        self.verticalLayout_6.addWidget(self.labeldescricaoProduto)
        self.txt_descricao = QtWidgets.QLineEdit(parent=self.layoutWidget1)
        self.txt_descricao.setObjectName("txt_descricao")
        self.verticalLayout_6.addWidget(self.txt_descricao)
        self.layoutWidget2 = QtWidgets.QWidget(parent=self.tab_2)
        self.layoutWidget2.setGeometry(QtCore.QRect(20, 190, 81, 41))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label = QtWidgets.QLabel(parent=self.layoutWidget2)
        self.label.setObjectName("label")
        self.verticalLayout_5.addWidget(self.label)
        self.precovenda = QtWidgets.QLineEdit(parent=self.layoutWidget2)
        self.precovenda.setObjectName("precovenda")
        self.verticalLayout_5.addWidget(self.precovenda)
        self.alterarProduto = QtWidgets.QPushButton(parent=self.tab_2)
        self.alterarProduto.setGeometry(QtCore.QRect(332, 281, 75, 23))
        self.alterarProduto.setObjectName("alterarProduto")
        self.incluirProduto = QtWidgets.QPushButton(parent=self.tab_2)
        self.incluirProduto.setGeometry(QtCore.QRect(251, 281, 75, 23))
        self.incluirProduto.setObjectName("incluirProduto")
        #chama função adicionar produto 
        self.incluirProduto.clicked.connect(self.adicionaBanco)

        self.Procurar = QtWidgets.QPushButton(parent=self.tab_2)
        self.Procurar.setGeometry(QtCore.QRect(494, 281, 75, 23))
        self.Procurar.setObjectName("Procurar")
        self.excluirProduto = QtWidgets.QPushButton(parent=self.tab_2)
        self.excluirProduto.setGeometry(QtCore.QRect(413, 281, 75, 23))
        self.excluirProduto.setObjectName("excluirProduto")
        self.layoutWidget3 = QtWidgets.QWidget(parent=self.tab_2)
        self.layoutWidget3.setGeometry(QtCore.QRect(20, 130, 419, 43))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.labelestoque = QtWidgets.QLabel(parent=self.layoutWidget3)
        self.labelestoque.setObjectName("labelestoque")
        self.verticalLayout_8.addWidget(self.labelestoque)
        self.txt_estoque = QtWidgets.QLineEdit(parent=self.layoutWidget3)
        self.txt_estoque.setObjectName("txt_estoque")
        self.verticalLayout_8.addWidget(self.txt_estoque)
        self.horizontalLayout_3.addLayout(self.verticalLayout_8)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.labelestoquemin = QtWidgets.QLabel(parent=self.layoutWidget3)
        self.labelestoquemin.setObjectName("labelestoquemin")
        self.verticalLayout_7.addWidget(self.labelestoquemin)
        self.txt_estoquMin = QtWidgets.QLineEdit(parent=self.layoutWidget3)
        self.txt_estoquMin.setObjectName("txt_estoquMin")
        self.verticalLayout_7.addWidget(self.txt_estoquMin)
        self.horizontalLayout_3.addLayout(self.verticalLayout_7)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.labelestoquemax = QtWidgets.QLabel(parent=self.layoutWidget3)
        self.labelestoquemax.setObjectName("labelestoquemax")
        self.verticalLayout_9.addWidget(self.labelestoquemax)
        self.txty_estoqueMax = QtWidgets.QLineEdit(parent=self.layoutWidget3)
        self.txty_estoqueMax.setObjectName("txty_estoqueMax")
        self.verticalLayout_9.addWidget(self.txty_estoqueMax)
        self.horizontalLayout_3.addLayout(self.verticalLayout_9)
        self.window_produto.addTab(self.tab_2, "")
        self.verticalLayout_4.addWidget(self.window_produto)
        self.Editaproduto.addWidget(self.page)
        self.inicial_window = QtWidgets.QWidget()
        self.inicial_window.setObjectName("inicial_window")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.inicial_window)
        self.verticalLayout.setObjectName("verticalLayout")
        self.window_name = QtWidgets.QLabel(parent=self.inicial_window)
        self.window_name.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.window_name.setObjectName("window_name")
        self.verticalLayout.addWidget(self.window_name)
        self.pushButton = QtWidgets.QPushButton(parent=self.inicial_window)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.Editaproduto.addWidget(self.inicial_window)
        self.verticalLayout_2.addWidget(self.Editaproduto)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.Editaproduto.setCurrentIndex(0)
        self.window_produto.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.botao_produtos.setText(_translate("MainWindow", "Relatórios"))
        self.botao_localizarProd.setText(_translate("MainWindow", "Entradas/Saídas"))
        # self.botao_relatorio.setText(_translate("MainWindow", ""))
        self.botao_atuaza.setText(_translate("MainWindow", "Sobre"))
        self.labelnomesparaprocurarproduto.setText(_translate("MainWindow", "Descrição ou código do produto "))
        self.telaproduto.headerItem().setText(0, _translate("MainWindow", "Descrição "))
        self.telaproduto.headerItem().setText(1, _translate("MainWindow", "Localização"))
        __sortingEnabled = self.telaproduto.isSortingEnabled()
        # self.telaproduto.setSortingEnabled(False)
        # self.telaproduto.topLevelItem(0).setText(0, _translate("MainWindow", "Produto teste"))
        # self.telaproduto.topLevelItem(0).setText(1, _translate("MainWindow", "Sessão 01 prateleira 02"))
        # self.telaproduto.topLevelItem(1).setText(0, _translate("MainWindow", "Placa de video RTX 4060"))
        # self.telaproduto.topLevelItem(1).setText(1, _translate("MainWindow", "Sessão 02 prateleira 03"))
        self.telaproduto.setSortingEnabled(__sortingEnabled)
        self.botaoprocurarproduto.setText(_translate("MainWindow", "Procurar"))
        self.window_produto.setTabText(self.window_produto.indexOf(self.tab), _translate("MainWindow", "Restrear Localização Produto"))
        self.labeltitulo.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">Cadastrar produto</span></p></body></html>"))
        self.comLocalizacao.setItemText(1, _translate("MainWindow", "Sessão 01 prateleira 01 "))
        self.comLocalizacao.setItemText(2, _translate("MainWindow", "Sessão 01 prateleira 02"))
        self.comLocalizacao.setItemText(3, _translate("MainWindow", "Sessão 02 prateleira 03 "))
        self.comLocalizacao.setItemText(4, _translate("MainWindow", "Sessão 02 prateleira 04"))
        self.comLocalizacao.setItemText(5, _translate("MainWindow", "Sessão 03 prateleira 05"))
        self.comLocalizacao.setItemText(6, _translate("MainWindow", "Sessão 03 prateleira 06 "))
        self.ComboCategoria.setItemText(1, _translate("MainWindow", "Eletrônicos"))
        self.ComboCategoria.setItemText(2, _translate("MainWindow", "Celulares"))
        self.ComboCategoria.setItemText(3, _translate("MainWindow", "Capinhas "))
        self.ComboCategoria.setItemText(4, _translate("MainWindow", "Peliculas"))
        self.ComboCategoria.setItemText(5, _translate("MainWindow", "Fones"))
        self.ComboCategoria.setItemText(6, _translate("MainWindow", "Caixa de som"))
        self.ComboCategoria.setItemText(7, _translate("MainWindow", "Outros"))
        self.labellocalizacao.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt;\">Localização </span></p></body></html>"))
        self.labelcategoria.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt;\">Categoria</span></p></body></html>"))
        self.labeldescricaoProduto.setText(_translate("MainWindow", "Descrição "))
        self.label.setText(_translate("MainWindow", "Preço Venda"))
        self.alterarProduto.setText(_translate("MainWindow", "Alterar"))
        self.incluirProduto.setText(_translate("MainWindow", "Incluir"))
        self.Procurar.setText(_translate("MainWindow", "Procurar"))
        self.excluirProduto.setText(_translate("MainWindow", "Excluir"))
        self.labelestoque.setText(_translate("MainWindow", "Estoque "))
        self.labelestoquemin.setText(_translate("MainWindow", "Estoque Min"))
        self.labelestoquemax.setText(_translate("MainWindow", "Estoque Max"))
        self.window_produto.setTabText(self.window_produto.indexOf(self.tab_2), _translate("MainWindow", "Cadastro de Produto"))
        self.window_name.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:36pt; font-weight:600; color:#00007f;\">Bryan</span></p><p align=\"center\"><span style=\" font-size:36pt; font-weight:600; color:#00007f;\">sistemas</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Vender"))

    #função adiona banco de dados 
    def adicionaBanco(self):
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
       
        if self.txt_estoque == '':
            self.txt_estoque = 0

        self.descricao = self.txt_descricao.text()

        self.categoria = self.ComboCategoria.currentText()
        
        self.preco = self.precovenda.text().replace(',','.')

        self.localizacao = self.comLocalizacao.currentText()

        self.estoque = self.txt_estoque.text()

        self.estoque_min = self.txt_estoquMin.text()

        self.estoque_max = self.txty_estoqueMax.text()

        print(self.descricao, self.categoria, self.preco, self.localizacao, self.estoque, self.estoque_min, self.estoque_max )
        
        try:
            if self.descricao != '' and self.categoria != '' and self.preco != '' and self.localizacao != '' and self.estoque != '' and self.estoque_min != '' and self.estoque_max != '':
                
                
                try:

                    float(self.estoque)
                    float(self.estoque_min)
                    float(self.estoque_max)
                    float(self.preco)

                    if self.estoque.isnumeric() and self.estoque_min.isnumeric() and self.estoque_max.isnumeric() and self.preco.isnumeric():
                        cursor = self.connection.cursor()
                        #Cria uma tabela de teste
                        cursor.execute("INSERT INTO produtos"
                                "(descricao, categoria, preco,localizacao, estoque, estoque_min,estoque_max)"
                                "VALUES('%s', '%s', %s, '%s', %s, %s, %s)" %(self.descricao, self.categoria, float(self.preco), self.localizacao, float(self.estoque), float(self.estoque_min), float(self.estoque_max) )) #
                        #Insere dados na tabela
                        cursor.execute("SELECT * FROM produtos") # Lê os dados
                        print(cursor.fetchall()) # Mostra os dados lidos
                        self.connection.commit()
                        from avisos.avisoCadastrado import Ui_Sobre
                        self.window = QtWidgets.QMainWindow()
                        self.avisoCad = Ui_Sobre()
                        self.avisoCad.setupUi(self.window)
                        self.window.show()

                except ValueError:
                    from avisos.avisoStringToInt import Ui_Sobre
                    self.window = QtWidgets.QMainWindow()
                    self.avisoInt = Ui_Sobre()
                    self.avisoInt.setupUi(self.window)
                    self.window.show()
                
            else:
                from avisos.aviso import Ui_Sobre
                self.window = QtWidgets.QMainWindow()
                self.aviso = Ui_Sobre()
                self.aviso.setupUi(self.window)
                self.window.show()
                

        finally:
            self.connection.close()

        
            self.txt_descricao.setText('') 

            # self.ComboCategoria.setItemText(0)
            
            self.precovenda.setText('') 

            # self.comLocalizacao.clearEditText()

            self.txt_estoque.setText('')

            self.txt_estoquMin.setText('') 

            self.txty_estoqueMax.setText('')


    def localizaProduto(self):
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
            self.telaproduto.clear()
            
            cursor = self.connection.cursor()

            desc = self.inputparaselecionarproduto.text()

            filtro = '%' + desc + '%'
           
            #Insere dados na tabela
            cursor.execute("SELECT * FROM produtos WHERE upper(descricao) LIKE upper('%s')"  %(filtro) ) # Lê os dados

            #print(cursor.fetchall()) # Mostra os dados lidos
            strjson = json.loads(json.dumps(cursor.fetchall()))
            
            if strjson == []:
                           
                #Insere dados na tabela
                cursor.execute("SELECT * FROM produtos WHERE id = '%s'" %(desc) ) # Lê os dados

                #print(cursor.fetchall()) # Mostra os dados lidos
                strjson = json.loads(json.dumps(cursor.fetchall()))

            count = 0
    
            for chave in strjson:
               
                print(chave["id"], chave["descricao"], chave["categoria"], chave["preco"], chave["localizacao"], chave["estoque"], chave["estoque_min"], chave["estoque_min"])
            
                item_0 = QtWidgets.QTreeWidgetItem(self.telaproduto)
                self.telaproduto.topLevelItem(count).setText(0, _translate("MainWindow", chave["descricao"]))
                self.telaproduto.topLevelItem(count).setText(1, _translate("MainWindow", chave["localizacao"]))
                
                count = count + 1 
                
        finally:
            self.connection.close()

    def show_sobre(self):
        from sobre.sobre import Ui_Sobre
        self.janela = QtWidgets.QMainWindow()
        self.sobre = Ui_Sobre()
        self.sobre.setupUi(self.janela)
        self.janela.show()

    def show_relatorio(self):
        from relatorio.relatorioestoque import Ui_Form
        self.window = QtWidgets.QMainWindow()
        self.relatorio = Ui_Form()
        self.relatorio.setupUi(self.window)
        self.window.show()

    def show_entradasesaidas(self):
        from entradaeSaidasProduto.ESv2 import Ui_Form
        self.window2 = QtWidgets.QMdiSubWindow()
        self.es = Ui_Form()
        self.es.setupUi(self.window2)
        self.window2.show()  

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
