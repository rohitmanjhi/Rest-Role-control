from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import status
from django.shortcuts import render
from Rest_Auth_Test.user.models import User
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view, permission_classes
from .serializers import UserSerializer, ForgotPasswordSerializer, LoginSerializer
from .utils import Permission
# Create your views here.


# Sign up functionality
class SignUp(APIView):
    serializer_class = UserSerializer

    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        # Check serializer valid or not
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Forgot password functionality
class ForgotPassword(APIView):
    serializer_class = ForgotPasswordSerializer

    def post(self, request, format=None):
        # Get all request data
        email = request.data.get('email')
        password = request.data.get('password')
        confirm_passrord = request.data.get('confirm_password')

        # Check all field exist or not
        if email and password and confirm_passrord:
            try:
                user = User.objects.get(email=email)

                # Check password or confirm password match or not
                if password == confirm_passrord:
                    user.set_password(password)
                    user.save()
                    return Response({"msg": "Password created successfully"}, status=status.HTTP_201_CREATED)
                return Response({"msg": "Password and confirm password not match"}, status=status.HTTP_400_BAD_REQUEST)
            except User.DoesNotExist:
                return Response({"msg": "Email does not exist"}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"msg": "Something went wrong in input"}, status=status.HTTP_400_BAD_REQUEST)


# Login functionality
class Login(TokenObtainPairView):
    serializer_class = LoginSerializer
