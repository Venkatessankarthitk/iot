from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path
from data.views import views
from django.views.generic import TemplateView

urlpatterns = [
    path('data', views.DataList.as_view(), name="DataList"),
    path('data/<int:pk>/', views.DataDetail.as_view(), name="DataDetail"),
    path('postdata', TemplateView.as_view(template_name="data.html"), name="postdata"),
    path('', auth_views.login, {'template_name': 'login.html'}, name='login'),
    path('logout/', auth_views.logout, {'next_page': '/'}, name='logout'),
    path('rpm', TemplateView.as_view(template_name="rpm.html"), name="rpm"),
    path('fuel', TemplateView.as_view(template_name="fuel.html"), name="fuel"),
    path('liverpm', views.LiveRPM, name="LiveRPM"),
    path('livespeed', views.LiveSPEED, name="LiveSPEED"),
    # path('postdata', views.hello_world)
]