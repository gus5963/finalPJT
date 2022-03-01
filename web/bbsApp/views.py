from django.shortcuts import render, redirect
from .models import *
# Create your views here.

# 사용자의 상태정도 저장하기 위해서 session
#
def index(request):
    print('✅ GET bbs Index 🚀')
    if request.session.get('userId') and request.session.get('userName'):
        context = {
            'id' : request.session['userId'],
            'name' : request.session['userName']
        }
        # session에 넣어진 값들을 갖고 오는방법
        return render(request, 'home.html', context)
    else:
        print('⛔️ Wrong Password or ID')
        return render(request, 'login.html')


def joinForm(request):
    print('✅ GET bbs joinForm 🚀')
    return render(request, 'join.html')

def bbsLogin(request):
    print('✅ GET bbs Login 🚀')
    if request.method == 'GET':
        return redirect('bbsIndex')
    else:
        id = request.POST['id']
        pwd = request.POST['pwd']

        user = BbsUser.objects.get(userId=id,userPwd=pwd)
        print('user result :',user)
        context = {}
        if user is not None :
            request.session['userId'] = user.userId
            request.session['userName'] = user.userName
            # session을 만들어주는 과정
            context['id']=request.session['userId']
            context['name'] = request.session['userName']
            # context에 session을 넣어주는 과정
            return render(request, 'home.html', context)
        else:
            return redirect('bbsIndex')

def bbsList(request):
    print('✅ GET bbs List 🚀')
    boards = BbsList.objects.all()
    context = {
        'boards' : boards,
        'id': request.session['userId'],
        'name': request.session['userName']
    }
    return render(request, 'list.html', context)


def bbsRegisterForm(request):
    print('✅ GET bbs Register Form 🚀')
    context = {
        'id' : request.session['userId'],
        'name' : request.session['userName']
    }
    return render(request, 'bbsRegisterForm.html', context)


def bbsLogOut(request):
    print('✅ GET bbs LogOut 🚀')
    request.session['userId'] = {}
    request.session['userName'] = {}
    request.session['userPwd'] = {}
    request.session.modified = True
    return redirect('bbsIndex')

def uploadForm(request):
    print('✅ GET bbs UploadForm 🚀')
    title = request.POST['title']
    content = request.POST['content']
    writer = request.POST['writer']
    print('✅ request check', title, content, writer)
    BbsList(title=title, content=content,writer=writer).save()
    return render(request, 'list.html')

def bbsRead(request):
    print('✅ GET bbs Read 🚀')
    boards