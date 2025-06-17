from django.urls import path
from .views import (
    home_view,
    PostListView, PostDetailView,
    PostCreateView, PostUpdateView, PostDeleteView,
    donate, donation_thank_you,
    contact_view, contact_thank_you  
)
from .views import types_of_abuse_view


urlpatterns = [
    path('', home_view, name='home'),
    path('donate/', donate, name='donate'),
    path('thank-you/', donation_thank_you, name='donation_thank_you'),
    path('contact/', contact_view, name='contact'),
    path('contact/thank-you/', contact_thank_you, name='contact_thank_you'),

    path('news/', PostListView.as_view(), name='post_list'),
    path('post/new/', PostCreateView.as_view(), name='post_new'),
    path('post/<slug:slug>/edit/', PostUpdateView.as_view(), name='post_edit'),
    path('post/<slug:slug>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('post/<slug:slug>/', PostDetailView.as_view(), name='post_detail'),
    path('types-of-abuse/', types_of_abuse_view, name='types_of_abuse'),

]
