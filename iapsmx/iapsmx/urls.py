from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = patterns('',)
    # Examples:
    # url(r'^$', 'iapsmx.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

# Components
# Personas
urlpatterns += patterns('',
                        url(r'^$', 'personas.views.home'),
                        url(r'^personas/',include('personas.urls', namespace='personas')),
                        url(r'^poms/',include('poms.urls', namespace='poms')),
                        url(r'^encuestas/', include('encuestas.urls', namespace='encuestas')),
                        url(r'^encuestas/discreta/', include('encuestas.urls', namespace='encuesta_discreta')),
                        url(r'^fin/$', 'personas.views.fin'),
                        url(r'^analysis/',include('analysis.urls', namespace='analysis')),
                        )

    #url(r'^admin/', include(admin.site.urls)),

if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'^media/(?P<path>.*)',
         'serve',
         {'document_root': settings.MEDIA_ROOT}), )

    urlpatterns += patterns('',
                            url(r'^404/$', 'django.views.defaults.page_not_found'),
                            url(r'^500/$', 'django.views.defaults.server_error'),
                            )



