#! /usr/bin/python
# -*- coding: UTF-8 -*-
#------------Módulos---------------------------------#
from pyrastreio import correios
import time
import os
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3
#------------Banco de Dados-------------------------#
conexao = sqlite3.connect('dados.db')
def create_table():
    c = conexao.cursor()
    c.execute("""create table if not exists pacotes_correio (id_pack integer primary key autoincrement, descricao text, cod_encomenda text)""")
    conexao.commit()
    c.close()
create_table()
#-----------fontes-----------------------------------#
fonte = 'Arial 12'
backgroud = '#353535'
titulo = '#F2D64B'
cor_texto_01 = '#F2EEB3'
#-------------App----------------------------------#
janela = Tk()
janela.title("Rastreio de Encomendas - CORREIO")
janela.geometry("900x700")
janela["bg"]=backgroud
#
ct_0 = Frame(janela)
ct_0["pady"]=5
ct_0["padx"]=5
ct_0["bg"]=backgroud
ct_0.pack()
#
ct_menu = Frame(ct_0)
ct_menu["pady"]=5
ct_menu["padx"]=5
ct_menu["bg"]=backgroud
ct_menu.pack()
def cad():
    ct_00_0.forget()
    init()
    def buscar():
        id = en_03.get()
        conexao = sqlite3.connect('dados.db')
        c = conexao.cursor()
        c.execute("SELECT * from pacotes_correio where id_pack = " + id + " ")
        for linha in c:
            id_pack = linha[0]
            descricao = linha[1]
            cod_encomenda = linha[2]
            en_01.delete(0, END)
            en_02.delete(0, END)
            en_01.insert(INSERT, descricao)
            en_02.insert(INSERT, cod_encomenda)
        conexao.commit()
        c.close()


    def adicionar():
        descricao = en_01.get()
        cod_encomenda = en_02.get()
        cod_encomenda = cod_encomenda.upper() #colocar código em maiúsculas.
        cod_encomenda = cod_encomenda.replace(" ","") #remover espaços

        conexao = sqlite3.connect('dados.db')
        c = conexao.cursor()
        c.execute('INSERT INTO pacotes_correio ( descricao, cod_encomenda) VALUES (? ,?)', (descricao.title(), cod_encomenda))
        conexao.commit()
        c.close()
        en_01.delete(0, END)
        en_02.delete(0, END)


    def alterar():
        id = en_03.get()
        descricao = en_01.get()
        cod_encomenda = en_02.get()
        cod_encomenda = cod_encomenda.upper() #colocar código em maiúsculas.
        cod_encomenda = cod_encomenda.replace(" ","") #remover espaços

        conexao = sqlite3.connect('dados.db')
        c = conexao.cursor()
        c.execute("UPDATE pacotes_correio set descricao = '"+descricao.title()+"', cod_encomenda = '"+cod_encomenda+"'where id_pack= " + id+ " ")
        conexao.commit()
        c.close()
        en_01.delete(0, END)
        en_02.delete(0, END)
        en_03.delete(0, END)

    def excluir():
        id= en_03.get()
        c = conexao.cursor()
        c.execute("delete from pacotes_correio where id_pack = " + id+ " ")
        en_01.delete(0, END)
        en_02.delete(0, END)
        en_03.delete(0, END)
        conexao.commit()
        c.close()


    ct_00 = Frame(ct_00_0)
    ct_00["pady"]=5
    ct_00["padx"]=5
    ct_00["bg"]=backgroud
    ct_00.pack()

    ct_01 = Frame(ct_00)
    ct_01["pady"]=5
    ct_01["padx"]=5
    ct_01["bg"]=backgroud
    ct_01.pack()

    ct_01 = Frame(ct_00)
    ct_01["pady"]=5
    ct_01["padx"]=5
    ct_01["bg"]=backgroud
    ct_01.pack()
    #
    lb_01 = Label(ct_01, font=(fonte +' bold'), fg=titulo, bg=backgroud,text='CORREIOS - RASTREIO DE ENCOMENDAS').pack()
    lb_01 = Label(ct_01, font=(fonte), fg=cor_texto_01, bg=backgroud,text='Adicionar encomenda na base de dados').pack()

    ct_02 = Frame(ct_00)
    ct_02["pady"]=5
    ct_02["padx"]=5
    ct_02["bg"]=backgroud
    ct_02.pack()

    ct_02_1 = Frame(ct_02)
    ct_02_1["pady"]=5
    ct_02_1["padx"]=5
    ct_02_1["bg"]=backgroud
    ct_02_1.pack()
    lb_01 = Label(ct_02_1,width=25, font=(fonte), fg=cor_texto_01, bg=backgroud,text='Descrição')
    lb_01.pack(side=LEFT)
    en_01 = Entry(ct_02_1, font=(fonte), fg='black', bg='white',width=30)
    en_01.pack(side=LEFT)

    ct_02_2 = Frame(ct_02)
    ct_02_2["pady"]=5
    ct_02_2["padx"]=5
    ct_02_2["bg"]=backgroud
    ct_02_2.pack()
    lb_02 = Label(ct_02_2,width=25, font=(fonte), fg=cor_texto_01, bg=backgroud,text='Código de Rastreio')
    lb_02.pack(side=LEFT)
    en_02 = Entry(ct_02_2, font=(fonte), fg='black', bg='white',width=30)
    en_02.pack(side=LEFT)

    ct_03 = Frame(ct_00)
    ct_03["pady"]=5
    ct_03["padx"]=5
    ct_03["bg"]=backgroud
    ct_03.pack()
    lb_03= Label(ct_03,width=15, font=(fonte), fg=cor_texto_01, bg=backgroud,text='Id')
    lb_03.pack(side=LEFT)
    en_03 = Entry(ct_03, font=(fonte), fg='black', bg='white',width=15)
    en_03.pack(side=LEFT)
    bt_03= Button(ct_03,width=15, font=(fonte), fg=cor_texto_01, bg=backgroud,text='Buscar', command=buscar)
    bt_03.pack(side=LEFT)

    ct_03 = Frame(ct_00)
    ct_03["pady"]=5
    ct_03["padx"]=5
    ct_03["bg"]=backgroud
    ct_03.pack()
    bt_04= Button(ct_03,width=15, font=(fonte), fg=cor_texto_01, bg=backgroud,text='Adicionar', command=adicionar)
    bt_04.pack(side=LEFT)
    bt_05= Button(ct_03,width=15, font=(fonte), fg=cor_texto_01, bg=backgroud,text='Alterar', command=alterar)
    bt_05.pack(side=LEFT)
    bt_06= Button(ct_03,width=15, font=(fonte), fg=cor_texto_01, bg=backgroud,text='Excluir', command=excluir)
    bt_06.pack(side=LEFT)
