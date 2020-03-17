from rest_framework.serializers import ModelSerializer
from v1.models import Quiz,Question,Profile
from rest_framework import serializers
from django.contrib.auth.models import User


class QuizSerializer(ModelSerializer):
    class Meta:
        model = Quiz
        fields = '__all__'



class QuestionSerializer(ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'



class ProfileSerializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'        


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password')

    def create(self, validated_data, instance=None):
        user = super(UserSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user      