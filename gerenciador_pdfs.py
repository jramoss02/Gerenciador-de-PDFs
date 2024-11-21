import os
import tkinter as tk
from tkinter import filedialog, messagebox
from pypdf import PdfReader, PdfWriter

# Classe principal do aplicativo para gerenciar PDFs
class PDFMergerApp:
    def __init__(self, root):
        # Inicializa a janela principal e define o título
        self.root = root
        self.root.title("Gerenciador de PDFs")
        
        # Lista para armazenar os caminhos dos arquivos PDF adicionados
        self.pdf_list = []

        # Criação de um frame para os botões
        button_frame = tk.Frame(root)
        button_frame.pack(fill=tk.X, padx=10, pady=5)

        # Botões com funcionalidades para adicionar, remover e organizar PDFs
        tk.Button(button_frame, text="Adicionar PDFs", command=self.adicionar_pdfs).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Remover Selecionado", command=self.remover_pdf).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Remover Todos", command=self.remover_todos).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Mover Para Cima", command=self.mover_para_cima).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Mover Para Baixo", command=self.mover_para_baixo).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Combinar PDFs", command=self.combinar_pdfs).pack(side=tk.RIGHT, padx=5)

        # Listbox para exibir os PDFs adicionados
        self.pdf_listbox = tk.Listbox(root, selectmode=tk.SINGLE, height=15)
        self.pdf_listbox.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

    # Função para adicionar PDFs à lista
    def adicionar_pdfs(self):
        # Abre o diálogo para selecionar arquivos PDF
        arquivos = filedialog.askopenfilenames(
            title="Selecione os PDFs",
            filetypes=[("Arquivos PDF", "*.pdf")]
        )
        for arquivo in arquivos:
            # Adiciona o arquivo à lista, caso não esteja duplicado
            if arquivo not in self.pdf_list:
                self.pdf_list.append(arquivo)
                # Exibe apenas o nome do arquivo na Listbox
                nome_arquivo = os.path.basename(arquivo)
                self.pdf_listbox.insert(tk.END, nome_arquivo)

    # Função para remover o PDF selecionado da lista
    def remover_pdf(self):
        selecionado = self.pdf_listbox.curselection()  # Obtém o índice do item selecionado
        if selecionado:
            indice = selecionado[0]
            # Remove o arquivo da lista e da Listbox
            self.pdf_list.pop(indice)
            self.pdf_listbox.delete(indice)
        else:
            # Exibe uma mensagem se nenhum item estiver selecionado
            messagebox.showwarning("Aviso", "Nenhum item selecionado para remover.")

    # Função para remover todos os PDFs da lista
    def remover_todos(self):
        if self.pdf_list:
            self.pdf_list.clear()  # Limpa a lista
            self.pdf_listbox.delete(0, tk.END)  # Limpa a Listbox
        else:
            messagebox.showwarning("Aviso", "A lista já está vazia.")

    # Função para mover o PDF selecionado para cima na lista
    def mover_para_cima(self):
        selecionado = self.pdf_listbox.curselection()
        if selecionado:
            indice = selecionado[0]
            if indice > 0:
                # Troca os PDFs na lista e atualiza a Listbox
                self.pdf_list[indice], self.pdf_list[indice - 1] = self.pdf_list[indice - 1], self.pdf_list[indice]
                self.pdf_listbox.delete(indice)
                self.pdf_listbox.insert(indice - 1, os.path.basename(self.pdf_list[indice - 1]))
                self.pdf_listbox.select_set(indice - 1)  # Seleciona o item movido
        else:
            messagebox.showwarning("Aviso", "Nenhum item selecionado para mover.")

    # Função para mover o PDF selecionado para baixo na lista
    def mover_para_baixo(self):
        selecionado = self.pdf_listbox.curselection()
        if selecionado:
            indice = selecionado[0]
            if indice < len(self.pdf_list) - 1:
                # Troca os PDFs na lista e atualiza a Listbox
                self.pdf_list[indice], self.pdf_list[indice + 1] = self.pdf_list[indice + 1], self.pdf_list[indice]
                self.pdf_listbox.delete(indice)
                self.pdf_listbox.insert(indice + 1, os.path.basename(self.pdf_list[indice + 1]))
                self.pdf_listbox.select_set(indice + 1)  # Seleciona o item movido
        else:
            messagebox.showwarning("Aviso", "Nenhum item selecionado para mover.")

    # Função para combinar os PDFs da lista em um único arquivo
    def combinar_pdfs(self):
        if not self.pdf_list:
            messagebox.showwarning("Aviso", "Nenhum PDF foi adicionado.")
            return

        # Abre o diálogo para salvar o arquivo combinado
        caminho_saida = filedialog.asksaveasfilename(
            title="Salvar arquivo combinado como",
            defaultextension=".pdf",
            filetypes=[("Arquivo PDF", "*.pdf")],
            initialfile="arquivo_combinado.pdf"
        )
        if not caminho_saida:
            return  # Cancela a operação se o usuário não selecionar um local

        try:
            writer = PdfWriter()  # Cria um objeto para escrever PDFs
            for caminho_arquivo in self.pdf_list:
                reader = PdfReader(caminho_arquivo)  # Lê o PDF
                for pagina in reader.pages:
                    writer.add_page(pagina)  # Adiciona cada página ao novo PDF

            # Salva o arquivo combinado
            with open(caminho_saida, "wb") as arquivo_final:
                writer.write(arquivo_final)

            messagebox.showinfo("Sucesso", "PDFs combinados com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro", f"Falha ao combinar PDFs: {e}")

# Inicializa o aplicativo
if __name__ == "__main__":
    root = tk.Tk()  # Cria a janela principal
    app = PDFMergerApp(root)  # Instancia o aplicativo
    root.mainloop()  # Inicia o loop principal do Tkinter
