from django.contrib import admin
from django.urls import path
from App import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.add_show_student, name="addandshow"),
    path("delete/<int:id>/", views.delete_student, name="deletestudent"),
    path("update/<int:id>/", views.update_student, name="updatestudent"),
]
