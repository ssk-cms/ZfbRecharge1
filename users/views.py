import json

from django.contrib.auth.hashers import make_password,check_password
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect
from users.models import Register
from users.form import UserLogin,UserRegister
import hashlib


# Create your views here.

#注册
def Register_views(request):
    # 判断是get请求还是post请求，得到用户的请求意图
    if request.method == 'GET':
        return render(request, 'register.html')
    # post请求
    else:
        # #先验证手机号在数据库中是否存在
        uphone = request.POST['uphone']
        users = Register.objects.filter(phone_number=uphone)
        if users:
          #uphone 已经存在
          errMsg = '手机号码已经存在'
          return render(request,'register.html',locals())
        # 接收数据插入到数据库中
        upwd = request.POST['upwd']
        cpwd = request.POST['cpwd']
        if upwd != cpwd:
            error = '密码输入错误!'
            return render(request, 'register.html', locals())
        uname = request.POST['uname']
        uemail = request.POST['uemail']
        select_pwd = make_password(upwd,None,'pbkdf2_sha1')
        user = Register()
        user.phone_number = uphone
        user.password = select_pwd
        user.username = uname
        user.email = uemail
        user.save()
        # 取出user中的id 和 uphone的值保存进session
        request.session['uid'] = user.id
        request.session['uphone'] = user.phone_number
        return redirect('index:number_list1')


#登录

def Login_views(request):
    # 判断　get 请求还是　post　请求
    if request.method == 'GET':
        # 　获取来访地址，如果没有则设置为/
        url = request.META.get('HTTP_REFERER', '/')
        # get请求　－　判断session,判断cookie,登录页
        # 先判断session中是否有登录信息
        if 'uid' in request.session and 'uphone' in request.session:
            # 有登录信息保存在　session
            # 从哪来，回哪去
            id = request.session['uid']
            uname=Register.objects.get(id=id).username
            return render(request,'./index/index.html',locals())

        else:
            # 没有登录信息保存在　session，继续判断cookies中是否有登录信息
            if 'uid' in request.COOKIES and 'uphone' in request.COOKIES:
                # cookies中有登录信息　－　曾经记住过密码
                # 将cookies中的信息取出来保存进session，再返回到首页
                uid = request.COOKIES['uid']
                uphone = request.COOKIES['uphone']
                request.session['uid'] = uid
                request.session['uphone'] = uphone
                # 从哪来，回哪去
                resp = redirect(url)
                return resp
            else:
                # cookies中没有登录信息　－　去往登录页
                return render(request,'login.html')
    # 请求方式为post请求
    else:
        # post请求 - 实现登录操作
        # 获取手机号和密码
        uphone = request.POST['uphone']
        upwd = request.POST['upwd']
        # 根据手机号查询该用户的加密密码
        users = Register.objects.filter(phone_number=uphone)
        if users:
            select_password = users[0].password
        # check_password()返回一个TRUE或FALSE
        else:
            message = '该用户未注册'
            return render(request,'login.html',locals())
        if check_password(upwd,select_password):
            # 登录成功：先存进session
            request.session['uid'] = users[0].id
            request.session['uphone'] = uphone
            # 声明响应对象：从哪来回哪去
            url = request.COOKIES.get('url', '/')
            resp = redirect(url)
            # 将url从cookies中删除出去
            if 'url' in request.COOKIES:
                resp.delete_cookie('url')
            # 判断是否要存进cookies
            if 'isSaved' in request.POST:
                expire = 60 * 60 * 24 * 90
                resp.set_cookie('uid', users[0].id, expire)
                resp.set_cookie('uphone', uphone, expire)
            # 有登录信息保存在　session
            # 从哪来，回哪去
            id = request.session['uid']
            uname = Register.objects.get(id=id).username
            return render(request, './index/index.html', locals())
        else:
            # 登录失败
            # 判断是手机号还是密码输入错误
            users_phone = Register.objects.filter(phone_number=uphone)
            if not users_phone:
                error = '手机号不存在!'
            else:
                error='密码输入错误!'
            return render(request, 'login.html', locals())


def Logout_views(request):
    # 判断session中是否有登录信息，有的话则清除
    if 'uid' in request.session and 'uphone' in request.session:
        del request.session['uid']
        del request.session['uphone']
        # 构建响应对象：哪发的退出请求，则返回到哪去
        # url = request.META.get('HTTP_REFERER', '/')
        # resp = HttpResponseRedirect(url)
        # 判断cookies中是否有登录信息，有的话，则删除
        if 'uid' in request.COOKIES and 'uphone' in request.COOKIES:
            del request.COOKIES['uid']
            del request.COOKIES['uphone']
        return redirect('/')
    return redirect('/')


# 定义login的装饰器
def login_required(fn):
    def login(request):
        if request.method == 'POST':
            form = UserLogin(request.POST)
            if form.is_valid():  # 获取表单信息
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                # password = hash_lib(password)
                namefilter = Register.objects.filter(username=username, password=password)
                unames = Register.objects.filter(username=username)
                for name in unames:
                    uname = name.username
                if len(namefilter) > 0:

                    return render(request, 'index.html', {'uname': uname})

                else:
                    return render(request, 'login.html', {'error': '该用户名不存在！'})
            fn()
        else:
            form = UserLogin()
            return render(request, 'login.html', {'form': form})
    return login


# # 检查　session 中是否有登录信息，如果有获取对应数据的uname值
# def check_login_views(request):
#   if 'uid' in request.session and 'uphone' in request.session:
#     loginStatus = 1
#     #通过uid的值获取对应的uname
#     id = request.session['uid']
#     uname=Register.objects.get(id=id).uname
#     dic = {
#       'loginStatus':loginStatus,
#       'uname':uname
#     }
#     return HttpResponse(json.dumps(dic))
#   else:
#     dic = {
#       'loginStatus':0
#     }
#     return HttpResponse(json.dumps(dic))

def Check_users(select1):
    if select1 == '用户':
        return redirect('/')
    elif select1 == '管理员':
        return redirect('/orders/')
    elif select1 == '老板':
        return redirect('/orders/')

# 无法登陆视图
def Detail_views(request):
    return render(request,'detail.html')


