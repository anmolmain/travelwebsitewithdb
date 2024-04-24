from django.contrib import admin
from django.urls import path
from eventhorizon import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home,name="home"),
    path('trips/', views.trips,name="trips"),
    path('checkout/', views.checkout,name="checkout"),
    path('contactUs/', views.contactUs,name="contactUs"),
    path('save_booking//', views.save_booking, name='save_booking'),
    path("register/", views.register, name="register"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),

]
