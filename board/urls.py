from django.urls import path
from .views import (StoryList, StoryCreate, StoryDetail,
                    StoryUpdate, StoryDelete, VoteAdd,
                    CommentCreate, CommentDetail, CommentUpdate,
                    CommentDelete)


urlpatterns = [
    path('story/list/', StoryList.as_view(), name='stories list'),
    path('story/create/', StoryCreate.as_view(), name='story_create'),
    path('story/<int:pk>/detail/', StoryDetail.as_view(), name='story_detail'),
    path('story/<int:pk>/update/', StoryUpdate.as_view(), name='story_update'),
    path('story/<int:pk>/delete/', StoryDelete.as_view(), name='story_delete'),
    path('vote/add/', VoteAdd.as_view(), name='vote_add'),
    path('comment/create/', CommentCreate.as_view(), name='comment_create'),
    path('comment/<int:pk>/detail/', CommentDetail.as_view(),
         name='comment_detail'),
    path('comment/<int:pk>/update/', CommentUpdate.as_view(),
         name='comment_update'),
    path('comment/<int:pk>/delete/', CommentDelete.as_view(),
         name='comment_delete')
]