def consultar():
    ct_00_0.forget()
    init()
    #
    ct_00 = Frame(ct_00_0)
    ct_00["pady"]=5
    ct_00["padx"]=5
    ct_00["bg"]=backgroud
    ct_00.pack()
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
    ct_04 = Frame(ct_00)
    ct_04["pady"]=5
    ct_04["padx"]=5
    ct_04["bg"]=backgroud
    ct_04.pack()
    def pacotes_cadastrados():
        global ct_04a
        ct_04a = Frame(ct_04)
        ct_04a["pady"]=5
        ct_04a["padx"]=5
        ct_04a["bg"]=backgroud
        ct_04a.pack()

    pacotes_cadastrados()
    def listar_pacotes_cadastrados():
        ct_04a.forget()
        pacotes_cadastrados()
        global pac
        column_names = ('Id','Código de Rastreio','Descrição')
        # Cria barra de rolagem
        scrollbar = Scrollbar(ct_04a )
        scrollbar.pack(side='right', fill=Y)
        #cria planilha
        cad = ttk.Treeview(ct_04a ,height="2", columns=column_names, yscrollcommand=scrollbar.set,selectmode = "extended")
        cad.column("#0",minwidth=0,width=0)

        #tamanho da coluna
        cad.column('Id', width=100)
        cad.column('Código de Rastreio', width=500)
        cad.column('Descrição', width=220)
        for col in column_names:
            cad.heading(col, text=col)
        scrollbar.config(command=cad.yview)
        def listarpacotes( *args, **kwarks):
            fonec = '%' #fonec.get() + '%'
            conexao = sqlite3.connect('dados.db')
            c = conexao.cursor()
            c.execute("SELECT * FROM pacotes_correio WHERE id_pack LIKE ?",(fonec,))
            consulta = c.fetchall()
            for x in consulta:
                 id = x[0]
                 descricao = x[1]
                 cod_encomenda = x[2]
                 cad.insert('', 'end', text=x, values=(id,cod_encomenda, descricao))
        cad.pack(padx=20, pady=10)
        listarpacotes()
        # Evento duplo clique do treeview
        def duplo_clique(*args):
            item = cad.selection()[0]
            texto = cad.item(item, 'text')
            tamanho=len(texto)
            fat = (tamanho - 13)
            codigo_fin = texto[fat:tamanho]

            en_02.delete(0, END)
            en_02.insert(INSERT, codigo_fin)
            cod_rast()
        # Cria evento duplo clique
        cad.bind("<Double-Button-1>", duplo_clique)
    listar_pacotes_cadastrados()

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
def sair():
    janela.quit()
bt_01 = Button(ct_menu,font=(fonte +' bold'), fg=titulo, bg=backgroud,text='CADASTRAR', command = cad)
bt_01.pack(side=LEFT)
bt_02 = Button(ct_menu,font=(fonte +' bold'), fg=titulo, bg=backgroud,text='CONSULTAR', command = consultar)
bt_02.pack(side=LEFT)
bt_03 = Button(ct_menu,font=(fonte +' bold'), fg=titulo, bg=backgroud,text='SAIR', command = sair)
bt_03.pack(side=LEFT)
def init():
    global ct_00_0
    ct_00_0 = Frame(ct_0)
    ct_00_0["pady"]=5
    ct_00_0["padx"]=5
    ct_00_0["bg"]=backgroud
    ct_00_0.pack()
init()
consultar()
mainloop()
