import sys
import subprocess
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QMainWindow, QLabel, QApplication, QGridLayout, QWidget, QMessageBox
from PyQt5.QtCore import QSize

class Janela(QMainWindow):
    def __init__(self):
        super(Janela, self).__init__()
        self.setup_main_Window()
        self.initUI()

    #criando um QLabel texto
    def setup_main_Window(self):
        self.x = 640
        self.y = 480
        self.setMinimumSize(QSize(self.x, self.y))
        self.setWindowTitle("Processamento Digital de Imagens")
        self.Wid = QWidget(self)
        self.setCentralWidget(self.Wid)
        self.layout = QGridLayout()
        self.Wid.setLayout(self.layout)

    def initUI(self):
        self.barrademenu = self.menuBar()

        #menus
        self.menuarquivo = self.barrademenu.addMenu("&Arquivo")
        self.menutransfornar = self.barrademenu.addMenu("&Transformação")
        self.menuSobre = self.barrademenu.addMenu("&Sobre")

        #as actions
        self.opcaoabrir = self.menuarquivo.addAction("Abrir")
        self.opcaoabrir.triggered.connect(self.open_file)
        self.opcaoabrir.setShortcut("Ctrl+A")
        #self.opcaoabrir.setCheckable(True)
        #self.opcaoabrir.setChecked(False)
        #self.opcaorecentes = self.menuarquivo.addMenu("Recentes")
        #self.opcaoabrirrecente = self.opcaorecentes.addAction("Abrir recentas")
        #self.menuarquivo.addSeparator()
        self.opcaofechar = self.menuarquivo.addAction("Fechar")
        self.opcaofechar.setShortcut("Ctrl+F")
        self.opcaofechar.triggered.connect(self.close)

        self.opcaosobre = self.menuSobre.addAction("Sobre")
        self.opcaosobre.triggered.connect(self.exibir_mensagem)
        #self.opcaoapagar = self.menuSobre.addAction("Apagar")
        #self.opcaoapagar.triggered.connect(self.apagar)
        #barra status
        #self.barrastatus = self.statusBar()
        #self.barrastatus.showMessage("Jailson ")
        self.opcaotransformar = self.menutransfornar.addAction("Blur")
        self.opcaotransformar.triggered.connect(self.transform_me1)
        #self.opcaotransformar.setShortcut("Ctrl+T")
        self.opcaotransformar = self.menutransfornar.addAction("Contour")
        self.opcaotransformar.triggered.connect(self.transform_me2)
        #self.opcaotransformar.setShortcut("Ctrl+T")
        self.opcaotransformar = self.menutransfornar.addAction("Detail")
        self.opcaotransformar.triggered.connect(self.transform_me3)
        #self.opcaotransformar.setShortcut("Ctrl+T")
        #QLabel texto
        #self.texto = QLabel("Jailson Quirino de Paula")
        #self.texto.adjustSize()
        #self.largura = self.texto.frameGeometry().width()
        #self.altura = self.texto.frameGeometry().height()
        #self.texto.setAlignment(QtCore.Qt.AlignCenter)        
        #self.botao1 = QtWidgets.QPushButton(self)
        #self.botao1.setText("Original")
        #self.botao1.clicked.connect(self.open_file)
        #self.botao2 = QtWidgets.QPushButton(self)
        #self.botao2.setText("Transformar")
        #self.botao2.clicked.connect(self.transform_me)

        #imagens QLabel
        self.imagem1 = QLabel(self)
        self.endereco1 = 'imagens/carro1.png'
        self.pixmap1 = QtGui.QPixmap(self.endereco1)
        self.pixmap1 = self.pixmap1.scaled(250, 250, QtCore.Qt.KeepAspectRatio)
        self.imagem1.setPixmap(self.pixmap1)
        self.imagem1.setAlignment(QtCore.Qt.AlignCenter)

        self.imagem2 = QLabel(self)
        self.endereco2 = 'imagens/carro1.png'
        self.pixmap2 = QtGui.QPixmap(self.endereco2)
        self.pixmap2 = self.pixmap1.scaled(250, 250, QtCore.Qt.KeepAspectRatio)
        self.imagem2.setPixmap(self.pixmap2)
        self.imagem2.setAlignment(QtCore.Qt.AlignCenter)
        #organizando
        #self.layout.addWidget(self.texto, 0, 0, 1, 2)
        #self.layout.addWidget(self.botao1, 2, 0)
        #self.layout.addWidget(self.botao2, 2, 1)
        self.layout.addWidget(self.imagem1, 1, 0)
        self.layout.addWidget(self.imagem2, 1, 1)
        self.layout.setRowStretch(0, 0)
        self.layout.setRowStretch(1, 1)
        self.layout.setRowStretch(2, 0)
    #Metodos do botao
    #def apagar(self):
        #self.barrastatus.clearMessage()
    def exibir_mensagem(self):
        #self.barrastatus.showMessage("Jailson Quirino")
        self.msg = QMessageBox()
        self.msg.setIcon(QMessageBox.Information)
        self.msg.setWindowTitle("ADS 3ºP")
        self.msg.setText("Jailson Quirino de Paula")
        self.msg.setInformativeText("Moro em Ituiutaba MG\n dia 17/05/2021")
        self.msg.setDetailedText(" Blur: Mostra uma imagem borada.\nContour: Mostra o contorno de toda imagem.\nDetail: Mostra os detales da imagem.")
        self.msg.exec_()

    def open_file(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self, caption= 'Abrir Imagens',
                    directory=QtCore.QDir.currentPath(),
                    filter='all files (*.*);; images (*.png; *.jpg;)',
                    initialFilter='images (*.png; *.jpg;)')

        print(fileName)
        if fileName != '':
            self.endereco1 = fileName
            self.pixmap1 = QtGui.QPixmap(self.endereco1)
            self.pixmap1 = self.pixmap1.scaled(250, 250, QtCore.Qt.KeepAspectRatio)
            self.imagem1.setPixmap(self.pixmap1)

    def transform_me1(self):
        self.entrada = self.endereco1
        self.saida = 'imagens/image_nova1.png'
        self.script = '.\Transform_Blur.py'
        self.janela2 = 'python ' + self.script +' \"' + self.entrada + '\" ' + self.saida
        print(self.janela2)
        subprocess.run(self.janela2, shell=True)
        self.endereco2 = self.saida
        self.pixmap2 = QtGui.QPixmap(self.endereco2)
        self.pixmap2 = self.pixmap2.scaled(250, 250, QtCore.Qt.KeepAspectRatio)
        self.imagem2.setPixmap(self.pixmap2)

    def transform_me2(self):
        self.entrada = self.endereco1
        self.saida = 'imagens/image_nova2.png'
        self.script = '.\Transform_Contour.py'
        self.janela2 = 'python ' + self.script +' \"' + self.entrada + '\" ' + self.saida
        print(self.janela2)
        subprocess.run(self.janela2, shell=True)
        self.endereco2 = self.saida
        self.pixmap2 = QtGui.QPixmap(self.endereco2)
        self.pixmap2 = self.pixmap2.scaled(250, 250, QtCore.Qt.KeepAspectRatio)
        self.imagem2.setPixmap(self.pixmap2)

    def transform_me3(self):
        self.entrada = self.endereco1
        self.saida = 'imagens/image_nova3.png'
        self.script = '.\Transform_Detail.py'
        self.janela2 = 'python ' + self.script +' \"' + self.entrada + '\" ' + self.saida
        print(self.janela2)
        subprocess.run(self.janela2, shell=True)
        self.endereco2 = self.saida
        self.pixmap2 = QtGui.QPixmap(self.endereco2)
        self.pixmap2 = self.pixmap2.scaled(250, 250, QtCore.Qt.KeepAspectRatio)
        self.imagem2.setPixmap(self.pixmap2)


app = QApplication(sys.argv)   
win = Janela()
win.show()
sys.exit(app.exec_()) 