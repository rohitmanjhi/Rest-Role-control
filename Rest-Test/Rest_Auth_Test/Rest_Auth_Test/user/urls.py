from django.urls import include, path, re_path
from .views import SignUp, ForgotPassword, user_detail, user_list, user_add, Login

urlpatterns = [
    path('api/signup/', SignUp.as_view(),
         name='sign_up'),
    path('api/forgot/password', ForgotPassword.as_view(),
         name='forgot_password'),
    path('token/', Login.as_view(), name='token_obtain_pair'),
]
