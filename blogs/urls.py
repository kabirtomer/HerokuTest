from django.urls import path

from .views import *

urlpatterns = [
    path('blogs/', new_topic, name='blogs'),
    path('blogs/post/new/', new_topic, name='post_new'),
    path('blogs/post/<int:pk>/edit', BlogEditView.as_view(), name='post_edit'),
    path('blogs/post/<int:pk>/delete', BlogDeleteView.as_view(), name='post_delete'),
    path('accounts/signup', SignUpView.as_view(), name='signup'),
]
