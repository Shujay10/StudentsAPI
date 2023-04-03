from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('Students.urls')),
    path('user1/', include('StudentsDFW.urls')),
]
