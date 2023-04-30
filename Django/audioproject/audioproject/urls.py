from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('audio-blog/', views.audio_blog_view, name='audio_blog'),
]
