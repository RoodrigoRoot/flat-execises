from django.urls import path
from users.views import CreateProfileAPIView


urlpatterns = [
    path('', CreateProfileAPIView.as_view(), name='create_profile')
]


