from .models import Connection_request
from .serializers import RequestSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from user.models import UserModel
import jwt

class SenderView(APIView):
    def get(self, request):

        token = request.COOKIES.get('jwt')
        payload = jwt.decode(token, 'secret', algorithm=['HS256'])
        user = UserModel.objects.get(id=payload['id'])
        sender = Connection_request.objects.filter(sender__id=user.id).values('requested', 'sender__id',
                                                'sender__name', 'receiver__id', 'receiver__name')

        return Response(sender)


class ReceivedView(APIView):
    def get(self, request):
        token = request.COOKIES.get('jwt')
        payload = jwt.decode(token, 'secret', algorithm=['HS256'])
        user = UserModel.objects.get(id=payload['id'])
        receiver = Connection_request.objects.filter(receiver__id=user.id).values('id', 'receiver__id',
                                                                                  'receiver__name', 'sender__id',
                                                                                  'sender__name', 'requested', )

        return Response(receiver)


class RequestView(APIView):
    def post(self, request):
        serializer = RequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class UpdateView(APIView):
    def patch(self, request):

        user = request.data['id']
        obj = Connection_request.objects.get(id=user)
        obj.requested = request.data['requested']
        obj.save()
        return Response('Updated')




