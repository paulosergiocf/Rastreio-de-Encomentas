#! /usr/bin/python
# -*- coding: UTF-8 -*-
#------------Módulos---------------------------------#
from pyrastreio import correios
import time
import os
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
#-----------fontes-----------------------------------#
fonte = 'Arial 12'
backgroud = '#353535'
titulo = '#F2D64B'
cor_texto_01 = '#F2EEB3'
#-------------App----------------------------------#
janela = Tk()
janela.title("Rastreio de Encomendas - CORREIO")
janela.geometry("900x500")
#
ct_00 = Frame(janela)
ct_00["pady"]=5
ct_00["padx"]=5
ct_00["bg"]=backgroud
ct_00.pack()
#
ct_01 = Frame(ct_00)
ct_01["pady"]=5
ct_01["padx"]=5
ct_01["bg"]=backgroud
ct_01.pack()
#
lb_01 = Label(ct_01, font=(fonte +' bold'), fg=titulo, bg=backgroud,text='CORREIOS - RASTREIO DE ENCOMENDAS').pack()
#
def cod_rast():
    listar_rastreio()#apagar e recriar planilha
    cod_rastreio = en_02.get()#capturar dados de entrada
    cod_rastreio = cod_rastreio.upper() #colocar código em maiúsculas.
    cod_rastreio = cod_rastreio.replace(" ","") #remover espaços
    resultado = (correios(cod_rastreio))#capturar dados sobre a encomenda.
    if resultado == []:# testa do código de Rastreio
        messagebox.showerror("ERRO", "Código de Rastreio Invalido!")
    else:
        for i in resultado:
            #captura dados do dicionário para variável
            data = i["data"]
            hora = i["hora"]
            local = i["local"]
            mensagem = i["mensagem"]
            if len(mensagem)> 75: #verifica número de letras e se a mensagem for muito comprida quebra linha.
                mensagem01 = mensagem[0:75]
                mensagem02 = mensagem[75:]
                mensagem03 = (mensagem01 + '\n' +mensagem02)
                pac.insert('', 'end', values=(data,hora,local,mensagem03))
            else:
                pac.insert('', 'end', values=(data,hora,local,mensagem))
#
ct_02 = Frame(ct_00)
ct_02["pady"]=5
ct_02["padx"]=5
ct_02["bg"]=backgroud
ct_02.pack()
#
lb_02 = Label(ct_02, font=fonte, fg=cor_texto_01, bg=backgroud,text='CÓDIGO DE RESTREIO').pack(side=LEFT)
global en_02
en_02 = Entry(ct_02, )
en_02.pack(side=LEFT)
bt_02 = Button(ct_02, font=fonte, fg=cor_texto_01, bg=backgroud,text='PESQUISAR', command=cod_rast).pack(side=LEFT)
#
ct_03 = Frame(ct_00)
ct_03["pady"]=5
ct_03["padx"]=5
ct_03["bg"]=backgroud
ct_03.pack()
def cont_3a():#cria container para planilha.
    global ct_03a
    ct_03a = Frame(ct_00)
    ct_03a["pady"]=5
    ct_03a["padx"]=5
    ct_03a["bg"]=backgroud
    ct_03a.pack()
cont_3a()
def listar_rastreio():
    ct_03a.forget()
    cont_3a()
    global pac
    column_names = ('data', 'hora','local','mensagem')
    # Cria barra de rolagem
    scrollbar = Scrollbar(ct_03a)
    scrollbar.pack(side='right', fill=Y)
    #cria planilha
    pac = ttk.Treeview(ct_03a,height="12", columns=column_names, yscrollcommand=scrollbar.set,selectmode = "extended")
    pac.column("#0",minwidth=0,width=0)
    #tamanho da coluna
    pac.column('data', width=70)
    pac.column('hora', width=50)
    pac.column('local', width=100)
    pac.column('mensagem', width=700)
    for col in column_names:
        pac.heading(col, text=col)
    scrollbar.config(command=pac.yview)
    # Cria cabeçario do treeview
    style = ttk.Style(ct_03a)
    style.theme_use('clam')
    style.configure("Treeview", rowheight=45)
    pac.pack(padx=20, pady=10)
listar_rastreio()
mainloop()
