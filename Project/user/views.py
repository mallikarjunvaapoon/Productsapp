from django.shortcuts import render
from .models import UserModel
from .serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework import viewsets
from connections.models import Connection_request
from connections.serializers import RequestSerializer
import jwt

class Register(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class Login(APIView):

    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        user = UserModel.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationFailed('User not found!')

        if user.password != password:
            raise AuthenticationFailed('Incorrect password!')

        token = jwt.encode({
            'id': user.id,
        },
            'secret', algorithm='HS256').decode('utf-8')

        response = Response()

        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {
            'jwt': token
        }
        return response

class UserView(APIView):

    def get(self, request):

        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed('Unauthenticated!')

        try:
            payload = jwt.decode(token, 'secret', algorithm=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')

        user = UserModel.objects.get(id=payload['id'])
        serializer = UserSerializer(user)
        return Response(serializer.data)

class Update(APIView):
    def patch(self, request):

        user = request.data['id']
        obj = Connection_request.objects.get(id=user)
        obj.status_of = request.data['status_of']
        obj.save()
        return Response('Updated')


class NotificationsView(APIView):
    def get(self, request):
        token = request.COOKIES.get('jwt')
        payload = jwt.decode(token, 'secret', algorithm=['HS256'])
        user = UserModel.objects.get(id=payload['id'])
        sender = Connection_request.objects.filter(sender__id=user.id).values('status_of', 'sender__id',
                                                'sender__name', 'receiver__id', 'receiver__name')
        receiver = Connection_request.objects.filter(receiver__id=user.id).values('id', 'receiver__id',
                                                'receiver__name','sender__id', 'sender__name', 'status_of', )

        message1 = {"message": "send notification block"}
        message2 = {"message": "received notification block"}

        data = (message1, sender, message2, receiver)

        return Response(data)


class Send_request(viewsets.ModelViewSet):
    queryset = Connection_request.objects.all()
    serializer_class = RequestSerializer