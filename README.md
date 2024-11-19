# Gerenciador de PDFs

O **Gerenciador de PDFs** é uma aplicação gráfica desenvolvida em Python que permite adicionar, remover, alterar a sequência e combinar arquivos PDF. A ferramenta é ideal para usuários que precisam organizar e mesclar documentos PDF de forma simples e intuitiva.

---

## 🎯 **Funcionalidades**

1. **Adicionar PDFs**  
   Permite selecionar vários arquivos PDF do seu computador e adicioná-los à lista para processamento.

2. **Remover Selecionado**  
   Remove um arquivo PDF específico da lista.

3. **Mover Para Cima/Para Baixo**  
   Altera a ordem dos arquivos na lista, garantindo que eles sejam combinados na sequência desejada.

4. **Combinar PDFs**  
   Une todos os PDFs da lista em um único arquivo, permitindo salvar o resultado em qualquer local desejado.

5. **Visualizar a Lista de PDFs**  
   Exibe em uma lista todos os arquivos adicionados, facilitando a organização.

---

## 🛠️ **Tecnologias Utilizadas**

- **Python**: Linguagem principal do projeto.
- **Tkinter**: Para criação da interface gráfica.
- **PyPDF**: Para manipulação e combinação de arquivos PDF.

---

## 💻 **Como Usar**

### Pré-requisitos

1. **Python 3.8+** instalado no computador.
2. Instalar as bibliotecas necessárias:
   ```bash
   pip install pypdf
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
1. Botões para gerenciar os arquivos PDF:
   - **Adicionar PDFs**
   - **Remover Selecionado**
   - **Mover Para Cima**
   - **Mover Para Baixo**
   - **Combinar PDFs**

2. Lista central para exibição dos PDFs adicionados.

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

--- 