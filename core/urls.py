from django.urls import path
from .views import (
    PostListView, PostDetailView,
    PostCreateView, PostUpdateView, PostDeleteView,
    donate, donation_thank_you
)

urlpatterns = [
    path('donate/', donate, name='donate'),
    path('thank-you/', donation_thank_you, name='donation_thank_you'),
    path('', PostListView.as_view(), name='post_list'),

    # CRUD (order matters: new/edit/delete before slug)
    path('post/new/', PostCreateView.as_view(), name='post_new'),
    path('post/<slug:slug>/edit/', PostUpdateView.as_view(), name='post_edit'),
    path('post/<slug:slug>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('post/<slug:slug>/', PostDetailView.as_view(), name='post_detail'),
]
