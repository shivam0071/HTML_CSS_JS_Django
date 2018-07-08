from django.urls import path, re_path
from basic_app import views

app_name = 'basic_app'

urlpatterns = [
    # path('', views.index), #non class based method
    path('',views.SchoolListView.as_view(),name='list'), # class based views way...name=list is used in base.html
    re_path(r'(?P<pk>[-\w]+)/$',views.SchoolDetailView.as_view(),name='basic_app1'),
    # re_path(r'^(?P<pk>[-\w]+)/$', views.SchoolDetailView.as_view(),name='detail'),
    # path ('/<str:pk>/',views.SchoolDetailView.as_view(),name='detail2'),
    # path ('1',views.SchoolDetailView.as_view(),name='detail3'),
    # re_path(r'^(?P<pk>[0-9])/$', views.SchoolDetailView.as_view(),name='detail')
    #(?P<year>[0-9]{4})/$'
]
