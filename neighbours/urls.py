from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url(r'^home/', views.index, name='index'),
    url(r'^$', views.home, name='index'),
    url(r'^user/(\d+)', views.person, name='user_profile'),
    url(r'^new_user_profile/$', views.new_person, name='NewPerson'),
    url(r'^edit_profile/$',views.edit_profile,name = 'edit_profile'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^business/', views.work, name='business'),
    url(r'^move/', views.moving, name='moved'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)