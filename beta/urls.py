from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'beta.views.index', name='index'),
    url(r'^(?P<url_hash>[a-zA-z0-9]{32})/$', 'beta.views.visiturl', name='visiturl'),
    # url(r'^$', 'standalonemodules.views.home', name='home'),
    # url(r'^standalonemodules/', include('standalonemodules.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
