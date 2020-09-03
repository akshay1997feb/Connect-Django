from django.conf.urls import url
from firstapp import views
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from rest_framework_simplejwt import views as jwt_views
# TEMPLATE URLS!
app_name = 'firstapp'

urlpatterns = [
    path('validate/token/', views.ValidateToken.as_view(), name='ValidateToken'),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/', views.AuthenticateUserApi.as_view(), name='auth'),
    path('basic/auth/', views.BasicAuthenticateUserApi.as_view(), name='auth'),
    path('newsfeed/', views.NewsFeedPost.as_view(), name='newsfeed'),
    path('user/main/info/', views.UserMainInfo.as_view(), name='userinfo'),
    path('user/profile/info/', views.UserProfile.as_view(), name='userinfo'),
    path('user/profile/pic/', views.UserGetProfilePic.as_view(), name='UserGetProfilePic'),
    path('user/feed/', views.UserFeed.as_view(), name='userfeed'),
    path('friend/list/', views.FriendsList.as_view(), name='friendslist'),
    path('friend/request/', views.FriendRequest.as_view(), name='friendrequest'),
    path('friend/edit/', views.Friend.as_view(), name='friend'),
    path('friend/mutual/', views.MutualFriendsList.as_view(), name='mutualfriend'),
    path('friend/count/', views.FriendCount.as_view(), name='PostCount'),
    path('friend/status/', views.FriendStatus.as_view(), name='FriendStatus'),
    path('register/', views.Register.as_view(), name='FriendCount'),
    path('post/', views.Posts.as_view(), name='post'),
    path('register/update/', views.RegisterUpdate.as_view(), name='registerupdate'),
    path('post/like/', views.Like.as_view(), name='like'),
    path('post/comment/', views.Comments.as_view(), name='comment'),
    path('post/comments/list/', views.PostCommentsList.as_view(), name='postcommentslist'),
    path('post/comments/count/', views.PostCommentsCount.as_view(), name='postcommentscount'),
    path('post/likes/list/', views.PostLikesList.as_view(), name='postlikeslist'),
    path('post/likes/count/', views.PostLikesCount.as_view(), name='postlikescount'),
    path('post/liked/', views.getLiked.as_view(), name='getLiked'),
    path('post/count/', views.PostCount.as_view(), name='PostCount'),
    path('post/delete/', views.PostDelete.as_view(), name='PostDelete'),
    path('post/latest/like/', views.LatestLikeOfPost.as_view(), name='LatestLikeOfPost'),
    path('post/latest/comments/', views.LatestCommentsOfPost.as_view(), name='LatestCommentsOfPost'),
    path('search/', views.Search.as_view(), name='Search'),




]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

'''
    #url(r'^register/$', views.register, name='register'),
    #url(r'^user_login/$', views.user_login, name='user_login'),
    url(r'^add_friend/(?P<pk>\w+)/$', views.add_friend, name='add_friend'),
    url(r'^accept_friend/(?P<pk>\w+)/$', views.accept_friend, name='accept_friend'),
    url(r'^profile/(?P<usrname>\w+)/$', views.profile, name='profile'),
    #url(r'^search/$', views.search, name='search'),
    path('friendlist/(?P<pk>\w+)/$',views.FriendListView.as_view(),name='friend_list'),
    path('postlist/',views.PostListView.as_view(),name='post_list'),
    url(r'^post/(?P<pk>\d+)/edit/$',views.PostUpdateView.as_view(),name='post_edit'),
    url(r'^post/(?P<pk>\d+)/remove/$',views.PostDeleteView.as_view(),name='post_remove'),
    #path('newsfeed/',views.NewsFeedPostListView.as_view(),name='news_feed'),
    path('post/new/',views.CreatePostView.as_view(),name='post_new'),
    url(r'^frienddetail/(?P<pk>\w+)/$',views.FriendDetailView.as_view(),name='friend_detail'),
    url(r'^postdetail/(?P<pk>\w+)/$',views.PostDetailView.as_view(),name='post_detail'),
    path('friendrequests/',views.FriendReqListView.as_view(),name='friend_req_list'),
    url(r'^deletefriend/(?P<pk>\w+)/$',views.delete_friend,name='delete_friend'),
    url(r'^post/(?P<pk>\d+)/comment/$',views.add_comment_to_post,name='add_comment_to_post'),
    #url(r'^comment/(?P<pk>\d+)/approve/$',views.comment_approve,name='comment_approve'),
    #url(r'^comment/(?P<pk>\d+)/remove/$',views.comment_remove,name='comment_remove'),
    url(r'^likesdetail/(?P<pk>\w+)/$',views.LikesListView.as_view(),name='likes_detail'),
    url(r'^ajax/validate_username/$', views.validate_username, name='validate_username'),
    #url(r'^like/(?P<pk>\d+)/post/$',views.like_post,name='like_post'),
    url(r'^unlike/(?P<pk>\d+)/post/$',views.unlike_post,name='unlike_post'),
     url(r'^like/(?P<pk>\d+)/checklike/$',views.liked_by_user,name='check_post'),
     url(r'^like/(?P<pk>\d+)/countlike/$',views.count_likes,name='count_likes'),
'''