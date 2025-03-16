#Importações
import datetime
from tkinter import Tk, ttk
from customtkinter import *
from PIL import Image
import conexao
from conexao import cursor
from tkcalendar import Calendar, DateEntry

#--------------------------------------------
# Funções


def limpar():
    for widget in scrolavel.winfo_children():
        widget.destroy()

def limparCampos(*telas):
    for tela in telas:
        for widget in tela.winfo_children():
            if isinstance(widget, CTkEntry):
                widget.delete(0, 'end')

def mostrar_clientes():
    limpar()
    i = 0

    if searchBarNome.get() == '' and searchBarCorrespondente.get() == '' and searchBarDate.get() == '':
        cursor.execute(f"SELECT * FROM cliente")
        for linha in cursor.fetchall():
            CTkLabel(scrolavel, text=f"{linha[0]}", font=('Arial', 12)).grid(row=i, column=1, padx=29, pady=10)
            CTkLabel(scrolavel, text=f"{linha[1]} {linha[2]}", font=('Arial', 12)).grid(row=i, column=2, padx=40, pady=10)
            CTkLabel(scrolavel, text=f"{linha[3]}", font=('Arial', 12)).grid(row=i, column=4, padx=45, pady=10)
            CTkLabel(scrolavel, text=f"{linha[4]}", font=('Arial', 12)).grid(row=i, column=5, padx=40, pady=10)
            CTkLabel(scrolavel, text=f"{linha[5]}", font=('Arial', 12)).grid(row=i, column=6, padx=29, pady=10)
            i += 1

    if searchBarNome.get() != '':
        cursor.execute(f"SELECT * FROM cliente where nome like '%{searchBarNome.get()}%'")
        for linha in cursor.fetchall():
            CTkLabel(scrolavel, text=f"{linha[0]}", font=('Arial', 12)).grid(row=i, column=1, padx=29, pady=10)
            CTkLabel(scrolavel, text=f"{linha[1]} {linha[2]}", font=('Arial', 12)).grid(row=i, column=2, padx=40, pady=10)
            CTkLabel(scrolavel, text=f"{linha[3]}", font=('Arial', 12)).grid(row=i, column=4, padx=45, pady=10)
            CTkLabel(scrolavel, text=f"{linha[4]}", font=('Arial', 12)).grid(row=i, column=5, padx=40, pady=10)
            CTkLabel(scrolavel, text=f"{linha[5]}", font=('Arial', 12)).grid(row=i, column=6, padx=29, pady=10)
            i += 1
    
    elif searchBarCorrespondente.get() != '':
        cursor.execute(f"SELECT * FROM cliente where correspondente like '%{searchBarCorrespondente.get()}%'")
        for linha in cursor.fetchall():
            CTkLabel(scrolavel, text=f"{linha[0]}", font=('Arial', 12)).grid(row=i, column=1, padx=29, pady=10)
            CTkLabel(scrolavel, text=f"{linha[1]} {linha[2]}", font=('Arial', 12)).grid(row=i, column=2, padx=40, pady=10)
            CTkLabel(scrolavel, text=f"{linha[3]}", font=('Arial', 12)).grid(row=i, column=4, padx=45, pady=10)
            CTkLabel(scrolavel, text=f"{linha[4]}", font=('Arial', 12)).grid(row=i, column=5, padx=40, pady=10)
            CTkLabel(scrolavel, text=f"{linha[5]}", font=('Arial', 12)).grid(row=i, column=6, padx=29, pady=10)
            i += 1

    if searchBarDate.get() != '':
        cursor.execute(f"SELECT * FROM cliente where data like '%{searchBarDate.get()}%'")
        for linha in cursor.fetchall():
            CTkLabel(scrolavel, text=f"{linha[0]}", font=('Arial', 12)).grid(row=i, column=1, padx=29, pady=10)
            CTkLabel(scrolavel, text=f"{linha[1]} {linha[2]}", font=('Arial', 12)).grid(row=i, column=2, padx=40, pady=10)
            CTkLabel(scrolavel, text=f"{linha[3]}", font=('Arial', 12)).grid(row=i, column=4, padx=45, pady=10)
            CTkLabel(scrolavel, text=f"{linha[4]}", font=('Arial', 12)).grid(row=i, column=5, padx=40, pady=10)
            CTkLabel(scrolavel, text=f"{linha[5]}", font=('Arial', 12)).grid(row=i, column=6, padx=29, pady=10)
            i += 1

    
            


