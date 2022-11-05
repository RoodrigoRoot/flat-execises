from django.urls import path

from properties.views import CreatePropertiesAPIView

urlpatterns = [

    path("", CreatePropertiesAPIView.as_view(), name="create_property"),

]

