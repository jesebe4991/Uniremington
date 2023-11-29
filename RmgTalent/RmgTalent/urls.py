"""
URL configuration for RmgTalent project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from MainApp import views


urlpatterns = [
    path('admin/', admin.site.urls),    
    path (' ', include('MainApp.urls')),
    path (' ', include('DtaOfertas.urls')),
    
    #path('', views.index),
    #path('index', views.index),
    #path('index.html', views.index),
    
    #    Ofertas
    #path('Ofertas/',include('DtaOfertas.urls')),
    #path('job_listing', views.job_listing),
    #path('job_listing.html', views.job_listing),
    
    #    Ofertas/Detalles
    path('job_details', views.job_details),
    path('job_details.html', views.job_details),
    
    #    Pagína/Aplicaciones    
    path('applications', views.applications),
    path('applications.html', views.applications),
    
    #    Ofertas/Perfil
    # path('index', views.index),
    # path('index.html', views.index),
]

#ruta de imagenes
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


    