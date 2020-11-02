from django.urls import path
from .views import Pagehomeview, Pageaboutview

urlpatterns = [
    path('', Pagehomeview.as_view(), name='page-home-view'),
    path('about/', Pageaboutview.as_view(), name='page-about-view')
]