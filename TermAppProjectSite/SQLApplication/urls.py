from django.urls import path

from . import views

#Adds and creates HTML hyperlinks and adds them to the array which the the file TermAppProjectSite\urls.py will use.
urlpatterns=[
    path('',views.index),
    #path('WorkPlease',views.hello),
    path('TesterSQLQuery',views.TesterSQLQuery)
]