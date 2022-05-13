from django.contrib.auth.models import User
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework_jwt.views import ObtainJSONWebToken
from rest_framework_jwt.serializers import *

from .config.serializers import RegisterSerializer


# Create your views here.


class RegistrationAPIView(CreateAPIView):

    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = (AllowAny,)
