from tkinter import *
from tkinter import ttk
from Funcoes import *

class Calculadora(Funcoes):
    def __init__ (self):
        self.janela = Tk()
        self.tela()
        self.criaVisor()
        self.botões()
        #self.funcoes()
        self.janela.mainloop()
    
    def tela (self):
        self.janela.title("Calculadora")
        self.janela.configure (background= "White")
        self.janela.geometry("375x500")

        canvas = Canvas(self.janela, width= 375, height= 500)
        canvas.pack()

        # Cores para o degradê
        color_start = (79, 79, 79)
        color_end = (220, 220, 220)

        # Cria um retângulo com degradê de cores
        self.background_degradê(canvas, 0, 0, 375, 500, color_start, color_end)



    def background_degradê(self, canvas, x1, y1, x2, y2, color1, color2):
        # Cria um gradiente de cores horizontal em um retângulo no canvas.
        for i in range(x1, x2 + 1):
            r = int((color1[0] * (x2 - i) + color2[0] * (i - x1)) / (x2 - x1))
            g = int((color1[1] * (x2 - i) + color2[1] * (i - x1)) / (x2 - x1))
            b = int((color1[2] * (x2 - i) + color2[2] * (i - x1)) / (x2 - x1))
            color = f'#{r:02X}{g:02X}{b:02X}'  # Converte para formato hexadecimal
            canvas.create_line(i, y1, i, y2, fill=color)   

    def criaVisor (self):
        #visor
        self.visor = Entry(self.janela, font= ("Verdana", 26), borderwidth= 3)
        self.visor.place(relx= 0.05, rely= 0.05, relwidth= 0.9, relheight= 0.12)

    def botões (self):

        #teclas numéricas
        self.um = Button (self.janela, text= "1", font= ("Verdana", 26), command= self.tecla_1).place(relx=0.05, rely= 0.39, relwidth= 0.16, relheight= 0.10)
        self.dois = Button (self.janela, text= "2", font= ("Verdana", 26), command= self.tecla_2).place(relx=0.235, rely= 0.39, relwidth= 0.16, relheight= 0.10)
        self.tres = Button (self.janela, text= "3", font= ("Verdana", 26), command= self.tecla_3).place(relx=0.42, rely= 0.39, relwidth= 0.16, relheight= 0.10)
        self.quatro = Button (self.janela, text= "4", font= ("Verdana", 26), command= self.tecla_4).place(relx=0.05, rely= 0.53, relwidth= 0.16, relheight= 0.10)
        self.cinco = Button (self.janela, text= "5", font= ("Verdana", 26), command= self.tecla_5).place(relx=0.235, rely= 0.53, relwidth= 0.16, relheight= 0.10)
        self.seis = Button (self.janela, text= "6", font= ("Verdana", 26), command= self.tecla_6).place(relx=0.42, rely= 0.53, relwidth= 0.16, relheight= 0.10)
        self.sete = Button (self.janela, text= "7", font= ("Verdana", 26), command= self.tecla_7).place(relx=0.05, rely= 0.67, relwidth= 0.16, relheight= 0.10)
        self.oito = Button (self.janela, text= "8", font= ("Verdana", 26), command= self.tecla_8).place(relx=0.235, rely= 0.67, relwidth= 0.16, relheight= 0.10)
        self.nove = Button (self.janela, text= "9", font= ("Verdana", 26), command= self.tecla_9).place(relx=0.42, rely= 0.67, relwidth= 0.16, relheight= 0.10)
        self.zero = Button (self.janela, text= "0", font= ("Verdana", 26), command= self.tecla_0).place(relx=0.235, rely= 0.81, relwidth= 0.16, relheight= 0.10)
        self.virgula = Button (self.janela, text= ",", font= ("Verdana", 26), command= self.tecla_virgula).place(relx=0.05, rely= 0.81, relwidth= 0.16, relheight= 0.10)
        
        #teclas para apagar
        self.ac = Button (self.janela, text= "AC", font= ("Verdana", 26), command= self.tecla_apaga_unidade).place(relx=0.05, rely= 0.25, relwidth= 0.16, relheight= 0.10)
        self.c = Button (self.janela, text= "C", font= ("Verdana", 26), command= self.tecla_apaga_tudo).place(relx=0.235, rely= 0.25, relwidth= 0.16, relheight= 0.10)

        #teclas de funcoes
        self.soma = Button(self.janela, text = "+", font= ("Verdana", 26), command= self.tecla_soma).place(relx=0.605, rely= 0.81, relwidth= 0.16, relheight= 0.10)
        self.subtração = Button(self.janela, text= "-", font= ("Verdana", 26), command= self.tecla_subtração).place(relx= 0.605, rely= 0.67, relwidth= 0.16, relheight= 0.10)
        self.multiplicação = Button(self.janela, text= "*", font= ("Verdana", 26), command= self.tecla_multiplicação).place(relx= 0.605, rely= 0.53, relwidth= 0.16, relheight= 0.10)
        self.divisão = Button(self.janela, text= "/", font= ("Verdana", 26), command= self.tecla_divisão).place(relx= 0.605, rely= 0.39, relwidth= 0.16, relheight= 0.10)
        self.porcentagem = Button(self.janela, text= "%", font= ("Verdana", 26), command= self.tecla_porcentagem).place(relx= 0.605, rely= 0.25, relwidth= 0.16, relheight= 0.10)
        self.potenciação = Button(self.janela, text= "^", font= ("Verdana", 26), command= self.tecla_potenciação).place(relx= 0.42, rely= 0.25, relwidth= 0.16, relheight= 0.10)
        self.raiz_quadrada = Button(self.janela, text= "√", font= ("Verdana", 26), command= self.tecla_raiz).place(relx= 0.79, rely= 0.39, relwidth= 0.16, relheight= 0.10)
        self.raiz_cubica = Button(self.janela, text= "∛", font= ("Verdana", 26), command= self.tecla_raiz_cubica).place(relx= 0.79, rely= 0.25, relwidth= 0.16, relheight= 0.10)
        self.potenciação_cubica = Button(self.janela, text= "Δ", font= ("Verdana", 26), command= self.tecla_delta).place(relx= 0.79, rely= 0.53, relwidth= 0.16, relheight= 0.10)
        #tecla de calcular
        self.calcula = Button(self.janela, text= "=", font= ("Verdana", 26), command= self.tecla_calcula).place(relx= 0.42, rely= 0.81, relwidth= 0.16, relheight= 0.10)

Calculadora()