import sys

import PyQt5
#Importando as bibliotecas de crianção
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout
#Importando as bibliotecas de designer
from PyQt5.QtWidgets import QPushButton, QLineEdit,  QSizePolicy

#Criar uma classe
class Calculadora(QMainWindow):
    def __init__(self, parent = None):
        super().__init__(parent)

        #Mudando o nome do titulo da janela instanciada
        self.setWindowTitle('Calculadora')

        #Travando para que não seja possivel redimensionar a janela
        self.setFixedSize(400, 400)

        self.cw = QWidget()

        #Criando uma grade da pagina
        self.grid = QGridLayout(self.cw)

        #Criando o display da calculadora
        self.display = QLineEdit()

        #Adicionando o display a grid
        self.grid.addWidget(self.display, 0, 0, 1, 5)

        #Impendindo que seja inputado coisas no display via teclado
        self.display.setDisabled(True)

        #Alterando o visual do display
        self.display.setStyleSheet(
            '* {background: white; color: #000; font-size: 30px; }')
        self.display.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)

        #Adicionando os botões

        #Linha 1
        self.add_btn(QPushButton('7'), 1, 0, 1, 1)
        self.add_btn(QPushButton('8'), 1, 1, 1, 1)
        self.add_btn(QPushButton('9'), 1, 2, 1, 1)
        self.add_btn(QPushButton('+'), 1, 3, 1, 1)
        self.add_btn(

            #Adcionando funcionalidade a esse botão
            QPushButton('C'), 1, 4, 1, 1,
            lambda: self.display.setText(''),
                'background: #d5580d; color: #fff; font-weigth: 700'

        )

        #Linha 2
        self.add_btn(QPushButton('4'), 2, 0, 1, 1)
        self.add_btn(QPushButton('5'), 2, 1, 1, 1)
        self.add_btn(QPushButton('6'), 2, 2, 1, 1)
        self.add_btn(QPushButton('-'), 2, 3, 1, 1)
        self.add_btn(

            #Adcionando funcionalidade a esse botão
            QPushButton('<-'), 2, 4, 1, 1,
            lambda: self.display.setText(
                self.display.text() [:-1]),
            'background:#13823a; color: #fff; font-weigth: 700;'
        )

        #Linha 3
        self.add_btn(QPushButton('1'), 3, 0, 1, 1)
        self.add_btn(QPushButton('2'), 3, 1, 1, 1)
        self.add_btn(QPushButton('3'), 3, 2, 1, 1)
        self.add_btn(QPushButton('/'), 3, 3, 1, 1)
        self.add_btn(QPushButton(''), 3, 4, 1, 1)

        #Linha 4
        self.add_btn(QPushButton('.'), 4, 0, 1, 1)
        self.add_btn(QPushButton('0'), 4, 1, 1, 1)
        self.add_btn(QPushButton(''), 4, 2, 1, 1)
        self.add_btn(QPushButton('*'), 4, 3, 1, 1)
        self.add_btn(

            #Adcionando uma funcionalidade a este botão
            QPushButton('='), 4, 4, 1, 1,
            self.eval_igual,
            'background:#095177 ; color: #fff; font-weigth: 700;'
        )



        #Configurando o objeto central como o cw
        self.setCentralWidget(self.cw)


    #Criando um metodo para criar os botões

    def add_btn(self, btn, row, col, rowspan, colspan, funcao = None, style = None):
        self.grid.addWidget(btn, row, col, rowspan, colspan)
        if not funcao:
            btn.clicked.connect(
                lambda: self.display.setText(
                    self.display.text() + btn.text()

                )
            )
        else:
            btn.clicked.connect(funcao)

        #Verificando se existe um estilo e caso não tenha empregando um
        if style:
            btn.setStyleSheet(style)

        #Configurando para que o display se ajuste ao tamanho da pagina
        btn.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)

    def eval_igual(self):
        try:
            self.display.setText(
                #Avaliando se a conta e valida
                str(eval(self.display.text()))
            )
        except Exception as e:
            self.display.setText('Conta Invalida')

if __name__ == '__main__':
    qt = QApplication(sys.argv)
    calc = Calculadora()
    calc.show()
    qt.exec_()