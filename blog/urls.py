from django.urls import path

from . import views

urlpatterns = [
    path('', views.PostList.as_view(), name='index'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    # path("<category>/", views.blog_category, name="blog_category"),
]