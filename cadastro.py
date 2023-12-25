import mysql.connector
import tkinter as tk 
from tkinter import ttk
import datetime as dt 

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='12345',
    database='cadastro')

cursor = conexao.cursor()




lista_tipos = ['Galão', 'Caixa', 'Unidade', 'Saco']
lista_produtos = []

#Criação da função
def inserir_produto():
    descricao = texto_descricao.get()
    tipo = selecionar_tipo.get()
    quantidade = int(texto_quantidade.get())
    criacao = dt.datetime.now()
    criacao = criacao.strftime('%d/%m/%Y %H:%M')
    produto = len(lista_produtos)+1
    produto_str = "COD-{}".format(produto)
    lista_produtos.append((produto_str, descricao, tipo, quantidade, criacao))
    comando = f'INSERT INTO cadastro_prod(nome_produto, tipo_produto, quantidade) VALUES("{descricao}", "{tipo}", "{quantidade}")'
    cursor.execute(comando)
    conexao.commit()
#Janela e Elementos dela.
janela = tk.Tk()
janela.title('Cadastro de materiais')

texto1 = tk.Label(janela, text='Descrição do material')
texto1.grid(column= 0, row= 1, padx= 15, pady= 15, sticky= 'nswe', columnspan= 4)

texto_descricao = tk.Entry()
texto_descricao.grid(column= 0, row= 2, padx= 10, pady= 10, sticky= 'nswe', columnspan= 4)

tipo_unidade = tk.Label(text='Tipo de unidade do produto:')
tipo_unidade.grid(column= 0, row= 3, padx= 30, pady= 15, sticky= 'nswe', columnspan=2)

selecionar_tipo = ttk.Combobox(values= lista_tipos)
selecionar_tipo.grid(column= 2, row= 3, padx=30, pady=10,sticky= 'nswe', columnspan= 2)

quant_tipo = tk.Label(text="Quantidade da Unidade:")
quant_tipo.grid(column=0, row=4, padx= 10, pady= 10, sticky= 'nswe', columnspan=2)

texto_quantidade = tk.Entry()
texto_quantidade.grid(column= 2, row=4, padx=10, pady=10, sticky='nswe', columnspan= 2)

botao_criar_cod = tk.Button(text="Adicionar", command= inserir_produto)
botao_criar_cod.grid(column=1, row= 5, padx=10, pady=10, sticky='nswe', columnspan=2)
janela.mainloop()

print(lista_produtos)

cursor.close()
conexao.close()