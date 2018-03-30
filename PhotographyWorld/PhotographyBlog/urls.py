from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'PhotographyBlog'
urlpatterns = [
    url(r'^$',views.IndexView.as_view(), name='index'),
    url(r'^work/$',views.WorkView.as_view(), name='work'),
    url(r'^work/(?P<id>[0-9]+)/$',views.Work_detailView.as_view(), name='work_detail'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)