def cadastrar_cliente():

    nome = inputNomeAdd.get()
    sobrenome = inputSobrenomeAdd.get()
    correspondente = inputCorrespondenteAdd.get()
    processoTipo = inputProcessoTipoAdd.get()
    data = inputDataAdd.get()

    # data_formatada = "YYYY-MM-DD"
    # data_formatada =[]
    # for i in range(len(data)):
    #     data_formatada.append(data[-i])

    # print(data_formatada)

    if nome == '' or sobrenome == '' or data == '':
        return CTkLabel(adicionar, text='Preencha todos os campos', font=('Arial', 13, 'bold')).place(relx=0.5, rely=0.7, anchor='center')

    cursor.execute(f"INSERT INTO cliente (nome, sobrenome, correspondente, processoTipo, data) VALUES ('{nome}', '{sobrenome}', '{correspondente}', '{processoTipo}', '{data}')")
    conexao.conn.commit()

    inputNomeAdd.delete(0, 'end')
    inputSobrenomeAdd.delete(0, 'end')
    inputDataAdd.delete(0, 'end')

    mostrar_clientes()



def editar_cliente():
    id = inputIdEdt.get()
    nome = inputNomeEdt.get()
    sobrenome = inputSobrenomeEdt.get()
    correspondente = inputCorrespondenteEdt.get()
    processoTipo = inputProcessoTipoEdt.get()
    data = inputDataEdt.get()


    if id == '' or nome == '' or sobrenome == '' or data == '':
        return CTkLabel(editar, text='Preencha todos os campos', font=('Arial', 13, 'bold')).place(relx=0.5, rely=0.8, anchor='center')

    cursor.execute(f"UPDATE cliente SET nome = '{nome}', sobrenome = '{sobrenome}', correspondente = '{correspondente}', processoTipo = '{processoTipo}', data = '{data}' WHERE id = {id}")
    conexao.conn.commit()

    inputIdEdt.delete(0, 'end')
    inputNomeEdt.delete(0, 'end')
    inputSobrenomeEdt.delete(0, 'end')
    inputDataEdt.delete(0, 'end')

    mostrar_clientes()


def confirmar_deletar():
    confirmacao = CTkFrame(deletar, width=400, height=200)
    confirmacao.place(relx=0.5, rely=0.6, anchor='center')
    CTkLabel(confirmacao, text='Deseja realmente deletar?', font=('Arial', 15)).place(relx=0.5, rely=0.1, anchor='center')
    CTkButton(confirmacao, text='Sim', width=100, height=50, command=deletar_cliente).place(relx=0.3, rely=0.4, anchor='center')

    def fechar():
        confirmacao.destroy()
        inputId.delete(0, 'end')
    CTkButton(confirmacao, text='Não', width=100, height=50, command=fechar).place(relx=0.7, rely=0.4, anchor='center')

def deletar_cliente():
    id = inputId.get()

    if id == '':
        return CTkLabel(deletar, text='Preencha todos os campos', font=('Arial', 12)).place(relx=0.5, rely=0.3, anchor='center')

    cursor.execute(f"DELETE FROM cliente WHERE id = {id}")
    conexao.conn.commit()

    inputId.delete(0, 'end')

    

    mostrar_clientes()
#--------------------------------------------
# Configuração da janela

app = CTk()

larguraTela = app.winfo_screenwidth()
alturaTela = app.winfo_screenheight()
altura = 550
largura = 1080

posx = (larguraTela/2) - (largura/2) + 100
posy = (alturaTela/2) - (altura/2)


app.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy))
app.resizable(0,0)
set_appearance_mode("dark")

#--------------------------------------------
# Criação dos campos de cadastro
telas = CTkTabview(app, width=355, height=540)
telas.place(relx=0.01, rely=0)

#--------------------------------------------
# Criação da aba de cadastro
adicionar = telas.add('Adicionar')

labelTituloAdd = CTkLabel(adicionar, text='CADASTRO DE CLIENTES', font=('Arial', 20))
labelTituloAdd.place(relx=0.5, rely=0.05, anchor='center')

inputNomeAdd = CTkEntry(adicionar, placeholder_text='Nome')
inputNomeAdd.place(relx=0.28, rely=0.15, anchor='center')

inputSobrenomeAdd = CTkEntry(adicionar, placeholder_text='Sobrenome')
inputSobrenomeAdd.place(relx=0.72, rely=0.15, anchor='center')

inputCorrespondenteAdd = CTkComboBox(adicionar, values=['Tatiana', 'Ana Flavia', 'Taynara'])
inputCorrespondenteAdd.place(relx=0.28, rely=0.25, anchor='center')

inputProcessoTipoAdd = CTkComboBox(adicionar, values=['Contrato', 'Aditivo'])
inputProcessoTipoAdd.place(relx=0.72, rely=0.25, anchor='center')

inputDataAdd = DateEntry(adicionar, width=12,font="Arial 15" ,background='darkblue', borderwidth=2, year=2025, date_pattern='dd/mm/yyyy')
inputDataAdd.place(relx=0.5, rely=0.35, anchor='center')

btnCadastrar = CTkButton(adicionar, text='Cadastrar', width=200, height=50, command=cadastrar_cliente)
btnCadastrar.place(relx=0.5, rely=0.48, anchor='center')

