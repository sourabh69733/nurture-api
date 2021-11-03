from django.urls import path
from api import views

app_name = 'api'
urlpatterns = [
    path("admin/advisor", views.advisor_create_or_list ),
    path("admin/<int:userId>/advisor", views.advisor_create_or_list),
    path("user/register", views.user_create_or_list ),
    path("user/login", views.user_login ),
    path("user/<int:userId>/advisor/<int:advisorId>", views.book_advisor_call),
    path("user/<int:user_id>/advisor/booking", views.list_booking),
]
