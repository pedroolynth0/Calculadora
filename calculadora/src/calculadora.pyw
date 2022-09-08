from multiprocessing.resource_sharer import stop
import os
import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMainWindow
import math

valor =[]
valor.append(0)
class teste(QMainWindow):
    
    def __init__(self):
        
        QMainWindow.__init__(self)
        uic.loadUi('integral.ui', self)
        self.calcular.clicked.connect(lambda: calcular())
        self.voltar.clicked.connect(lambda: voltar())
        self.setWindowTitle("Integral")
        self.close.clicked.connect(lambda: voltar())
        self.min.clicked.connect(lambda: min())
        n = 9999

        def min():
            tela2.showMinimized()
        def voltar():
            fechar()
            inicio()
            tela2.hide()
        def calcular():
            pi = math.pi

            resultado=0
            try:
               a = eval(self.a.text())
               b = eval(self.b.text())
               f = self.funcao.text()    
               deltax =h(a,b)                
               for i in range (n)  :
                
                   x1 = float(a) + ((i+1) *deltax)
                   x=x1
                   e=math.e
                   cosx = math.cos(x)
                   senx = math.sin(x)
                   resultado+= eval(f) 

            
                   self.resultado.setText(str(round((resultado*deltax),3)))
            except:
               self.resultado.setText("Error")
               
            

           
           
            
        def h (a,b):
            try:
               h = (b - a)/n
            except:
                h = "Error"   
            return h    
            
        
