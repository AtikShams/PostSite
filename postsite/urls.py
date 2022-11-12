from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('all/', views.all,name='all'),
    path('signup/', views.signup),
    path('login/', views.lin,name='login'),
    path('logout/', views.lout),
    path('seepost/', views.seepost,name='seepost'),
    path('createpost/', views.createpost,name='createpost'),
    path('update/<idup>', views.update, name="up"),
    path('delete/<iddel>', views.delete, name="del"),

]
