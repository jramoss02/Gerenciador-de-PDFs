import os
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
from PIL import Image, ImageTk
from pypdf import PdfReader, PdfWriter
from pdf2image import convert_from_path


class PDFMergerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gerenciador de PDFs")
        self.pdf_list = []

        # Frame principal
        main_frame = tk.Frame(root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

        # Frame de botões
        button_frame = tk.Frame(main_frame)
        button_frame.pack(fill=tk.X, padx=10, pady=5)

        # Botões principais
        tk.Button(button_frame, text="Adicionar PDFs", command=self.adicionar_pdfs).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Remover Selecionado", command=self.remover_pdf).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Remover Todos", command=self.remover_todos).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Mover Para Cima", command=self.mover_para_cima).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Mover Para Baixo", command=self.mover_para_baixo).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Combinar PDFs", command=self.combinar_pdfs).pack(side=tk.RIGHT, padx=5)

        self.split_frame = tk.Frame(main_frame)
        self.split_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

        self.listbox_frame = tk.Frame(self.split_frame)
        self.listbox_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.pdf_listbox = tk.Listbox(self.listbox_frame, selectmode=tk.SINGLE, height=15)
        self.pdf_listbox.pack(fill=tk.BOTH, expand=True)

        self.thumb_frame = tk.Frame(self.split_frame)
        self.thumb_frame.pack(side=tk.RIGHT, fill=tk.Y, padx=5)

        self.canvas = tk.Canvas(self.thumb_frame)
        self.canvas.pack(side=tk.LEFT, fill=tk.Y, expand=True)

        self.scrollbar = ttk.Scrollbar(self.thumb_frame, orient=tk.VERTICAL, command=self.canvas.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.canvas_frame = tk.Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.canvas_frame, anchor="nw")

        self.canvas_frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

    def adicionar_pdfs(self):
        arquivos = filedialog.askopenfilenames(
            title="Selecione os PDFs",
            filetypes=[("Arquivos PDF", "*.pdf")]
        )
        for arquivo in arquivos:
            if arquivo not in self.pdf_list:
                self.pdf_list.append(arquivo)
                nome_arquivo = os.path.basename(arquivo)
                self.pdf_listbox.insert(tk.END, nome_arquivo)
        self.atualizar_visualizador()

    def remover_pdf(self):
        selecionado = self.pdf_listbox.curselection()
        if selecionado:
            indice = selecionado[0]
            self.pdf_list.pop(indice)
            self.pdf_listbox.delete(indice)
            self.atualizar_visualizador()
        else:
            messagebox.showwarning("Aviso", "Nenhum item selecionado para remover.")

    def remover_todos(self):
        if self.pdf_list:
            self.pdf_list.clear()
            self.pdf_listbox.delete(0, tk.END)
            self.atualizar_visualizador()
        else:
            messagebox.showwarning("Aviso", "A lista já está vazia.")

    def mover_para_cima(self):
        selecionado = self.pdf_listbox.curselection()
        if selecionado:
            indice = selecionado[0]
            if indice > 0:
                self.pdf_list[indice], self.pdf_list[indice - 1] = self.pdf_list[indice - 1], self.pdf_list[indice]
                self.pdf_listbox.delete(indice)
                self.pdf_listbox.insert(indice - 1, os.path.basename(self.pdf_list[indice - 1]))
                self.pdf_listbox.select_set(indice - 1)
                self.atualizar_visualizador()
        else:
            messagebox.showwarning("Aviso", "Nenhum item selecionado para mover.")

    def mover_para_baixo(self):
        selecionado = self.pdf_listbox.curselection()
        if selecionado:
            indice = selecionado[0]
            if indice < len(self.pdf_list) - 1:
                self.pdf_list[indice], self.pdf_list[indice + 1] = self.pdf_list[indice + 1], self.pdf_list[indice]
                self.pdf_listbox.delete(indice)
                self.pdf_listbox.insert(indice + 1, os.path.basename(self.pdf_list[indice + 1]))
                self.pdf_listbox.select_set(indice + 1)
                self.atualizar_visualizador()
        else:
            messagebox.showwarning("Aviso", "Nenhum item selecionado para mover.")

    def combinar_pdfs(self):
        if not self.pdf_list:
            messagebox.showwarning("Aviso", "Nenhum PDF foi adicionado.")
            return
        caminho_saida = filedialog.asksaveasfilename(
            title="Salvar arquivo combinado como",
            defaultextension=".pdf",
            filetypes=[("Arquivo PDF", "*.pdf")],
            initialfile="arquivo_combinado.pdf"
        )
        if not caminho_saida:
            return
        try:
            writer = PdfWriter()
            for caminho_arquivo in self.pdf_list:
                reader = PdfReader(caminho_arquivo)
                for pagina in reader.pages:
                    writer.add_page(pagina)
            with open(caminho_saida, "wb") as arquivo_final:
                writer.write(arquivo_final)
            messagebox.showinfo("Sucesso", "PDFs combinados com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro", f"Falha ao combinar PDFs: {e}")

    def atualizar_visualizador(self):
        for widget in self.canvas_frame.winfo_children():
            widget.destroy()

        for arquivo in self.pdf_list:
            try:
                reader = PdfReader(arquivo)
                for i, pagina in enumerate(reader.pages):
                    img = self.converter_pagina_para_imagem(pagina, dpi=50)
                    if img:
                        tk_img = ImageTk.PhotoImage(img)
                        lbl = tk.Label(self.canvas_frame, image=tk_img)
                        lbl.image = tk_img
                        lbl.pack(pady=5)
            except Exception as e:
                print(f"Erro ao carregar {arquivo}: {e}")

    def converter_pagina_para_imagem(self, pagina_pdf, dpi=100):
        """
        Converte uma página de PDF para uma imagem.
        """
        try:
            with open("temp_page.pdf", "wb") as temp_pdf:
                writer = PdfWriter()
                writer.add_page(pagina_pdf)
                writer.write(temp_pdf)

            imagens = convert_from_path("temp_page.pdf", dpi=dpi)
            os.remove("temp_page.pdf")

            if imagens:
                return imagens[0]
            return None
        except Exception as e:
            print(f"Erro ao converter página para imagem: {e}")
            return None


if __name__ == "__main__":
    root = tk.Tk()
    app = PDFMergerApp(root)
    root.mainloop()
