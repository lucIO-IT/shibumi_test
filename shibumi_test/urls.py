"""shibumi_test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import SimpleRouter
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

from user_auth.views import RegistrationAPIView
from core.views import TodoViewSet

router = SimpleRouter()
router.register(r'todos', TodoViewSet, basename='Todo')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signin/', obtain_jwt_token),
    path('signin/refresh/', refresh_jwt_token),
    path('signup/', RegistrationAPIView.as_view()),
    path('', include(router.urls)),
]
