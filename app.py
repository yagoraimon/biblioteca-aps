from flask import Flask, render_template, redirect, url_for, request, flash, session
from models import db, Livro, Autor, Editora, Usuario, Emprestimo
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///biblioteca.db'
app.config['SECRET_KEY'] = 'minha_chave_secreta'

db.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']
        usuario = Usuario.query.filter_by(email=email).first()
        if usuario and usuario.verificar_senha(senha):
            session['usuario_id'] = usuario.id
            flash('Login realizado com sucesso!')
            return redirect(url_for('index'))
        else:
            flash('Credenciais inválidas. Tente novamente.')
    return render_template('login.html')

@app.route('/cadastro_usuario', methods=['GET', 'POST'])
def cadastro_usuario():
    if request.method == 'POST':
        usuario_id = request.form.get('usuario_id')
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']
        
        if usuario_id:
            usuario = Usuario.query.get(usuario_id)
            usuario.nome = nome
            usuario.email = email
            if senha:
                usuario.senha = senha
            flash('Usuário atualizado com sucesso!')
        else:
            novo_usuario = Usuario(nome=nome, email=email)
            novo_usuario.senha = senha
            db.session.add(novo_usuario)
            flash('Usuário cadastrado com sucesso!')
        
        db.session.commit()
        return redirect(url_for('cadastro_usuario'))
    
    if request.args.get('edit'):
        usuario = Usuario.query.get(request.args.get('edit'))
        usuarios = Usuario.query.all()
        return render_template('cadastro_usuario.html', usuario=usuario, usuarios=usuarios)
    
    if request.args.get('delete'):
        usuario = Usuario.query.get(request.args.get('delete'))
        db.session.delete(usuario)
        db.session.commit()
        flash('Usuário excluído com sucesso!')
        return redirect(url_for('cadastro_usuario'))

    usuarios = Usuario.query.all()
    return render_template('cadastro_usuario.html', usuarios=usuarios)


@app.route('/cadastro_livro', methods=['GET', 'POST'])
def cadastro_livro():
    if request.method == 'POST':
        livro_id = request.form.get('livro_id')
        titulo = request.form['titulo']
        autor_id = request.form['autor_id']
        editora_id = request.form['editora_id']
        ano_publicacao = request.form['ano_publicacao']
        
        if livro_id:
            livro = Livro.query.get(livro_id)
            livro.titulo = titulo
            livro.autor_id = autor_id
            livro.editora_id = editora_id
            livro.ano_publicacao = ano_publicacao
            flash('Livro atualizado com sucesso!')
        else:
            novo_livro = Livro(titulo=titulo, autor_id=autor_id, editora_id=editora_id, ano_publicacao=ano_publicacao, status='disponível')
            db.session.add(novo_livro)
            flash('Livro cadastrado com sucesso!')
        
        db.session.commit()
        return redirect(url_for('cadastro_livro'))
    
    if request.args.get('edit'):
        livro = Livro.query.get(request.args.get('edit'))
        autores = Autor.query.all()
        editoras = Editora.query.all()
        return render_template('cadastro_livro.html', livro=livro, autores=autores, editoras=editoras)
    
    if request.args.get('delete'):
        livro = Livro.query.get(request.args.get('delete'))
        db.session.delete(livro)
        db.session.commit()
        flash('Livro excluído com sucesso!')
        return redirect(url_for('cadastro_livro'))

    autores = Autor.query.all()
    editoras = Editora.query.all()
    livros = Livro.query.all()
    return render_template('cadastro_livro.html', autores=autores, editoras=editoras, livros=livros)

@app.route('/cadastro_autor', methods=['GET', 'POST'])
def cadastro_autor():
    if request.method == 'POST':
        autor_id = request.form.get('autor_id')
        nome = request.form['nome']
        nacionalidade = request.form['nacionalidade']
        data_nascimento = request.form['data_nascimento']
        
        if autor_id:
            autor = Autor.query.get(autor_id)
            autor.nome = nome
            autor.nacionalidade = nacionalidade
            autor.data_nascimento = data_nascimento
            flash('Autor atualizado com sucesso!')
        else:
            novo_autor = Autor(nome=nome, nacionalidade=nacionalidade, data_nascimento=data_nascimento)
            db.session.add(novo_autor)
            flash('Autor cadastrado com sucesso!')
        
        db.session.commit()
        return redirect(url_for('cadastro_autor'))
    
    if request.args.get('edit'):
        autor = Autor.query.get(request.args.get('edit'))
        autores = Autor.query.all()
        return render_template('cadastro_autor.html', autor=autor, autores=autores)
    
    if request.args.get('delete'):
        autor = Autor.query.get(request.args.get('delete'))
        db.session.delete(autor)
        db.session.commit()
        flash('Autor excluído com sucesso!')
        return redirect(url_for('cadastro_autor'))

    autores = Autor.query.all()
    return render_template('cadastro_autor.html', autores=autores)

