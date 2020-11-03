from django.urls import path
from .views import (
    BlogListView,
    BlogDetailView, 
    BolgCreateView, 
    BlogUpdateView,
    BlogDeleteView,
)

urlpatterns = [
    path('', BlogListView.as_view(), name='home-page'),
    path('post/<int:pk>', BlogDetailView.as_view(), name='post-detail'),
    path('post/new/', BolgCreateView.as_view(), name='post-new' ),
    path('post/<int:pk>/update/', BlogUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', BlogDeleteView.as_view(), name='post-delete'),
]