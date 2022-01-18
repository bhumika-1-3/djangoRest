# class to convert objects to json object

from rest_framework import serializers
from base.models import Room
from base.models import Topic, extra
from django.contrib.auth.models import User
from rest_framework.response import Response
from django.contrib.auth import authenticate, login, logout

class RoomSerializers(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'


class TopicSerializers(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = '__all__'


class todoSerializers(serializers.ModelSerializer):
    class Meta:
        model = extra
        fields = '__all__'


class RegisterSerializers(serializers.ModelSerializer):

    # password2 = serializers.CharField(
    #     style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = [
            'username',
            'password',
            # 'password2',
            'email',
        ]
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def save(self):
        user = User.objects.create(
            email=self.validated_data['email'],
            username=self.validated_data['username'],
            # password=self.validated_data['password'],
        )

        password = self.validated_data['password'],
        # password2=self.validated_data['password2'],

        # if password != password2:
        #     raise serializers.ValidationError({'password': 'passwords must match.'})
        user.set_password(password[0])

        user.save()
        return user


# login user
class LoginSerializers(serializers.ModelSerializer):

    # password2 = serializers.CharField(
    #     style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = [
            'username',
            'password',
        ]
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def validate(self, attrs):
        username = attrs.get('username', '')
        password = attrs.get('password', '')
        try:
            myuser = User.objects.get(username=username)
        except:
            return Response('User does not exist')

        # error or give a user object of the user
        user = authenticate(username=username, password=password)

        if not user:
            # create a session id in the cookies
            return Response('Invalid data')

        else:
            login(user)
            return Response('Correct data')

        # return super().validate(attrs)

    # def save(self):
    #     user = User(
    #         username=self.validated_data['username'],
    #         password=self.validated_data['password'],
    #     )

        # password=self.validated_data['password'],
        # password2=self.validated_data['password2'],

        # if password != password2:
        #     raise serializers.ValidationError({'password': 'passwords must match.'})
        # user.set_password(password)

        # user.save()
        # return user
