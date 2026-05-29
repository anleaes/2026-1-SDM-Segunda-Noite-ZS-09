from django.shortcuts import redirect


def login_obrigatorio(view):
    def wrapper(request, *args, **kwargs):
        if not request.session.get('usuario_id'):
            return redirect('login')
        return view(request, *args, **kwargs)
    return wrapper
