from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('pages.urls'), name='home'),
    path('admin/', admin.site.urls),
    path('blog/', include('Blog.urls', namespace='blog')),
]
