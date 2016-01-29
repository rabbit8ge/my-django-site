print('debug: start urls.')
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.http import HttpResponse
from blogs.views import blog_sitemap
from django.conf.urls.static import static

admin.autodiscover()

sitemaps = {
    'blogs': blog_sitemap
}
from django.conf import settings
urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'blogs.views.index', name='home'),
    url(r'^blogs/$', 'blogs.views.blogs', name='blogs'),
    url(r'^blogs/(?P<slug>[\w-]+)/$', 'blogs.views.blog_view', name='blog_view'),
    url(r'^blogs-category/(?P<slug>[\w-]+)/$', 'blogs.views.category_view', name='category_view'),
    url(r'^contact/$', 'blogs.views.contact', name='contact'),
    (r'^robots\.txt$', lambda r: HttpResponse("User-agent: *\nDisallow:", content_type="text/plain")),
    (r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),
    (r'^ckeditor/', include('ckeditor.urls')),

    url(r'^hypadmin/', include(admin.site.urls)),
)
print(include(admin.site.urls))

urlpatterns += patterns('', (
    r'^static/(?P<path>.*)$',
    'django.views.static.serve',
    {'document_root': settings.STATIC_ROOT, 'show_indexes':True}
))
#urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += patterns('', (
    r'^media/(?P<path>.*)$',
    'django.views.static.serve',
    {'document_root': settings.MEDIA_ROOT}
))
urlpatterns += patterns('', (
    r'^docs/(?P<path>.*)$',
    'django.views.static.serve',
    {'document_root': settings.DOCS_ROOT}
))

handler404 = 'blogs.views.handler404'

handler500 = 'blogs.views.handler500'

print('debug: end urls.')