from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from  django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout

def register_view(request):
    if request.user.is_authenticated:
        return render(request, 'login.html', {'custom_error': 'Siz ushbu profildan chiqmay turib boshqasiga kirsa olmaysiz !!!'})

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
           # Agar to'g'ri bo'lsa, saqlaymiz va login sahifasiga yo'naltiramiz
            form.save()
            return redirect('login')
    else:
        # Agar so'rov 'GET' bo'lsa, bo'sh forma yaratamiz
        form = CustomUserCreationForm()
    # Yaratilgan formani (bo'sh yoki xatolari bilan) shablonga yuboramiz
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.user.is_authenticated:
        return render(request, 'login.html', {'custom_error': 'Siz ushbu profildan chiqmay turib boshqasiga kirsa olmaysiz !!!'})

    if request.method == 'POST':
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
        else:
            # Xatolik bo'lsa, redirect qilmasdan, formani xatoliklari bilan qaytaramiz
            return render(request, 'login.html', {'form': form})
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form':form})

def logout_view(request):
    logout(request) # Foydalanuvchini tizimdan chiqaramiz
    return redirect('login') # Tizimdan chiqqandan so'ng login sahifasiga yo'naltiramiz