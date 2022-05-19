from django.contrib import admin
from django.urls import path
from mainApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('shop/<str:mc>/<str:sc>/<str:br>/', views.shop),
    path('product/<int:id>/',views.product),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
