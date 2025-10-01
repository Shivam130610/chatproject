from django.urls import path
from . import views

urlpatterns = [
    # --- Page (browser) URLs ---
    path('register/', views.RegisterPageView.as_view(), name='register_page'),
    path('login/', views.LoginPageView.as_view(), name='login_page'),
    path('users/', views.UsersPageView.as_view(), name='users_page'),
    path('send-message/', views.SendMessagePageView.as_view(), name='send_message_page'),
    path('inbox/', views.InboxPageView.as_view(), name='inbox_page'),

    # --- API URLs (use /api/... to avoid conflict with page GETs) ---
    path('api/register/', views.RegisterView.as_view(), name='api_register'),
    path('api/login/', views.LoginAPIView.as_view(), name='api_login'),      # returns token
    path('api/users/', views.UserListAPI.as_view(), name='api_users'),
    path('api/send-message/', views.MessageCreateAPI.as_view(), name='api_send_message'),
    path('api/inbox/', views.MessageListAPI.as_view(), name='api_inbox'),
]
