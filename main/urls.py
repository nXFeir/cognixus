from django.contrib import admin
from django.urls import include, path

from django.views.generic import TemplateView


class Home(TemplateView):
    template_name = 'home.html'

app_urls = [
    path('', include('todo.urls')),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(app_urls)),
    path('accounts/', include('allauth.urls')), 
    path('', Home.as_view(), name='home'), 

] 

admin.site.site_header = 'Cognixus Back Office'
admin.site.index_title = 'Cognixus'
admin.site.site_title  =  "Admin"