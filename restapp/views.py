from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, UpdateAPIView
from rest_framework.response import Response
from .serializers import UserSerializer, ClientSerializer,StatesSerializer,ExitingCreateSerializer, ServerSerializer, CameraSerializer, EnteringCreateSerializer,ClientUpdateSerializer, ClientCreateSerializer, EnteringSerializer, ExitingSerializer
from .models import User, Client, Server, Entering, Exiting, Camera
from rest_framework import status
from django.http import Http404
from django.contrib.auth import authenticate
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

class AuthUserRegistrationView(APIView):
    permission_classes = (AllowAny, )
    def post(self, request, *args, **kwargs):

        serializer = UserSerializer(data=request.data)

        for user in User.objects.all():
            if not user:
                break
            else:
                try:
                    Token.objects.get(user_id=user.id)
                except Token.DoesNotExist:
                    Token.objects.create(user=user)

        if serializer.is_valid():
            user = serializer.save()
            token = Token.objects.create(user=user)

            return Response(
                {
                    "user": {
                        "id": serializer.data["id"],
                        "firstname": serializer.data["firstname"],
                        "lastname": serializer.data["lastname"],
                        "username": serializer.data["username"],
                    },
                    "status": {
                        "message": "User created",
                        "code": f"{status.HTTP_200_OK} OK",
                    },
                    "token": token.key,
                }
            )
        return Response(
             {
                "error": serializer.errors,
                "status": f"{status.HTTP_203_NON_AUTHORITATIVE_INFORMATION}\
                    NON AUTHORITATIVE INFORMATION",
                }
        )

class UserLoginView(APIView):
    permission_classes = (AllowAny, )

    def post(self, request):
        user = authenticate(username=request.data.get('username'), password=request.data.get('password'))
        if user is None:
            return Response({"error": "xatolik"}, status=status.HTTP_404_NOT_FOUND)
        token, is_create = Token.objects.get_or_create(user=user)
        response = Response()

        response.set_cookie(key='token', value=token.key)
        response.data = {
            "ok": status.HTTP_200_OK,
            'token': token.key,
            "id": token.user.id,
            "username": token.user.username,
        }
        return response

class UserList(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = (DjangoFilterBackend,SearchFilter)
    filter_fields = (
        'id',
        'username'
        )

class UserById(APIView):
    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = UserSerializer(snippet)
        return Response(serializer.data)

class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('token')
        response.data = {
            'message': 'success'
        }
        return response

class ClientList(ListAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class ClientListStates(ListAPIView):
    queryset = Client.objects.all()
    serializer_class = StatesSerializer

class ClientCreate(APIView):
    serializer_class = ClientCreateSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        valid = serializer.is_valid(raise_exception=True)

        if valid:
            serializer.save()
            status_code = status.HTTP_201_CREATED

            response = {
                'success': True,
                'statusCode': status_code,
                'message': 'User successfully registered!',


            }

            return Response(response, status=status_code)


class ClientDetail(UpdateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientUpdateSerializer



class ClientById(APIView):
    def get_object(self, pk):
        try:
            return Client.objects.get(pk=pk)
        except Client.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = ClientSerializer(snippet)
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ServerList(ListAPIView):
    queryset = Server.objects.all()
    serializer_class = ServerSerializer


class EnteringList(ListAPIView):
    queryset = Entering.objects.all()
    serializer_class = EnteringSerializer

class EnteringById(APIView):
    def get_object(self, pk):
        try:
            return Entering.objects.get(pk=pk)
        except Entering.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = EnteringSerializer(snippet)
        return Response(serializer.data)


class EnteringCreate(APIView):
    serializer_class = EnteringCreateSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        valid = serializer.is_valid(raise_exception=True)

        if valid:
            serializer.save()
            status_code = status.HTTP_201_CREATED

            response = {
                'success': True,
                'statusCode': status_code,
                'message': 'User successfully registered!',
            }
            return Response(response, status=status_code)








class ExitingList(ListAPIView):
    queryset = Exiting.objects.all()
    serializer_class = ExitingSerializer

class ExitingById(APIView):
    def get_object(self, pk):
        try:
            return Exiting.objects.get(pk=pk)
        except Exiting.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = ExitingSerializer(snippet)
        return Response(serializer.data)


class ExitingCreate(APIView):
    serializer_class = ExitingCreateSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        valid = serializer.is_valid(raise_exception=True)

        if valid:
            serializer.save()
            status_code = status.HTTP_201_CREATED
            response = {
                'success': True,
                'statusCode': status_code,
                'message': 'User successfully registered!',
            }

            return Response(response, status=status_code)



class CameraList(ListAPIView):
    queryset = Camera.objects.all()
    serializer_class = CameraSerializer


class CameraById(APIView):
    def get_object(self, pk):
        try:
            return Camera.objects.get(pk=pk)
        except Camera.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = CameraSerializer(snippet)
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CameraCreate(APIView):
    serializer_class = CameraSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        valid = serializer.is_valid(raise_exception=True)

        if valid:
            serializer.save()
            status_code = status.HTTP_201_CREATED

            response = {
                'success': True,
                'statusCode': status_code,
                'message': 'User successfully registered!',


            }

            return Response(response, status=status_code)









