from rest_framework import serializers
from api.models import User, Booking, Advisor
from django.db import models

# class UserSerializer(serializers.ModelSerializer):
    # class Meta:
        # model = User
        # fields = ['id', 'name', 'email', 'password']

class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    email = serializers.EmailField(max_length=100 )
    password = serializers.CharField(max_length=20)

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.password = validated_data.get('password', instance.password)
        instance.save()
        return instance

class BookingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Booking
        fields = ["id", "time", "user", "advisor"]

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        print(validated_data)
        return Booking.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.time = validated_data.get('time', instance.time)
        instance.user_id = validated_data.get('user_id', instance.user_id)
        instance.advisor_id = validated_data.get('advisor_id', instance.advisor_id)
        instance.save()
        return instance

class AdvisorSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    photoUrl = serializers.URLField()

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Advisor.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.photoUrl = validated_data.get('photoUrl', instance.photoUrl)
        instance.save()
        return instance
