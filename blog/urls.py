from django.urls import  path, re_path
from . import views
from django.contrib.auth.views import LoginView, LogoutView, TemplateView
urlpatterns = [
    re_path(r'^$', views.post_list, name='post_list'),
    re_path(r'^post/new/$', views.post_new, name='post_new'),
    re_path(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    re_path(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
    path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    path('comment/<int:pk>/approve/', views.comment_approve, name='comment_approve'),
    path('comment/<int:pk>/remove/', views.comment_remove, name='comment_remove'),
    path('accounts/login/', views.LoginView.as_view(), name='login'),
    # urls.py
    path('accounts/logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('home/', TemplateView.as_view(template_name='home.html'), name='home'),
    path('drafts/', views.post_draft_list, name='post_draft_list'),
]