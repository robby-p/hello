from django.urls import include, path
from django.contrib import admin
from django.contrib.auth import views as auth_views


from . import views


urlpatterns = [
    path("", views.PostList.as_view(), name="home"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("admin/", admin.site.urls),
    path("login/", auth_views.LoginView.as_view(template_name="login.html")),
    path("post/<slug:slug>/", views.PostDetail.as_view(), name="post_detail"),
]
