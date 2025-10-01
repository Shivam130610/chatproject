from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth import authenticate
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken

from django.contrib.auth.models import User
from .models import Message
from .serializers import RegisterSerializer, UserSerializer, MessageSerializer

# ---------- API Views (same as earlier but under /api/) ----------

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

class LoginAPIView(ObtainAuthToken):
    # returns token on POST with username & password
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        token = response.data.get('token')
        if token:
            tok = Token.objects.get(key=token)
            return Response({
                "token": tok.key,
                "user_id": tok.user_id,
                "username": tok.user.username
            })
        return Response(response.data, status=response.status_code)

class UserListAPI(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class MessageCreateAPI(generics.CreateAPIView):
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]
    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)

class MessageListAPI(generics.ListAPIView):
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        user = self.request.user
        return Message.objects.filter(receiver=user).order_by("-timestamp")

# ---------- Template / Page Views (render HTML) ----------

class RegisterPageView(TemplateView):
    template_name = "chatapp/register.html"

class LoginPageView(TemplateView):
    template_name = "chatapp/login.html"

class UsersPageView(TemplateView):
    template_name = "chatapp/users.html"

class SendMessagePageView(TemplateView):
    template_name = "chatapp/send_message.html"

class InboxPageView(TemplateView):
    template_name = "chatapp/inbox.html"
