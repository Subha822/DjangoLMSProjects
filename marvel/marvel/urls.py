from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("superadmin/", admin.site.urls),
    path("admin/", include("quiz.urls")),
    path("",include("home.urls")),
    path("admin/customer/", include("quiz.urls")),

]
