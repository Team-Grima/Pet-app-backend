from django.urls import path, include
from django.contrib.auth import views as auth_views
from rest_framework_simplejwt.views import TokenObtainPairView

from common import views
#from common.views import RegisterAPIView

app_name = 'common'

urlpatterns = [
    #path('login/', auth_views.LoginView.as_view(template_name='common/login.html'),name='login'),
    #path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    #path('register/', RegisterAPIView.as_view()),
    #path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('1/', include('dj_rest_auth.urls')),
    path('2/', include('dj_rest_auth.registration.urls')),
    path('3/', include('allauth.urls')),


]