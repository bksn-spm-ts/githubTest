from django.urls import path

from . import views
urlpatterns = [
    path('', views.index, name='index'),
    # https://localhost:8000/oauthDemo/callback?code=CBNCKBAAHBCAABAAilN0aSwcNhJyeMBqhp9jk65BajhrHPqV&state=hogefuga
    path('callback', views.callback, name='callback'),
    path('token', views.index, name='token'),
]
