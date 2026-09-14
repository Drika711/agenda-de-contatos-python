import tkinter as tk
from tkinter import messagebox
import json
import os

ARQUIVO = "contatos.json"


def carregar_contatos():
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    return []


def salvar_contato():
    nome = entrada_nome.get().strip()
    telefone = entrada_telefone.get().strip()
    email = entrada_email.get().strip()

    if nome == "":
        messagebox.showwarning("Aviso", "Digite o nome.")
        return

    contatos = carregar_contatos()

    novo_contato = {
        "nome": nome,
        "telefone": telefone,
        "email": email
    }

    contatos.append(novo_contato)

    with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
        json.dump(contatos, arquivo, ensure_ascii=False, indent=4)

    messagebox.showinfo("Sucesso", "Contato salvo com sucesso!")

    entrada_nome.delete(0, tk.END)
    entrada_telefone.delete(0, tk.END)
    entrada_email.delete(0, tk.END)


# Janela principal
janela = tk.Tk()
janela.title("Agenda de Contatos")
janela.geometry("400x300")

# Nome
tk.Label(janela, text="Nome").pack()
entrada_nome = tk.Entry(janela, width=40)
entrada_nome.pack()

# Telefone
tk.Label(janela, text="Telefone").pack()
entrada_telefone = tk.Entry(janela, width=40)
entrada_telefone.pack()

# E-mail
tk.Label(janela, text="E-mail").pack()
entrada_email = tk.Entry(janela, width=40)
entrada_email.pack()

# Botão salvar
tk.Button(
    janela,
    text="Salvar",
    command=salvar_contato
).pack(pady=20)

janela.mainloop()
