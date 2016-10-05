from django.conf.urls import url
from . import PYToconnect,views
"""can also write from sagiApp import PYToconnect"""

urlpatterns=[
	url(r'^$',PYToconnect.classA.as_view()),
	url(r'^HTMLLinkA/$',PYToconnect.classB.as_view()),
	url(r'^go',PYToconnect.classC.as_view()),
	url(r'^first',views.sagi_view_A, name='my_svA'),
]