class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self) 
        uic.loadUi('calculadora3.ui', self)
        valores = []
        
        
        
    
        self.zero.clicked.connect(lambda: labelValue("0"))
        self.um.clicked.connect(lambda: labelValue("1"))
        self.dois.clicked.connect(lambda: labelValue("2"))
        self.tres.clicked.connect(lambda: labelValue("3"))
        self.quatro.clicked.connect(lambda: labelValue("4"))
        self.cinco.clicked.connect(lambda: labelValue("5"))
        self.seis.clicked.connect(lambda: labelValue("6"))
        self.sete.clicked.connect(lambda: labelValue("7"))
        self.oito.clicked.connect(lambda: labelValue("8"))
        self.nove.clicked.connect(lambda: labelValue("9"))
        self.euler.clicked.connect(lambda: temEuler())
        self.pi.clicked.connect(lambda: temPi())
        self.clear.clicked.connect(lambda: labelClear())
        self.ponto.clicked.connect(lambda: temPonto())
        self.mais.clicked.connect(lambda: somar())
        self.menos.clicked.connect(lambda: sub())
        self.igual.clicked.connect(lambda: igual())
        self.multiplicar.clicked.connect(lambda: vezes())
        self.divisao.clicked.connect(lambda: div())
        self.expoente_2.clicked.connect(lambda: elevar())
        self.raiz.clicked.connect(lambda: raiz())
        self.porcentagem.setEnabled(False)
        self.cos.clicked.connect(lambda: cos())
        self.seno.clicked.connect(lambda: sen())
        self.integral.clicked.connect(lambda: integral())
        self.min.clicked.connect(lambda: min())
        self.close.clicked.connect(lambda: close())



        def integral():
            
            
            fechar()
            tela2.show()
        def min():
            main.showMinimized()
        def close():
            main.hide()            
            os.close()
           
        def porcentagem():
            texto = self.outLabel.text()
            try:
                valores.append(float(texto))
                valores.append("%")
                self.outLabel.setText("0")
                self.op.setText("%")
            except:
                self.outLabel.setText("Error")

        def raiz():
            texto = self.outLabel.text()
            resultado = math.sqrt(float(texto))
            self.outLabel.setText(str(resultado))
        def cos():
            texto = self.outLabel.text()
            resultado = math.cos(float(texto))
            self.outLabel.setText(str(resultado))    
        def sen():
            texto = self.outLabel.text()
            resultado = math.sin(float(texto))
            self.outLabel.setText(str(resultado))                    

        def igual():
            resultado = 0
            op = ['+', '-', '*', '/']
            if len(valores) == 0:
                pass
            else:
                valores.append(float(self.outLabel.text()))
                contador = 0
                for i in range(len(valores)):
                    try:
                        if valores[i] == "+":
                            if contador == 0:
                                resultado = eval(
                                    f'{valores[i-1]} {op[0]} {valores[i+1]}')
                                contador = contador+1
                            else:
                                resultado = resultado + valores[i+1]
                        elif valores[i] == "-":
                            if contador == 0:
                                resultado = eval(
                                    f'{valores[i-1]} {op[1]} {valores[i+1]}')
                                contador = contador+1
                            else:
                                resultado = resultado - valores[i+1]
                        elif valores[i] == "*":
                            if contador == 0:
                                resultado = eval(
                                    f'{valores[i-1]} {op[2]} {valores[i+1]}')
                                contador = contador+1
                            else:
                                resultado = resultado * valores[i+1]
                        elif valores[i] == "/":
                            if contador == 0:
                                resultado = eval(
                                    f'{valores[i-1]} {op[3]} {valores[i+1]}')
                                contador = contador+1
                            else:
                                resultado = resultado / valores[i+1]
                        elif valores[i] == "**":
                            if contador == 0:
                                resultado = valores[i-1] ** valores[i+1]
                                contador = contador+1
                            else:
                                resultado = resultado ** valores[i+1]
                        elif valores[i] == "%":
                            resultado = "Nao implementado"                                
                    except:
                        resultado = "Error"
                self.outLabel.setText(str(resultado))
                self.op.setText("")
                valores.clear()

        def div():
            texto = self.outLabel.text()
            if texto == "0" or texto == "0.":
                pass
            else:
                try:
                    valores.append(float(texto))
                    valores.append("/")
                    self.outLabel.setText("0")
                    self.op.setText("÷")
                except:
                    self.outLabel.setText("Error")

        def vezes():
            texto = self.outLabel.text()
            if texto == "0" or texto == "0.":
                pass
            else:
                try:
                    valores.append(float(texto))
                    valores.append("*")
                    self.outLabel.setText("0")
                    self.op.setText("×")
                except:
                    self.outLabel.setText("Error")

        def somar():
            texto = self.outLabel.text()
            if texto == "0" or texto == "0.":
                pass
            else:
                try:
                    valores.append(float(texto))
                    valores.append("+")
                    self.outLabel.setText("0")
                    self.op.setText("+")
                except:
                    self.outLabel.setText("Error")

        def elevar():
            texto = self.outLabel.text()

            valores.append(float(texto))
            valores.append("**")
            self.outLabel.setText("0")
            self.op.setText("^")

        def sub():
            texto = self.outLabel.text()
            if texto == "0" or texto == "0.":
                pass
            else:
                valores.append(float(texto))
                valores.append("-")
                self.outLabel.setText("0")
                self.op.setText("-")

        def temPonto():
            texto = self.outLabel.text()
            if "." in texto:
                pass
            else:
                if texto == "0":
                    labelValue("0.")
                else:
                    labelValue(".")

        def temEuler():
            texto = self.outLabel.text()
            if "2.71828182845904" in texto:
                pass
            else:
                self.outLabel.setText("2.71828182845904")
                
                

        def temPi():
            texto = self.outLabel.text()
            if "3.14159265358979" in texto:
                pass
            else:
                labelValue("3.14159265358979")

        def labelValue(n):

            texto = self.outLabel.text()

            if(texto == "0"):
                texto = ""
            self.outLabel.setText(texto + n)
        
        def labelClear():
            self.outLabel.setText("0")
            valores.clear()
            self.op.setText("")


app = QtWidgets.QApplication(sys.argv)
main = MainWindow()
tela2 = teste()
def fechar(): 
    main.hide()
   

    
def inicio():
    main.show()

    
    
inicio()  
sys.exit(app.exec_())
    
   



    
