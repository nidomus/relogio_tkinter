from distutils import core
from tkinter import *
import math as m
import time as t

root = Tk()
root.resizable(0,0)
root.eval('tk::PlaceWindow . center')
root.title('Relógio')

segundo=0
res = 300

root.geometry(str(res+50)+'x'+str(res+50))
root.configure(bg='white')

def rotacao(x,y):
    coord_n = []
    rad = m.radians(6)#Pega a rotação equivalente a um segundo e converte em radiano

    #Multiplicação da Matriz de Rotação pela Matriz das coordenadas do Ponteiro
    x_novo = m.cos(rad)*x + m.sin(rad)*y
    y_novo = -1*m.sin(rad)*x + m.cos(rad)*y

    
    coord_n.append(x_novo)
    coord_n.append(y_novo)
    return coord_n


window = Frame(root,bg='white')

window.pack(padx = res/16,pady=res/16)
graph = Canvas(window,height= res, width = res, bd=0, bg='white')
#graph.create_line(res/2,res/2,res/2,10,fill='red')
#graph.create_line(res/2,res/2,res-10,res/2, fill='red')

#inicializa os ponteiros
pont_segundos = graph.create_line(res/2,res/2,res/2,20,arrow = 'last', fill='red',width =2)
pont_minutos = graph.create_line(res/2,res/2,res/2,20,arrow = 'last',fill='black',width =3)
pont_horas = graph.create_line(res/2,res/2,res/2,80,arrow = 'last',fill='black',width =4)

#cria o ponto no centro do eixo
graph.create_oval(res/2-3,res/2-3,res/2+3,res/2+3, fill = 'black')
graph.create_oval(2,2,res-2,res-2, width = 2)

#
graph.create_text(res/2,12,text='12', font=(None,13),fill='blue')
graph.create_text(res-12,res/2,text='3', font=(None,13),fill='blue')
graph.create_text(res/2,res-12,text='6', font=(None,13),fill='blue')
graph.create_text(12,res/2,text='9', font=(None,13),fill='blue')

coord_pontos = [0,res/2-10]

cont = 0
while cont<=60:
    x = res/2+coord_pontos[0]
    y = res/2-coord_pontos[1]
    if cont%5!=0:
        graph.create_oval(x,y,x,y,width=3,fill='black')
    elif cont %15!=0:
        graph.create_text(x,y,text=cont//5, font=(None,10))


    coord_pontos = rotacao(coord_pontos[0],coord_pontos[1]).copy()    
    cont+=1


graph.pack()

horario = t.localtime()
horario_segundos = horario.tm_hour*3600 + horario.tm_min*60 + horario.tm_sec

# O segundo elemento das coordenadas abaixo define o comprimento do ponteiro
coord_s = [0,res/2-20]# coordenada inicial do ponteiro dos segundos
coord_m = [0,res/2-20] # coordenada inicial do ponteiro dos minutos
coord_h =  [0,res/2-80] # coordenada inicial do ponteiro das horas

print(horario_segundos)
for s in range(horario_segundos):
    coord_s = rotacao(coord_s[0],coord_s[1]).copy()

    
    if s % 60 == 0 and s!=0:
        coord_m = rotacao(coord_m[0],coord_m[1]).copy()        
    
    if s % 720 == 0 and s!=0:
        coord_h = rotacao(coord_h[0],coord_h[1]).copy()   

graph.coords(pont_horas,res/2,res/2,res/2+coord_h[0],res/2-coord_h[1])
graph.coords(pont_minutos,res/2,res/2,res/2+coord_m[0],res/2-coord_m[1])
graph.coords(pont_segundos,res/2,res/2,res/2+coord_s[0],res/2-coord_s[1])
graph.update()

stop = False
while stop == False:
    
    coord_s = rotacao(coord_s[0],coord_s[1]).copy()# executa a rotação, retornando as novas coordenadas
    
    x_real = res/2 + coord_s[0] # desloca para o centro da tela 
    y_real = res/2 - coord_s[1] # desloca para o centro da tela 
    
    graph.coords(pont_segundos,res/2,res/2,x_real,y_real) # atualiza a coordenada real da linha

    t.sleep(1) # delay de 1 segundo

    if horario_segundos %60 == 0 and horario_segundos!=0:
        coord_m = rotacao(coord_m[0],coord_m[1]).copy()# executa a rotação, retornando as novas coordenadas
        graph.coords(pont_minutos,res/2,res/2,res/2+coord_m[0],res/2-coord_m[1]) # atualiza a coordenada real da linha   

    if horario_segundos %720 == 0 and horario_segundos!=0:
        coord_h = rotacao(coord_h[0],coord_h[1]).copy()# executa a rotação, retornando as novas coordenadas
        graph.coords(pont_horas,res/2,res/2,res/2+coord_h[0],res/2-coord_h[1]) # atualiza a coordenada real da linha       
    
    horario_segundos+=1 # adiciona mais um no contador de segundos
    graph.update() # atualiza a tela com a nova linha


root.mainloop()












