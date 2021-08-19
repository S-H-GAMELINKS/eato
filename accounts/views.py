from django.shortcuts import render, redirect

def mypage(request):
    if request.user.is_anonymous:
        return redirect('/accounts/login')

    return render(request, 'account/mypage.html')
