from django.urls import path
from .views import SignUpView, renderAccountView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='sign_up'),
    path('account/', renderAccountView, name='account'),
]