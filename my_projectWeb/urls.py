"""my_projectWeb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
# Incluir la aplicacion al proyecto
from django.urls import include, path, re_path
# Convocar a las ulrs de las settings
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    re_path(r"^", include("myApp.urls")),
    path("i18n/", include("django.conf.urls.i18n")),
] + static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)