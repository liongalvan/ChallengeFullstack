from django.contrib import admin
from django.urls import path
from apis import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.bank, name='optionbank'),
    path('signin', views.signin, name='signin'),
    path('data/', views.data, name='data'),
    path('bank/', views.bank, name='bank'),
]
