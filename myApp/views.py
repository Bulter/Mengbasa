import hashlib
import random
import time

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from myApp.models import LoopImg, User, Rwm, Cart

def index(request):
    imgs = LoopImg.objects.all()

    # 获取token
    token = request.session.get('token')
    user = None

    if token:
        user = User.objects.get(token=token)
        print(user.email)

    data = {
        'imgs': imgs,
        'user': user
    }
    return render(request, 'index.html', data)


def login(request):
    err = ""
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(email, password)
        try:
            # 假如账号错误，抛出异常
            user = User.objects.get(email=email)
            if user.password == generate_password(password):  # 成功
                user.token = generate_token()
                user.save()
                request.session['token'] = user.token
                return redirect('myApp:index')
            else:  # 密码错误
                err = '密码错误'
                return render(request, 'login.html', context={'err': err})
        except:
            err = '账号不存在'
            return render(request, 'login.html', context={'err': err})


def generate_password(param):
    md5 = hashlib.md5()
    md5.update(param.encode('utf-8'))
    return md5.hexdigest()


def generate_token():
    md5 = hashlib.md5()
    tempstr = str(time.time()) + str(random.random())
    md5.update(tempstr.encode('utf-8'))
    return md5.hexdigest()


def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    elif request.method == 'POST':
        user = User()
        user.email = request.POST.get('email')
        user.password = generate_password(request.POST.get('password'))
        user.name = request.POST.get('name')
        user.phone = request.POST.get('phone')

        # 状态保持
        user.token = generate_token()
        request.session['token'] = user.token

        # 存储数据库
        user.save()

        return redirect('myApp:index')


def logout(request):
    request.session.flush()
    return redirect('myApp:index')


def loopimg(request):
    loopimg = LoopImg.objects.all()
    print(request.GET.get('msg'))
    return JsonResponse(loopimg)


def checkEP(request):
    email = request.GET.get('email')

    users = User.objects.filter(email=email)
    if users.exists():  # 占用
        return JsonResponse({'msg': '账号被占用！', 'status': 0})
    else:  # 可用
        return JsonResponse({'msg': '账号可以使用!', 'status': 1})


def checkDetail(request):
    rwms = Rwm.objects.all()
    data = {}
    for rwm in rwms:
        data[rwm.rwmID] = rwm
    return JsonResponse(data)


def detail(request, id):
    rwms = Rwm.objects.all()
    rwm = rwms[int(id)-1]
    data = {
        'rwm': rwm,
    }
    print("Hello")
    return render(request, 'detail_information.html', data)


def cart(request):
    token = request.session.get('token')
    if token:
        user = User.objects.get(token=token)
        datas = Cart.objects.filter(user=user)
        return render(request, 'shopping_cart.html', {'datas': datas})
    else:
        return redirect('myApp:login')

# carts = Cart.objects.filter(user=user).filter(goods=goods)

def addCart(request):
    token = request.session.get('token')
    if token:
        user = User.objects.get(token=token)
        goods = Rwm.objects.get(id=request.GET.get('id'))
        carts = Cart.objects.filter(user=user).filter(goods=goods)
        if carts.exists():
            print('添加失败')
            return JsonResponse({'msg': '添加失败,您购物车中已有同类型商品', 'status': 0})
        else:
            cart = Cart()
            cart.user = user
            cart.goods = goods
            cart.size = request.GET.get('size')
            cart.color = request.GET.get('color')
            cart.number = request.GET.get('number')
            cart.save()
            print("添加成功")
            return JsonResponse({'msg': '{}添加成功'.format(cart.goods.rwmName), 'status': 1})
    else:
        print('神经')
        return redirect('myApp:login')
