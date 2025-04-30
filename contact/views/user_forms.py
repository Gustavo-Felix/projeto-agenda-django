from django.shortcuts import render, redirect # type: ignore
from django.contrib import auth, messages # type: ignore
from django.contrib.auth.forms import AuthenticationForm # type: ignore
from django.contrib.auth.decorators import login_required # type: ignore
from contact.forms import RegisterForm, RegisterUpdateForm 

def register(request):
    form = RegisterForm()

    if request.method ==  'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save() 
            messages.success(request, 'Usuário Cadastrado!')
            return redirect('contact:login')

    return render(
        request,
        'contact/register.html',
        {
            'form': form,
            'site_title': 'Registrar-se'
        }
    )

def login_view(request):
    form = AuthenticationForm(request)

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        
        if form.is_valid():
            user = form.get_user()
            messages.success(request, 'Login efetuado com sucesso!')
            auth.login(request, user)
            return redirect('contact:index')
        messages.error(request, 'Login inválido!')

    return render(
        request,
        'contact/login.html',
        {
            'form': form,
            'site_title': 'Login'
        }
    )

@login_required(login_url='contact:login')
def logout_view(request):
    auth.logout(request)

    return redirect('contact:login')
    
@login_required(login_url='contact:login')
def user_update(request):
    form = RegisterUpdateForm(instance=request.user)

    if request.method != 'POST':
        return render(
            request,
            'contact/register.html',
            {
                'form': form,
                'site_title': 'Update'
            }
        )

    form = RegisterUpdateForm(data=request.POST, instance=request.user)

    if not form.is_valid():
        return render(
            request,
            'contact/register.html',
            {
                'form': form,
                'site_title': 'Update'
            }
        )
    
    form.save()

    return redirect('contact:index')