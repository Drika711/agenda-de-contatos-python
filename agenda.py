import tkinter as tk
from tkinter import messagebox
def salvar():
    nome = entrada_nome.get()
    telefone = entrada_telefone.get()
    email = entrada_email.get()

    if nome == "":
        messagebox.showwarning("Aviso", "Digite o nome")
        return
    print(nome, telefone, email)
    messagebox.showinfo("Sucesso", "Contato salvo com sucesso!")
    entrada_nome.delete(0, tk.END)
    entrada_telefone.delete(0, tk.END)
    entrada_email.delete(0, tk.END)

janela = tk.Tk()
janela.title("Agenda de Contatos")
janela.geometry("400x300")

tk.Label(janela, text="telefone").pack()
entrada_nome = tk.Entry(janela, width=40)
entrada_nome.pack()

tk.Label(janela, text="telefone").pack()
entrada_telefone = tk.Entry(janela, width=40)
entrada_telefone.pack()

tk.Label(janela, text="email").pack()
entrada_email = tk.Entry(janela, width=40)
entrada_email.pack()
 
tk.Button(janela, text="Salvar", command=salvar).pack(pady=10)

janela.mainloop()

import json
import os
ARQUIVO = "contatos.json"


def carregar_contatos():
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    return []

def salvar_contatos(contatos):
    with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
        json.dump(contatos, arquivo, indent=4, ensure_ascii=False)


contatos = carregar_contatos()

while True:
    print("\n=== Agenda ===")
    print("1 - Adicionar")
    print("2 - Listar")
    print("3 - Buscar")
    print("4 - Editar")
    print("5 - Excluir")
    print("0 - Sair")

    opcao = input("Escolha:")
    
    if opcao == "1":
        nome = input("Nome: ")
        telefone = input("Telefone: ")
        email = input("Email: ")
        contatos.append({
            "nome": nome,
            "telefone": telefone,
            "email": email
        })
        salvar_contatos(contatos)
        print("contato salvo!")

    elif opcao == "2":
        if not contatos:
            print("Nenhum contato cadastrado.")
        else:
            for i, contato in enumerate(contatos, start=1):
                print(f"{i}. {contato['nome']}")
                print(f"nome: {contato['nome']}")
                print(f"Telefone: {contato['telefone']}")
                print(f"Email: {contato['email']}")

    elif opcao == "3":
        nome = input("Digite o nome: ").lower()
        encontrados = [c for c in contatos if nome in c["nome"].lower()]
        if encontrados:
            for contato in encontrados:
                print(contato)
        else:
            print("Nenhum contato encontrado.")

    elif opcao == "4":
        nome = input("Nome do contato")
        for contato in contatos:
            if contato['nome'].lower() == nome.lower():
                contato['telefone'] = input("Novo telefone: ")
                contato['email'] = input("Novo email: ")
                salvar_contatos(contatos)
                print("Contato atualizado.")
                encontrado = True
                break
        else:
            print("Contato não encontrado.")

    elif opcao == "5":
        nome = input("Nome do contato")
        for contato in contatos:
            if contato['nome'].lower() == nome.lower():
                contatos.remove(contato)
                salvar_contatos(contatos)
                print("Contato excluído.")
                break
        else:
            print("Contato não encontrado.")

    elif opcao == "0":
        print("Até logo!")
        break

    else:
        print("Opção inválida!")


                     



           
