from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Message, MessageStatus


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password']
        )
        return user


class MessageSerializer(serializers.ModelSerializer):
    sender = UserSerializer(read_only=True)
    receiver = UserSerializer(read_only=True)

    class Meta:
        model = Message
        fields = ['id', 'sender', 'receiver', 'text', 'timestamp']


class MessageStatusSerializer(serializers.ModelSerializer):
    message = MessageSerializer(read_only=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = MessageStatus
        fields = ['id', 'message', 'user', 'is_read', 'is_delivered', 'updated_at']
