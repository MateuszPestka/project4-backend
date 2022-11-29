from django.urls import path
from posts import views
from django.urls import include

urlpatterns = [
    path('posts/', views.PostList.as_view()),
    path('posts/<int:pk>/', views.PostDetail.as_view()),
    path('summernote/', include('django_summernote.urls')),
]
