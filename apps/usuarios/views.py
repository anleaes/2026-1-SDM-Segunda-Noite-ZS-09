from django.shortcuts import render, redirect

from .models import Usuario


def login(request):
    template_name = 'usuarios/login.html'

    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        try:
            usuario = Usuario.objects.get(email=email)
        except Usuario.DoesNotExist:
            return render(request, template_name, {'erro': 'Usuario nao encontrado'})

        if usuario.login(senha):
            request.session['usuario_id'] = usuario.id
            request.session['usuario_nome'] = usuario.nome
            return redirect('cliente_list')

        return render(request, template_name, {'erro': 'Senha incorreta'})

    return render(request, template_name)


def logout(request):
    request.session.clear()
    return redirect('login')


def cadastrar(request):
    template_name = 'usuarios/cadastrar.html'

    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        if Usuario.objects.filter(email=email).exists():
            return render(request, template_name, {'erro': 'Email ja cadastrado'})

        Usuario.objects.create(nome=nome, email=email, senha=senha)
        return redirect('login')

    return render(request, template_name)
