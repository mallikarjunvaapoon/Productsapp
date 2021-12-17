from .models import Feed, Comment
from .serializers import FeedSerializer, CommentSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


class FeedView(APIView):
    def get(self, request):
        user = Feed.objects.all()
        serializer = FeedSerializer(user, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = FeedSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class CommentView(APIView):
    def get(self, request):
        user = Comment.objects.all()
        serializer = CommentSerializer(user, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CommentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
