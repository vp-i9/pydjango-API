from django.urls import path, include
from . import views

"""
add these for later:
Urls.py

In development for Django to serve your static files, you have to include the static URLs in your urls.py:

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = ...

urlpatterns += staticfiles_urlpatterns()

"""


app_name = "polls"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
    path("__debug__/", include("debug_toolbar.urls")),
]

# urlpatterns = [
#     # eg >>> /polls/
#     path("", views.index, name="index"),
#     # eg >>> /polls/5/
#     path("<int:question_id>/", views.detail, name="detail"),
#     # eg >>> /polls/5/results.html/
#     path("<int:question_id>/results.html/", views.results, name="results"),
#     # eg >>> /polls/5/vote/
#     path("<int:question_id>/vote/", views.vote, name="vote"),
# ]
