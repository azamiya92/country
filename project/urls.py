from django.conf.urls import include, url
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^countrylist/$','main.views.countrylist'),
    url(r'^country/(?P<pk>\d+)/$','main.views.countrydetail'),
    url(r'^createcountry/$','main.views.createcountryform'),
    url(r'^sign_up/$', 'main.views.sign_up'),
    url(r'^signin/$', 'main.views.signin'),
    url(r'^signout/$', 'main.views.signout'),
    url(r'^editreview/(?P<pk>\d+)/$', 'main.views.editreview'),
    url(r'^deletereview/(?P<pk>\d+)/$', 'main.views.deletereview'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



