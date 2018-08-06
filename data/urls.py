from django.contrib import admin
from django.urls import include, path
from data.views import views
from django.views.generic import TemplateView

urlpatterns = [
    path('data', views.DataList.as_view(), name="DataList"),
    path('data/<int:pk>/', views.DataDetail.as_view(), name="DataDetail"),
    path('postdata', TemplateView.as_view(template_name="data.html")),
    # path('postdata', views.hello_world)
]