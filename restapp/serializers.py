from rest_framework import serializers
from .models import User, Client, Server, Camera, Entering, Exiting


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
        "id",
        'firstname',
        'lastname',
        'username',
        'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }


    def create(self, validated_data):
        auth_user = User.objects.create_user(**validated_data)
        return auth_user

class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = [
        "id",
        'FirstName',
        'LastName',
        'CarModel',
        'CarNumber',
        'PhoneNumber',
        'CreatedAt',
        'UpdatedAt',
        'CreatedUserId'
        ]



class ServerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Server
        fields = [
        "id",
        'ServerIP',
        'ServerPort',
        'ServerLogin',
        'ServerPassword',
        'CreatedUserld',
        ]

class CameraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Camera
        fields = [
        'id',
        "CamPort",
        'CamIP',
        'CamLogin',
        'CamPassword',
        'CreatedUserld',
        ]

class ClientUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = [
        'FirstName',
        'LastName',
        'CarModel',
        'CarNumber',
        'PhoneNumber',
        'UpdatedAt'
        ]

class ClientCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = [
        'FirstName',
        'LastName',
        'CarModel',
        'CarNumber',
        'PhoneNumber',
        'CreatedAt',
        'UpdatedAt',
        'CreatedUserId'
        ]
    def create(self, validated_data):
        return Client.objects.create(**validated_data)

class EnteringSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entering
        fields = [
        "id",
        'ClientId',
        'EnteringTime',
        'CreatedAt',
        'UpdatedAt'
        ]

class EnteringCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entering
        fields = [
        'ClientId',
        'EnteringTime',
        'CreatedAt',
        'UpdatedAt'
        ]
    def create(self, validated_data):
        return Entering.objects.create(**validated_data)




class ExitingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exiting
        fields = [
        "id",
        'ClientId',
        'ExitingTime',
        'CreatedAt',
        'UpdatedAt'
        ]
class ExitingCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exiting
        fields = [
        'ClientId',
        'ExitingTime',
        'CreatedAt',
        'UpdatedAt'
        ]
    def create(self, validated_data):
        return Exiting.objects.create(**validated_data)

class ExitingSerializerSt(serializers.ModelSerializer):
    class Meta:
        model = Exiting
        fields = [
        'CreatedAt',
        ]
        # depth=1

class StatesSerializer(serializers.ModelSerializer):
    exiting = ExitingSerializerSt(many=True)
    enter = EnteringSerializer(many=True)
    class Meta:
        model = Client
        fields = [
        "id",
        'FirstName',
        'LastName',
        'CarNumber',
        'exiting',
        'enter'
        ]







