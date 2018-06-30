from django.conf.urls import patterns, include, url

urlpatterns = patterns('', 
url(r'^kpi/', 'app1.views.kpi', name = 'kpi'),
url(r'^kpidetails/', 'app1.views.kpidetails', name = 'kpidetails'),
url(r'^xunit/', 'app1.views.xunit', name = 'xunit'),
url(r'^mstest/', 'app1.views.mstest', name = 'mstest'),



)
