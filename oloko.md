# Sistema de Gerenciamento de Biblioteca

O sistema de gerenciamento de biblioteca permite o cadastro de livros, autores e editoras, além de realizar empréstimos e devoluções, consultar o acervo, gerar relatórios e controlar os usuários do sistema.

## Requisitos do Sistema

- Python 3.7 ou superior
- Flask 2.0 ou superior
- SQLite

## Instalação e Configuração

### Crie e Ative um Ambiente Virtual
```bash
    python -m venv venv
    source venv/bin/activate  # No Windows, use venv\Scripts\activate
```
### Instale as Dependências
```bash
    pip install -r requirements.txt
```
### Inicialize o Banco de Dados
```bash
    from app import db, app
    with app.app_context():
        db.create_all()
```
### Execute o Aplicativo
```bash
    python app.py
```

## Guia do Usuário

### Acessando o Sistema

Abra um navegador e acesse http://127.0.0.1:5000.

### Funcionalidades

#### Cadastro de Livros

Navegue para "Cadastro de Livros".
Preencha os campos e clique em "Cadastrar Livro".
Para editar ou excluir um livro, use os links de ação na tabela de livros cadastrados.

#### Cadastro de Autores

Navegue para "Cadastro de Autores".
Preencha os campos e clique em "Cadastrar Autor".
Para editar ou excluir um autor, use os links de ação na tabela de autores cadastrados.

#### Cadastro de Editoras

Navegue para "Cadastro de Editoras".
Preencha os campos e clique em "Cadastrar Editora".
Para editar ou excluir uma editora, use os links de ação na tabela de editoras cadastradas.

#### Cadastro de Usuários

Navegue para "Cadastro de Usuários".
Preencha os campos e clique em "Cadastrar Usuário".
Para editar ou excluir um usuário, use os links de ação na tabela de usuários cadastrados.

#### Empréstimo de Livros

Navegue para "Empréstimos".
Selecione o usuário e o livro e clique em "Realizar Empréstimo".

#### Devolução de Livros

Navegue para "Devoluções".
Selecione o usuário e o livro e clique em "Registrar Devolução".

#### Consulta ao Acervo

Navegue para "Consulta".
Preencha os campos de busca e clique em "Consultar".

#### Relatórios

Navegue para "Relatórios".
Visualize os registros de empréstimos e devoluções.

## Estrutura do Projeto

biblioteca/
├── app.py
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── cadastro_livro.html
│   ├── cadastro_autor.html
│   ├── cadastro_editora.html
│   ├── cadastro_usuario.html
│   ├── emprestimo.html
│   ├── devolucao.html
│   ├── consulta.html
│   ├── relatorios.html
├── static/
│   ├── css/
│       ├── style.css
├── models.py
├── requirements.txt

### Clone o Repositório
