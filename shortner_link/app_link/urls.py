from django.urls import path
from . import views

urlpatterns = [
    path('', views.info_users, name='users'),
    path('registration/', views.registration, name='registration'),
    path('authorization/', views.authorization, name='authorization'),
    path("logout/", views.users_logout, name="logout"),
    path('create', views.add_link, name='create'),
    path('<str:pk>', views.shorten_link, name='shorten'),
    # path('info_urls/', views.info_urls, name='info_urls'),
    path('info_urls/', views.post, name='info_urls'),
]

