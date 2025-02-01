from django.urls import path, include
from .views import homeView,loginview, logout_user, add_post,PostView
urlpatterns = [ 
	path('', homeView.as_view(), name='home'),
	path('login/', loginview, name='login'),
	path('logout/',logout_user,name='logout'),
	path('post/<int:pk>',PostView.as_view(),name="post-details"),
	path('add post/',add_post.as_view(),name='add_post'),
]
