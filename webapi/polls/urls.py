
# -*- coding: utf-8 -*-
"""
    webapi.polls.urls
    ~~~~~~~~~~~

    DESCRIPTION

    :copyright: (c) 2018 by  Raymond.
    :last modified by 2018-09-10 11:36:42
"""

from django.urls import path
from . import views


app_name = "polls"
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<int:q_id>/vote", views.vote, name="vote")
]
