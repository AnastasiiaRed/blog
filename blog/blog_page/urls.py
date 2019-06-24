from django.urls import path
from blog_page import views
 
urlpatterns = [
    path('addcomment/', views.addcomment)
]