from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from main_app import views
from faq import views_faq

"""bilberry URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'', views.home),
    path('contact_photo', views.contact_photo, name="contact_photo"),
    path('viewer/<id_photo>/<choice_flag>', views.image_viewer, name="viewer"),
    path('list', views.image_list, name="list"),
    path('faq', views_faq.faq, name="faq")
]

if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)