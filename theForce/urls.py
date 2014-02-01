from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	# DO I NEED TO CHANGE THIS???
	url(r'^database/admin/', include(admin.site.urls)),
	url(r'^$',  'theForce.views.index'),
	url(r'^auth/$',  'theForce.views.auth_view'),
	url(r'^logout/$', 'theForce.views.logout'),
	url(r'^loggedin/$', 'theForce.views.loggedin', name='loggedin'),
	url(r'^invalid/$', 'theForce.views.invalid_login'),
	# registration   
	url(r'^register/$', 'theForce.views.register_user'),
	url(r'^register_success/$', 'theForce.views.register_success'),
)