btnLimpar = CTkButton(adicionar, text='Limpar', width=200, height=50, command=lambda: limparCampos(adicionar))
btnLimpar.place(relx=0.5, rely=0.6, anchor='center')

#--------------------------------------------
# Criação da aba de editar

editar = telas.add('Editar')

labelTituloEdt = CTkLabel(editar, text='EDITAR CLIENTE', font=('Arial', 20))
labelTituloEdt.place(relx=0.5, rely=0.05, anchor='center')

inputIdEdt = CTkEntry(editar, placeholder_text='ID')
inputIdEdt.place(relx=0.5, rely=0.15, anchor='center')

inputNomeEdt = CTkEntry(editar, placeholder_text='Nome')
inputNomeEdt.place(relx=0.28, rely=0.25, anchor='center')

inputSobrenomeEdt = CTkEntry(editar, placeholder_text='Sobrenome')
inputSobrenomeEdt.place(relx=0.72, rely=0.25, anchor='center')

inputCorrespondenteEdt = CTkComboBox(editar, values=['Tatiana', 'Ana Flavia', 'Taynara'])
inputCorrespondenteEdt.place(relx=0.28, rely=0.35, anchor='center')

inputProcessoTipoEdt = CTkComboBox(editar, values=['Contrato', 'Aditivo'])
inputProcessoTipoEdt.place(relx=0.72, rely=0.35, anchor='center')


# inputDataEdt = DateEntry(editar, background="black", disabledbackground="black", bordercolor="black", 
#                headersbackground="black", normalbackground="black", foreground='white', 
#                normalforeground='white', headersforeground='white', font="Arial 15", year=2025)
# inputDataEdt.config(background = "black")
# inputDataEdt.place(relx=0.5, rely=0.45, anchor='center')

inputDataEdt = DateEntry(editar, width=12,font="Arial 15" ,background='darkblue', borderwidth=2, year=2025, date_pattern='dd/mm/yyyy')
inputDataEdt.place(relx=0.5, rely=0.45, anchor='center')

btnEditar = CTkButton(editar, text='Editar', width=200, height=50, command=editar_cliente)
btnEditar.place(relx=0.5, rely=0.58, anchor='center')

btnLimparEdt = CTkButton(editar, text='Limpar', width=200, height=50, command=lambda: limparCampos(editar))
btnLimparEdt.place(relx=0.5, rely=0.7, anchor='center')

#--------------------------------------------
# Criação da aba de deletar


deletar = telas.add('Deletar')

labelTitulo = CTkLabel(deletar, text='DELETAR CLIENTE', font=('Arial', 20))
labelTitulo.place(relx=0.5, rely=0.05, anchor='center')

inputId = CTkEntry(deletar, placeholder_text='ID')
inputId.place(relx=0.5, rely=0.15, anchor='center')

btnDeletar = CTkButton(deletar, text='Deletar', width=200, height=50 , command=confirmar_deletar)
btnDeletar.place(relx=0.5, rely=0.25, anchor='center')


#--------------------------------------------

#Botão de pesquisar cliente e mostrar clientes

searchBarNome = CTkEntry(app, placeholder_text='Nome cliente')
searchBarNome.place(relx=0.45, rely=0.06, anchor='center' )

searchBarCorrespondente = CTkEntry(app, placeholder_text='Correspondente')
searchBarCorrespondente.place(relx=0.6, rely=0.06, anchor='center' )

searchBarDate = CTkEntry(app, placeholder_text='Data')
searchBarDate.place(relx=0.75, rely=0.06, anchor='center')

botao = CTkButton(app, text='Mostrar Clientes', command=mostrar_clientes)
botao.configure(height=27)
botao.place(relx=0.9, rely=0.06, anchor='center')

#--------------------------------------------
# Criação da tabela


header = CTkFrame(app, width=690, height=50)
header.place(relx=0.675, rely=0.16, anchor='center')

id = CTkLabel(header, text='ID', font=('Arial', 12))
id.place(relx=0.0552, rely=0.5, anchor='center')

nome = CTkLabel(header, text='Nome', font=('Arial', 12))
nome.place(relx=0.24, rely=0.5, anchor='center')

correspondente = CTkLabel(header, text='Correspondente', font=('Arial', 12))
correspondente.place(relx=0.485, rely=0.5, anchor='center')

processoTipo = CTkLabel(header, text='Processo', font=('Arial', 12))
processoTipo.place(relx=0.69, rely=0.5, anchor='center')

data = CTkLabel(header, text='Data', font=('Arial', 12))
data.place(relx=0.85, rely=0.5, anchor='center')

#--------------------------------------------  
# Scrollable Frame

scrolavel = CTkScrollableFrame(app, width=665, height=400)
scrolavel.place(relx=0.674, rely=0.6, anchor='center')

























app.mainloop()
#--------------------------------------------
