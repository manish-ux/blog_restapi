from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [
       path('users/list/',views.UserList.as_view(),name="userlist"),
       path('users/details/<int:pk>/',views.UserRetrieve.as_view(),name="userdetails"),
       path('users/create/',views.UserCreate.as_view(),name="usercreate"),
       path('users/update/<int:pk>/',views.UserUpdate.as_view(),name="userupdate"),
       path('users/destroy/',views.UserDestroy.as_view(),name="userdestroy"),
       path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
       path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
       path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
       path('users/comments/',views.CommentList.as_view(),name="commentlist"),
       path('users/comments/create/<int:pk>/',views.CommentDetail.as_view(),name="commentdetails"),
       ]


