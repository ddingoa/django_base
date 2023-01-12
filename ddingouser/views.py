from django.contrib.auth.models import User
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from  django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.db import IntegrityError

class BaseView(View):
    @staticmethod
    def response(data={}, message='', status=200):
        result = {
            'data' : data,
            'meassge' : message,
        }
        return JsonResponse(result,status)

class UserCreateView(BaseView):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(UserCreateView,self).dispatch(request, *args, **kwargs)

    def post(self, request):
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        email = request.POST.get('email', '')

        try:
            user = User.objects.create_user(username, email, password)
        except IntegrityError:
            return self.response(message='이미 존재하는 아이디입니다.', status=400)

        return self.response({'user.id': user.id})
