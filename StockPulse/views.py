from django.shortcuts import render

def home(request):
    return render(request, 'registration/login.html')  # 'home.html' 템플릿을 렌더링