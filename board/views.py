from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import (
    StorySerializer,
    StoryDetailSerializer,
    VoteSerializer,
    CommentSerializer,
)
from .permissions import IsCreator
from .models import Story, Vote, Comment


class StoryList(generics.ListAPIView):
    serializer_class = StorySerializer

    def get_queryset(self):
        stories = Story.objects.all()
        return stories


class StoryCreate(generics.CreateAPIView):
    """API for story creation"""

    serializer_class = StorySerializer
    permission_classes = [
        IsAuthenticated,
    ]


class StoryDetail(generics.RetrieveAPIView):
    """API for show story's details"""

    queryset = Story.objects.all()
    serializer_class = StoryDetailSerializer


class StoryUpdate(generics.UpdateAPIView):
    """API for changing story """

    queryset = Story.objects.all()
    serializer_class = StorySerializer
    permission_classes = [
        IsCreator,
    ]
    http_method_names = [
        "patch",
    ]


class StoryDelete(generics.DestroyAPIView):
    """API for delete story """

    queryset = Story.objects.all()
    serializer_class = StorySerializer
    permission_classes = [
        IsCreator,
    ]


class VoteAdd(generics.CreateAPIView):
    """Api for add vote for srory"""

    serializer_class = VoteSerializer
    permission_classes = [
        IsAuthenticated,
    ]

    def post(self, request, *args, **kwargs):
        story = Story.objects.get(pk=request.data["story"])
        if story.created_by != request.user and not Vote.objects.filter(
            story=story, created_by=request.user
        ):
            return self.create(request, *args, **kwargs)
        else:
            return Response(
                {"You do not have permissions"},
                status=status.HTTP_400_BAD_REQUEST
            )


class CommentCreate(generics.CreateAPIView):
    """API for comment creation"""

    serializer_class = CommentSerializer
    permission_classes = [
        IsAuthenticated,
    ]


class CommentDetail(generics.RetrieveAPIView):
    """API for show comment's details"""

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentUpdate(generics.UpdateAPIView):
    """API for comment update"""

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [
        IsCreator,
    ]
    http_method_names = [
        "patch",
    ]


class CommentDelete(generics.DestroyAPIView):
    """API for comment delete"""

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [
        IsCreator,
    ]
