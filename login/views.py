from django.shortcuts import render, redirect
from django.contrib import messages
from core.models import Gn_user

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = Gn_user.objects.get(username=username, password=password)
            # Kullanıcı bulundu, oturum aç ve ana sayfaya yönlendir
            request.session['user_id'] = user.userid 
            return redirect('homepage')  # Örneğin, anasayfa için 'home' isimli bir URL tanımlı olsun
        except Gn_user.DoesNotExist:
            # Kullanıcı bulunamadı, hata mesajı göster
            messages.error(request, 'Kullanıcı adı veya şifre yanlış.')
    return render(request, 'login.html')
