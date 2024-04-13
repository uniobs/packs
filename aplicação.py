import tkinter as tk
from tkinter import filedialog, messagebox
import csv
import os
import shutil

# Função para lidar com o clique do botão "Salvar"
def salvar_item():
    nome = entry_nome.get()
    link = entry_link.get()
    preco = entry_preco.get()
    conteudo = entry_conteudo.get()
    imagem_path = entry_imagem.get()

    if not (nome and link and preco and conteudo and imagem_path):
        messagebox.showerror('Erro', 'Por favor, preencha todos os campos.')
        return

    # Copia a imagem para a pasta de imagens
    imagem_nome = nome.lower().replace(' ', '-') + '.png'
    destino_imagem = os.path.join('imagens', imagem_nome)
    shutil.copyfile(imagem_path, destino_imagem)

    # Salva os dados no arquivo CSV
    with open('dados.csv', 'a', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow([nome, link, preco, conteudo, imagem_nome])

    messagebox.showinfo('Sucesso', 'Item salvo com sucesso!')

# Função para selecionar a imagem
def selecionar_imagem():
    imagem_path = filedialog.askopenfilename(filetypes=[('Imagens', '*.png;*.jpg;*.jpeg')])
    if imagem_path:
        entry_imagem.delete(0, tk.END)
        entry_imagem.insert(0, imagem_path)

# Criar a janela principal
root = tk.Tk()
root.title('Cadastro de Item')

# Criar e posicionar os widgets na janela
tk.Label(root, text='Nome:').pack()
entry_nome = tk.Entry(root)
entry_nome.pack()

tk.Label(root, text='Link:').pack()
entry_link = tk.Entry(root)
entry_link.pack()

tk.Label(root, text='Preço:').pack()
entry_preco = tk.Entry(root)
entry_preco.pack()

tk.Label(root, text='Conteúdo:').pack()
entry_conteudo = tk.Entry(root)
entry_conteudo.pack()

tk.Label(root, text='Imagem:').pack()
entry_imagem = tk.Entry(root)
entry_imagem.pack()

btn_selecionar = tk.Button(root, text='Selecionar Imagem', command=selecionar_imagem)
btn_selecionar.pack()

btn_salvar = tk.Button(root, text='Salvar', command=salvar_item)
btn_salvar.pack()

# Rodar o loop principal da aplicação
root.mainloop()