@app.route('/cadastro_editora', methods=['GET', 'POST'])
def cadastro_editora():
    if request.method == 'POST':
        editora_id = request.form.get('editora_id')
        nome = request.form['nome']
        endereco = request.form['endereco']
        telefone = request.form['telefone']
        
        if editora_id:
            editora = Editora.query.get(editora_id)
            editora.nome = nome
            editora.endereco = endereco
            editora.telefone = telefone
            flash('Editora atualizada com sucesso!')
        else:
            nova_editora = Editora(nome=nome, endereco=endereco, telefone=telefone)
            db.session.add(nova_editora)
            flash('Editora cadastrada com sucesso!')
        
        db.session.commit()
        return redirect(url_for('cadastro_editora'))
    
    if request.args.get('edit'):
        editora = Editora.query.get(request.args.get('edit'))
        editoras = Editora.query.all()
        return render_template('cadastro_editora.html', editora=editora, editoras=editoras)
    
    if request.args.get('delete'):
        editora = Editora.query.get(request.args.get('delete'))
        db.session.delete(editora)
        db.session.commit()
        flash('Editora excluída com sucesso!')
        return redirect(url_for('cadastro_editora'))

    editoras = Editora.query.all()
    return render_template('cadastro_editora.html', editoras=editoras)

@app.route('/emprestimo', methods=['GET', 'POST'])
def emprestimo():
    if request.method == 'POST':
        usuario_id = request.form['usuario_id']
        livro_id = request.form['livro_id']
        novo_emprestimo = Emprestimo(usuario_id=usuario_id, livro_id=livro_id, data_emprestimo=datetime.utcnow())
        livro = Livro.query.get(livro_id)
        livro.status = 'emprestado'
        db.session.add(novo_emprestimo)
        db.session.commit()
        flash('Empréstimo realizado com sucesso!')
        return redirect(url_for('emprestimo'))
    usuarios = Usuario.query.all()
    livros = Livro.query.filter_by(status='disponível').all()
    return render_template('emprestimo.html', usuarios=usuarios, livros=livros)

@app.route('/consulta', methods=['GET'])
def consulta():
    titulo = request.args.get('titulo')
    autor_nome = request.args.get('autor')
    editora_nome = request.args.get('editora')

    query = Livro.query.join(Autor).join(Editora)

    if titulo:
        query = query.filter(Livro.titulo.contains(titulo))
    if autor_nome:
        query = query.filter(Autor.nome.contains(autor_nome))
    if editora_nome:
        query = query.filter(Editora.nome.contains(editora_nome))

    livros = query.all()
    return render_template('consulta.html', livros=livros)

@app.route('/relatorios', methods=['GET'])
def relatorios():
    emprestimos = Emprestimo.query.all()
    return render_template('relatorios.html', emprestimos=emprestimos)

@app.route('/devolucao', methods=['GET', 'POST'])
def devolucao():
    if request.method == 'POST':
        usuario_id = request.form['usuario_id']
        livro_id = request.form['livro_id']
        
        emprestimo = Emprestimo.query.filter_by(usuario_id=usuario_id, livro_id=livro_id, data_devolucao=None).first()
        if emprestimo:
            emprestimo.data_devolucao = datetime.utcnow()
            livro = Livro.query.get(livro_id)
            livro.status = 'disponível'
            db.session.commit()
            flash('Devolução registrada com sucesso!')
        else:
            flash('Empréstimo não encontrado ou já devolvido.')
        return redirect(url_for('devolucao'))
    
    usuarios = Usuario.query.all()
    livros = Livro.query.filter_by(status='emprestado').all()
    return render_template('devolucao.html', usuarios=usuarios, livros=livros)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
