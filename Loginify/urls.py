from django.urls import path

from . import views

urlpatterns = [
    # Task 2: test endpoint
    path("hello/", views.hello_world, name="hello_world"),

    # Task 3: signup & login with templates
    path("signup/", views.signup, name="signup"),
    path("login/", views.login, name="login"),

    # Task 5: CRUD API endpoints
    path("users/", views.get_all_users, name="get_all_users"),
    path("users/<str:email>/", views.get_user_by_email, name="get_user_by_email"),
    path("users/<str:email>/update/", views.update_user, name="update_user"),
    path("users/<str:email>/delete/", views.delete_user, name="delete_user"),
]
