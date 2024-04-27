from tkinter import *

class Funcoes:
    def tecla_apaga_tudo (self):
        #apagar tudo que estava escrito no visor
        self.visor.delete(0, END)
    def arredonda_resultado (self):
        self.resultado = round (self.resultado, 13)
    def tira_ponto_zero (self):
        self.resultado = self.resultado.replace(".0", "")
    def mostra_resultado (self):
        #colocando o resultado no visor
        self.arredonda_resultado()
        self.tecla_apaga_tudo()
        self.resultado = str(self.resultado)
        if (self.resultado[-2] == "." and self.resultado[-1] == "0"):
            self.tira_ponto_zero()
        self.visor.insert(END, self.resultado)

    #teclas numéricas
    def tecla_1 (self):
        self.visor.insert(END, "1")
    def tecla_2 (self):
        self.visor.insert(END, "2") 
    def tecla_3 (self):
        self.visor.insert(END, "3") 
    def tecla_4 (self):
        self.visor.insert(END, "4") 
    def tecla_5 (self):
        self.visor.insert(END, "5") 
    def tecla_6 (self):
        self.visor.insert(END, "6") 
    def tecla_7 (self):
        self.visor.insert(END, "7") 
    def tecla_8 (self):
        self.visor.insert(END, "8") 
    def tecla_9 (self):
        self.visor.insert(END, "9") 
    def tecla_0 (self):
        self.visor.insert(END, "0")
    def tecla_virgula (self):
        self.visor.insert(END, ".")
    
    #teclas funcionais
    def tecla_soma (self):
        self.visor.insert(END, "+")
    def tecla_subtração (self):
        self.visor.insert(END, "-")
    def tecla_multiplicação (self):
        self.visor.insert(END, "*")
    def tecla_divisão (self):
        self.visor.insert(END, "/")
    def tecla_potenciação (self):
        self.visor.insert(END, "^")
    def tecla_raiz (self):
        self.numero = self.visor.get()
        
        #calcula raiz quadrada
        self.resultado = float(self.numero) ** 0.5
        self.mostra_resultado()
    def tecla_raiz_cubica (self):
        self.numero = self.visor.get()
        
        #calcula raiz cubica
        self.resultado = float(self.numero) ** (1/3)
       
        self.mostra_resultado()
    def tecla_calcula (self):
        self.operacao = self.visor.get()
        n = 0
        contador = [int]*3
        operador = ""
        ind_operador = 0
        numero = [""]*3

        #calcula delta
        if (self.operacao[0] == "a"):
            for i in range(len(self.operacao)):
                if self.operacao[i] == "=":
                    contador[n] = i
                    n += 1
            
            n = 0

            for i in range(len(self.operacao)):
                if i > contador[0] and i < contador[1] - 3:
                    numero[0] = numero[0] + self.operacao[i] 
                elif i > contador[1] and i < contador[2] - 3:
                    numero[1] = numero[1] + self.operacao[i] 
                elif i > contador[2]:
                    numero[2] = numero[2] + self.operacao[i]
            
            for i in range(len(numero)):
                numero[i] = int(numero[i])
            
            self.resultado = float (numero[1] ** 2 - 4 * numero[0] * numero[2])

            self.mostra_resultado()
        else:           
            #Descobrir que tipo de operação matematica está sendo feita e em que posicao o operador está
            for i in range(len(self.operacao)):
                if self.operacao[i] == "+" or self.operacao[i] == "-" or self.operacao[i] == "*" or self.operacao[i] == "/" or self.operacao[i] == "^":
                    operador = self.operacao[i]
                    ind_operador = i
            
            #Separar os dois termos da operacao
            termo = [""]*2

            for i in range(len(self.operacao)):
                if i < ind_operador:
                    termo[0] += self.operacao[i]
                elif i > ind_operador:
                    termo[1] += self.operacao[i]
                
            self.tecla_apaga_tudo()
            
            #Realizando a operacao
            if operador == "+":
                self.resultado = float(termo[0]) + float(termo[1])
            if operador == "-":
                self.resultado = float(termo[0]) - float(termo[1])
            if operador == "*":
                self.resultado = float(termo[0]) * float(termo[1])
            if operador == "/":
                self.resultado = float(termo[0]) / float(termo[1])
            if operador == "^":
                self.resultado = float(termo[0]) ** float(termo[1])
            
            self.mostra_resultado()
    def tecla_porcentagem (self):
        numero = self.visor.get()
        
        #transforma numero para um float
        numero = float(numero)

        self.tecla_apaga_tudo()

        self.visor.insert(END, str(numero/100))
    def tecla_delta (self):
        self.visor.insert(END, 'a=, b=, c=')
    def tecla_apaga_unidade (self):
        text = self.visor.get()

        self.tecla_apaga_tudo()
        
        #coloca no visor o mesmo texto sem o ultimo caracter
        text = text[0:len(text) - 1]
        self.visor.insert(END, text)
    
                

    
