from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def home(request):
    return render(request, 'registration/login.html')  # 'home.html' 템플릿을 렌더링

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # 사용자 생성
            messages.success(request, '회원가입이 완료되었습니다!')
            return redirect('login')  # 회원가입 후 로그인 페이지로 리디렉션
    else:
        form = UserCreationForm()

    return render(request, 'registration/signup.html', {'form': form})