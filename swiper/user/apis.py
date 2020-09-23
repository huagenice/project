# Create your views here.
from django.http import JsonResponse
from django.core.cache import cache
from user.logics import send_vcode
from user.models import User


def fetch_vcode(request):
    '''给用户发送验证码'''
    phonenum = request.GET.get('phonenum')
    if send_vcode(phonenum):
        return JsonResponse({'code': 0, 'data': None})
    else:
        return JsonResponse({'code': 1000, 'data': '验证码发送失败'})


def submot_vcode(request):
    '''提交验证码，执行注册登录'''
    phonenum = request.POST.get('phonenum')
    vcode = request.POST.get('vcode')

    key = 'Vcode-%s' % phonenum
    cached_vcode = cache.get(key)

    if vcode and vcode == cached_vcode:
        # 考虑：如果缓存的vcode过期变为了none值，且用户没有输入验证码也是none
        # 值，却反而通过了
        try:
            user = User.objects.get(phonenum=phonenum)  # 从数据库获取用户
        except User.DoesNotExist:
            # 如果用户不存在，则执行注册流程
            user = User.objects.create(phonenum=phonenum, nickname=phonenum)
        # session中记录用户登录状态
        request.session['uid'] = user.id
        return JsonResponse({'code': 0, 'data': user.to_dict()})

    return JsonResponse({'code': 1001, 'data': '验证码错误'})


def show_profile(request):
    '''给用户发送验证码'''
    return JsonResponse()


def update_project(request):
    '''查看个人资料'''
    return JsonResponse()


def qn_token(request):
    '''给用户发送验证码'''
    return JsonResponse()


def qn_callback(request):
    '''给用户发送验证码'''
    return JsonResponse()
