from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('courses/', views.course_list, name='course_list'),
    path('add/', views.add_course, name='add_course'),
    path('edit/<int:pk>/', views.edit_course, name='edit_course'),
    path('delete/<int:pk>/', views.delete_course, name='delete_course'),
]
