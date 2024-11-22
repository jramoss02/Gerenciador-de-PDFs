# Gerenciador de PDFs

O **Gerenciador de PDFs** é uma aplicação gráfica desenvolvida em Python que permite adicionar, remover, alterar a sequência e combinar arquivos PDF. A ferramenta é ideal para usuários que precisam organizar e mesclar documentos PDF de forma simples e intuitiva, agora com a funcionalidade de visualizar miniaturas das páginas do PDF.

---

## 🎯 **Funcionalidades**

1. **Adicionar PDFs**  
   Permite selecionar vários arquivos PDF do seu computador e adicioná-los à lista para processamento.

2. **Remover Selecionado**  
   Remove um arquivo PDF específico da lista.
   
3. **Remover Todos**  
   Remove todos os arquivos da lista.

4. **Mover Para Cima/Para Baixo**  
   Altera a ordem dos arquivos na lista, garantindo que eles sejam combinados na sequência desejada.

5. **Combinar PDFs**  
   Une todos os PDFs da lista em um único arquivo, permitindo salvar o resultado em qualquer local desejado.

6. **Visualizar a Lista de PDFs**  
   Exibe em uma lista todos os arquivos adicionados, facilitando a organização.

7. **Exibição de Miniaturas**  
   Mostra uma prévia das páginas de cada PDF adicionado, com miniaturas das páginas exibidas em uma área lateral. Isso facilita a visualização rápida do conteúdo dos PDFs antes de combiná-los.

---

## 🛠️ **Tecnologias Utilizadas**

- **Python**: Linguagem principal do projeto.
- **Tkinter**: Para criação da interface gráfica.
- **PyPDF**: Para manipulação e combinação de arquivos PDF.
- **Pillow (PIL)**: Para manipulação de imagens, utilizada para exibição das miniaturas dos PDFs.
- **pdf2image**: Para conversão das páginas do PDF em imagens.

---

## 💻 **Como Usar**

### Pré-requisitos

1. **Python 3.8+** instalado no computador.
2. Instalar as bibliotecas necessárias:
   ```bash
   pip install pypdf pillow pdf2image
   ```

---

### Executando o Projeto

1. Baixe ou clone o repositório:
   ```bash
   git clone https://github.com/jramoss02/Gerenciador-de-PDFs.git
   cd gerenciador-pdfs
   ```

2. Execute o script Python:
   ```bash
   python gerenciador_pdfs.py
   ```

---

## 🚀 **Gerando o Executável**

Para criar um executável do projeto que funcione sem o Python instalado:

1. Instale o **PyInstaller**:
   ```bash
   pip install pyinstaller
   ```

2. Gere o executável:
   ```bash
   pyinstaller --onefile --noconsole gerenciador_pdfs.py
   ```

3. O executável será gerado na pasta `dist/`. Basta distribuí-lo aos usuários.

---

## 🖼️ **Interface do Usuário**

### Tela Principal

1. **Botões para gerenciar os arquivos PDF**:
   - **Adicionar PDFs**
   - **Remover Selecionado**
   - **Mover Para Cima**
   - **Mover Para Baixo**
   - **Combinar PDFs**

2. **Lista centralizada**: Exibe todos os arquivos PDF adicionados de forma centralizada, com a opção de alterar a ordem ou remover os arquivos.

3. **Exibição de miniaturas**: As páginas dos PDFs são convertidas para imagens e exibidas como miniaturas em uma área lateral da interface, permitindo visualizar rapidamente as páginas dos documentos.

---

## 🔧 **Personalizações**

1. **Ícone do Executável**  
   Para alterar o ícone do aplicativo, inclua um arquivo `.ico` e use a flag `--icon` ao gerar o executável:
   ```bash
   pyinstaller --onefile --noconsole --icon=icone.ico gerenciador_pdfs.py
   ```

2. **Pasta Inicial para Seleção de Arquivos**  
   Altere a variável `initialdir` no método `filedialog.askopenfilenames()` para definir o diretório padrão.

---

## ⚠️ **Cuidados**

- Certifique-se de que todos os arquivos PDF estão acessíveis e não estão sendo usados por outros programas.
- Para evitar erros, não utilize caracteres especiais nos nomes dos arquivos PDF.

---

## 🏆 **Contribuições**

Contribuições são bem-vindas!  
Siga as etapas abaixo para contribuir com o projeto:

1. Faça um fork do repositório.
2. Crie uma branch para sua feature:
   ```bash
   git checkout -b minha-feature
   ```
3. Envie as mudanças:
   ```bash
   git push origin minha-feature
   ```

---

## 📄 **Licença**

Este projeto está licenciado sob a [MIT License](LICENSE).

---

## 📞 **Contato**

Se tiver dúvidas ou sugestões, entre em contato:
- **Email**: 02.jrsramos@gmail.com
- **LinkedIn**: [José Ramos](https://linkedin.com/in/josé-roberto-ramos)
