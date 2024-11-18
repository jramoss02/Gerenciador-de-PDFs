import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from pypdf import PdfReader, PdfWriter

class PDFMergerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gerenciador de PDFs")
        self.pdf_list = []

        button_frame = tk.Frame(root)
        button_frame.pack(fill=tk.X, padx=10, pady=5)

        tk.Button(button_frame, text="Adicionar PDFs", command=self.adicionar_pdfs).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Remover Selecionado", command=self.remover_pdf).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Mover Para Cima", command=self.mover_para_cima).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Mover Para Baixo", command=self.mover_para_baixo).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Combinar PDFs", command=self.combinar_pdfs).pack(side=tk.RIGHT, padx=5)

        self.pdf_listbox = tk.Listbox(root, selectmode=tk.SINGLE, height=15)
        self.pdf_listbox.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

    def adicionar_pdfs(self):
        arquivos = filedialog.askopenfilenames(
            title="Selecione os PDFs",
            filetypes=[("Arquivos PDF", "*.pdf")]
        )
        for arquivo in arquivos:
            if arquivo not in self.pdf_list:
                self.pdf_list.append(arquivo)
                self.pdf_listbox.insert(tk.END, arquivo)

    def remover_pdf(self):
        selecionado = self.pdf_listbox.curselection()
        if selecionado:
            indice = selecionado[0]
            self.pdf_list.pop(indice)
            self.pdf_listbox.delete(indice)
        else:
            messagebox.showwarning("Aviso", "Nenhum item selecionado para remover.")

    def mover_para_cima(self):
        selecionado = self.pdf_listbox.curselection()
        if selecionado:
            indice = selecionado[0]
            if indice > 0:
                self.pdf_list[indice], self.pdf_list[indice - 1] = self.pdf_list[indice - 1], self.pdf_list[indice]
                self.pdf_listbox.delete(indice)
                self.pdf_listbox.insert(indice - 1, self.pdf_list[indice - 1])
                self.pdf_listbox.select_set(indice - 1)
        else:
            messagebox.showwarning("Aviso", "Nenhum item selecionado para mover.")

    def mover_para_baixo(self):
        selecionado = self.pdf_listbox.curselection()
        if selecionado:
            indice = selecionado[0]
            if indice < len(self.pdf_list) - 1:

                self.pdf_list[indice], self.pdf_list[indice + 1] = self.pdf_list[indice + 1], self.pdf_list[indice]

                self.pdf_listbox.delete(indice)
                self.pdf_listbox.insert(indice + 1, self.pdf_list[indice + 1])
                self.pdf_listbox.select_set(indice + 1)
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


if __name__ == "__main__":
    root = tk.Tk()
    app = PDFMergerApp(root)
    root.mainloop()
